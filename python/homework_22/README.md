# Homework 22. Pytest. Module 3

## Setup

```bash
cd python/homework_22
python3 -m venv venv
./venv/bin/pip install -r requirements.txt
```

## Run

```bash
./venv/bin/pytest
```

All options come from `pytest.ini`, so no extra flags are needed. The tests
can also be started from another folder, e.g. `pytest python/homework_22`:
the artefacts are always written to `homework_22/artefacts/`.

Run only one group of tests with a marker:

```bash
./venv/bin/pytest -m config
./venv/bin/pytest -m "data_processing and not negative"
```

## Artefacts

| File | Content |
|------|---------|
| `artefacts/pytest.log.txt` | Logs of the whole session |
| `artefacts/<test_name>/pytest.log.txt` | Logs of one test |
| `artefacts/report.html` | pytest-html report |
| `artefacts/console_output.txt` | Console output of the run |

The artefacts are overwritten on every run.
