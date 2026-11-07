"""Independent checks of the experiment's fixture, oracle and provenance."""

from __future__ import annotations

import json
import os
import shutil
from pathlib import Path

import pytest

import run


@pytest.fixture(scope="module")
def measurement():
    root = Path(os.environ["SOURCE_ROOT"]).resolve()
    return root, run.experiment(root)


def rows(measurement):
    return {row["case"]: row for row in measurement[1]["cases"]}


def test_quality_sweep_matches_independent_scalar_calculation(measurement):
    data = rows(measurement)
    for path in ["core", "validated"]:
        baseline = data[f"{path}-quality-cap1.0-gamma1"]
        changed = data[f"{path}-quality-cap1.0-gamma9"]
        assert baseline["fixture_sha256"] == changed["fixture_sha256"]
        assert baseline["shared_scalar"] == pytest.approx(4.0)
        assert changed["weights"]["gamma"] == pytest.approx(9 / 11)
        assert changed["shared_scalar"] == pytest.approx((0 + 2 + 10 * 9) / 11)


def test_feasible_cap_limits_quality_influence(measurement):
    data = rows(measurement)
    for path in ["core", "validated"]:
        row = data[f"{path}-quality-cap0.5-gamma1e+06"]
        assert row["cap_feasible_after_policy"] and row["cap_respected"]
        assert row["weights"] == {"alpha": 0.25, "beta": 0.25, "gamma": 0.5}
        assert row["shared_scalar"] == pytest.approx(5.5)


def test_equal_weighting_is_insensitive_above_floor(measurement):
    data = rows(measurement)
    for path in ["core", "validated"]:
        baseline = data[f"{path}-equal-cap0.5-gamma1"]
        changed = data[f"{path}-equal-cap0.5-gamma1e+06"]
        assert changed["weights"] == baseline["weights"]
        assert changed["shared_scalar"] == baseline["shared_scalar"]


def test_floor_boundary_changes_membership(measurement):
    data = rows(measurement)
    for path in ["core", "validated"]:
        assert data[f"{path}-floor-boundary-0.49"]["accepted"] == ["alpha", "beta"]
        assert data[f"{path}-floor-boundary-0.5"]["accepted"] == ["alpha", "beta", "gamma"]


def test_validation_and_quorum_controls_are_observed(measurement):
    data = rows(measurement)
    blocked = data["validated-quorum-blocks"]
    assert blocked["weights"] == {}
    assert blocked["shared_scalar"] == 0.0
    assert blocked["validation"]["quorum_met_before_policy"] is False
    rejected = data["validated-tensor-nan-rejected"]
    assert rejected["validation"]["rejected"] == ["gamma"]
    assert rejected["validation"]["findings"]["gamma"]
    assert rejected["shared_scalar"] == 1.0


def test_finite_baseline_results_and_oracle(measurement):
    for row in measurement[1]["cases"]:
        assert row["all_weights_finite"]
        assert row["independent_scalar_oracle_matches"] in (True, None)
        if row["weights"]:
            assert row["weight_sum"] == pytest.approx(1.0, abs=1e-12)


def test_repeated_experiment_is_identical(measurement):
    assert run.experiment(measurement[0]) == measurement[1]


def test_modified_sources_are_rejected(measurement, tmp_path):
    manifest = json.loads((run.HERE / "sources.json").read_text())
    for entry in manifest["files"]:
        target = tmp_path / entry["path"]
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(measurement[0] / entry["path"], target)
    policy = next(entry["path"] for entry in manifest["files"] if entry["path"].endswith("/policy.py"))
    with (tmp_path / policy).open("a") as stream:
        stream.write("\n# changed\n")
    with pytest.raises(ValueError, match="Source mismatch"):
        run.verify_sources(tmp_path)
