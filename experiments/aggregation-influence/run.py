"""Measure metadata influence through unmodified, pinned coordinator code."""

from __future__ import annotations

import argparse
import hashlib
import importlib
import json
import math
import platform
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent


def verify_sources(root: Path) -> dict:
    manifest = json.loads((HERE / "sources.json").read_text())
    for item in manifest["files"]:
        data = (root / item["path"]).read_bytes()
        if hashlib.sha256(data).hexdigest() != item["sha256"]:
            raise ValueError(f"Source mismatch: {item['path']}")
    return manifest


def setup(root: Path) -> tuple:
    manifest = verify_sources(root)
    sys.path[:0] = [str(root / "src"), str(root / manifest["validator_path"])]
    core = importlib.import_module(manifest["package"] + ".training.consortium")
    gate = importlib.import_module("contribution_validator.gate")
    for module_name, expected in [
        (manifest["package"] + ".training.consortium.coordinator", root / manifest["coordinator_path"]),
        ("contribution_validator.gate", root / manifest["validator_path"] / "contribution_validator/gate.py"),
    ]:
        module = importlib.import_module(module_name)
        if Path(module.__file__).resolve() != expected.resolve():
            raise ValueError(f"Imported wrong source: {module_name}")
    return manifest, core, gate


def safe_number(value: float) -> float | str:
    if math.isfinite(value):
        return value
    return "NaN" if math.isnan(value) else ("+Infinity" if value > 0 else "-Infinity")


def measure(core, gate, case: str, scores: dict[str, float], *, weighting="quality", cap=1.0,
            floor=0.0, path="core", quorum=1, values=None) -> dict:
    import torch

    values = values or {"alpha": 0.0, "beta": 2.0, "gamma": 10.0}
    values = {key: values[key] for key in scores}

    class ScalarModel(torch.nn.Module):
        def __init__(self):
            super().__init__()
            self.weight = torch.nn.Parameter(torch.tensor([0.0], dtype=torch.float64))

    class FixedNode:
        def __init__(self, node_id):
            self.node_id = node_id

        def run_sovereign_cycle(self, round_num, _base_state):
            state = {"weight": torch.tensor([values[self.node_id]], dtype=torch.float64)}
            artifact = core.SovereignModelArtifact(self.node_id, "fixture", "fixed", state)
            contribution = core.SovereignContribution(self.node_id, round_num, state, scores[self.node_id], 1)
            return core.SovereignCycleResult(artifact, contribution)

    policy = core.ContributionPolicy(quality_floor=floor, max_node_weight=cap, weighting=weighting)
    model = ScalarModel()
    coordinator = (core.ConsortiumCoordinator(model, policy) if path == "core" else
                   gate.ValidatingConsortiumCoordinator(model, policy, min_admitted_nodes=quorum))
    result = coordinator.run_round([FixedNode(node_id) for node_id in scores])
    weights = result.contribution_weights
    finite = all(math.isfinite(w) for w in weights.values())
    state = result.shared_base_state["weight"].item()
    fixture = json.dumps({key: safe_number(value) for key, value in values.items()}, sort_keys=True)
    row = {
        "case": case, "path": path, "weighting": weighting, "quality_floor": floor,
        "configured_cap": cap, "scores": {k: safe_number(v) for k, v in scores.items()},
        "fixture_sha256": hashlib.sha256(fixture.encode()).hexdigest(),
        "fixed_local_states": {k: safe_number(v) for k, v in values.items()},
        "accepted": result.accepted_nodes, "rejected": result.rejected_nodes,
        "weights": {k: safe_number(v) for k, v in weights.items()},
        "shared_scalar": safe_number(state), "all_weights_finite": finite,
        "weight_sum": safe_number(sum(weights.values())),
        "cap_feasible_after_policy": bool(weights) and cap * len(weights) >= 1.0,
        "cap_respected": finite and all(w <= cap + 1e-12 for w in weights.values()),
        "independent_scalar_oracle_matches": math.isclose(
            state, sum(values[k] * w for k, w in weights.items()), abs_tol=1e-12
        ) if finite and all(math.isfinite(v) for v in values.values()) else None,
    }
    if path == "validated":
        summary = coordinator.round_summaries[result.round_num]
        row["validation"] = {
            "min_admitted_nodes": quorum, "quorum_met_before_policy": summary.quorum_met,
            "admitted": summary.admitted_nodes, "rejected": summary.validation_rejected_nodes,
            "findings": {k: [str(finding.code) for finding in report.findings]
                         for k, report in summary.reports.items()},
        }
    return row


def experiment(root: Path) -> dict:
    import torch

    manifest, core, gate = setup(root)
    torch.set_num_threads(1)
    torch.manual_seed(0)
    torch.use_deterministic_algorithms(True)
    rows = []
    for path in ["core", "validated"]:
        for weighting, cap in [("quality", 1.0), ("quality", 0.5), ("equal", 0.5)]:
            for gamma in [1.0, 9.0, 1_000_000.0]:
                rows.append(measure(core, gate, f"{path}-{weighting}-cap{cap}-gamma{gamma:g}",
                                    {"alpha": 1.0, "beta": 1.0, "gamma": gamma},
                                    path=path, weighting=weighting, cap=cap))
        for weighting in ["quality", "equal"]:
            if path == "validated":
                continue
            rows.append(measure(core, gate, f"{path}-{weighting}-floor-shrink",
                                {"alpha": 0.1, "beta": 0.1, "gamma": 1.0},
                                path=path, weighting=weighting, cap=0.5, floor=0.5,
                                quorum=1))
        for gamma in [0.49, 0.5]:
            rows.append(measure(core, gate, f"{path}-floor-boundary-{gamma}",
                                {"alpha": 1.0, "beta": 1.0, "gamma": gamma},
                                path=path, floor=0.5))
    rows.append(measure(core, gate, "validated-quorum-blocks", {"alpha": 1.0, "beta": 1.0},
                        path="validated", cap=0.5, quorum=3))
    rows.append(measure(core, gate, "validated-tensor-nan-rejected",
                        {"alpha": 1.0, "beta": 1.0, "gamma": 1.0}, path="validated", cap=0.5,
                        values={"alpha": 0.0, "beta": 2.0, "gamma": float("nan")}))
    return {
        "schema_version": 1, "source_commit": manifest["commit"],
        "sources_manifest_sha256": hashlib.sha256((HERE / "sources.json").read_bytes()).hexdigest(),
        "runner_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "environment": {"python": platform.python_version(), "torch": torch.__version__,
                        "platform": platform.system(), "machine": platform.machine(),
                        "device": "cpu", "dtype": "float64", "seed": 0, "threads": 1},
        "scope": "Unmodified coordinator and merge; fixed one-parameter nodes; no local training or network",
        "cases": rows,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", required=True, type=Path)
    parser.add_argument("--output", type=Path, default=HERE / "results.json")
    args = parser.parse_args()
    result = experiment(args.source_root.resolve())
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True, allow_nan=False) + "\n")
    print(f"Recorded {len(result['cases'])} cases in {args.output}")


if __name__ == "__main__":
    main()
