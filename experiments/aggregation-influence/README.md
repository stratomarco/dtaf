# Aggregation influence experiment

This experiment measures how quality metadata changes a contribution's influence while its local model state stays fixed. It runs the upstream policy, coordinator and merge without modifying their source. It exercises both the core path and the optional validating coordinator.

The fixture replaces local training with deterministic nodes returning a single float64 parameter: alpha = 0, beta = 2, gamma = 10. The initial base is 0. Only scores change within each metadata sweep. These parameter values are diagnostic, not trained models or quality measurements.

## Reproduce

Use Python 3.14. The recorded run used Python 3.14.10 and CPU PyTorch 2.15.0+cpu. From this directory, with `uv` installed:

```sh
uv venv --python 3.14 .venv
uv pip install --python .venv/bin/python -r requirements-lock.txt --extra-index-url https://download.pytorch.org/whl/cpu --index-strategy unsafe-best-match
.venv/bin/python fetch_sources.py source-snapshot
.venv/bin/python run.py --source-root source-snapshot --output reproduced-results.json
SOURCE_ROOT="$PWD/source-snapshot" .venv/bin/python -m pytest -q test_experiment.py
```

`fetch_sources.py` downloads 36 pinned public files and verifies their SHA-256 digests. This is a partial source snapshot, not a full repository checkout. Existing files with different contents are never replaced. A full checkout of the pinned commit can also be passed to `--source-root`.

`run.py` verifies the source manifest before importing the code and checks the coordinator import locations. The checked-in [results](results.json) record source and runner digests, environment, fixture digests, inputs, weights, merged value and validation decisions. Non-finite tensor input is represented explicitly as a string in JSON. No network calls occur during measurement.

## Recorded observations

For both coordinator paths, with alpha and beta scores held at 1:

| Weighting | Cap | Gamma score | Gamma weight | Merged scalar |
|---|---|---|---|---|
| Quality | 1.0 | 1 | 1/3 | 4.0 |
| Quality | 1.0 | 9 | 9/11 | 8.363636 |
| Quality | 0.5 | 9 | 0.5 | 5.5 |
| Quality | 0.5 | 1,000,000 | 0.5 | 5.5 |
| Equal | 0.5 | 1 through 1,000,000 | 1/3 | 4.0 |

The 26 cases also cover the quality-floor boundary, the core policy's already documented infeasible-cap behavior, validation rejection of a non-finite tensor, and a quorum blocking a round. The low-participant core cases return full weight to the sole accepted node; a normalized cap cannot be satisfied when accepted count times cap is below one. These observations do not select the right governance policy.

## Validation and limits

Eight experiment tests check an independent scalar calculation, fixed-fixture identity, cap behavior, equal weighting, admission boundaries, validation/quorum behavior, deterministic repeatability and rejection of changed source files. Separately, 111 targeted upstream tests passed; see [validation record](validation.json).

The experiment executes actual coordinator calls with synthetic local nodes. It does not exercise local training, transport, identity enforcement, deployment, model quality, poisoning effectiveness or publication. It uses weighted-average merging only. The 50% cap is an experimental setting, not a recommended deployment value. No full repository `make before-pr` run is claimed.

Read the [source-backed review](../../reviews/update-admission/README.md) for architecture, assumptions and unresolved policy questions. Source code remains in its upstream repository under its existing licenses; it is not vendored here. New materials follow this repository's license.
