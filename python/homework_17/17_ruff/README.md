# Homework 17: Ruff

`messy.py` was cleaned with [ruff](https://docs.astral.sh/ruff/) using the
settings in `pyproject.toml` (line length 120, Python 3.11, double quotes,
rules `E, W, F, I, UP, B, C4, N, Q`).

## Original violations

`ruff check .` found 12 errors:

```
messy.py:1:1: E401 [*] Multiple imports on one line
messy.py:1:1: I001 [*] Import block is un-sorted or un-formatted
messy.py:1:8: F401 [*] `os` imported but unused
messy.py:1:12: F401 [*] `sys` imported but unused
messy.py:3:8: F401 [*] `json` imported but unused
messy.py:6:5: N802 Function name `Add` should be lowercase
messy.py:8:5: F841 Local variable `unused` is assigned to but never used
messy.py:9:5: F841 Local variable `msg` is assigned to but never used
messy.py:9:11: F541 [*] f-string without any placeholders
messy.py:14:13: E711 Comparison to `None` should be `cond is None`
messy.py:15:15: Q000 [*] Single quotes found but double quotes preferred
messy.py:20:19: W292 [*] No newline at end of file
```

`ruff format --check --diff .` reported `1 file would be reformatted`:
missing spaces in `def Add(a,b)` and `result=a+b`, extra spaces in
`print( Add(2 ,3) )`, single quotes in `'none!'` and no newline at the end
of the file.

## How each rule was fixed

| Rule | Problem | Fix | How |
|------|---------|-----|-----|
| E401 | `import os, sys` on one line | Split into separate imports, then removed as unused | `ruff check --fix` |
| I001 | Imports not sorted | Imports sorted (stdlib first, alphabetical) | `ruff check --fix` |
| F401 | `os`, `sys`, `json` imported but unused | Removed the unused imports | `ruff check --fix` |
| F541 | `f"done"` is an f-string with no placeholders | Removed the `f` prefix | `ruff check --fix` |
| Q000 | `'none!'` uses single quotes | Changed to `"none!"` | `ruff check --fix` |
| W292 | No newline at end of file | Added a trailing newline | `ruff check --fix` |
| N802 | Function name `Add` is not snake_case | Renamed to `add` and updated the call `add(2, 3)` | by hand |
| F841 | Unused local variables `unused` and `msg` | Deleted both assignments | by hand |
| E711 | `x == None` | Replaced with `x is None` | by hand |
| Formatting | Bad spacing around `=`, `,` and in `print( ... )` | Reformatted | `ruff format` |

Extra manual cleanup: `d = OrderedDict()` was never used, so the variable and
the `from collections import OrderedDict` import were removed as well. No rule
was silenced with `# noqa`.

## Result

```
$ ruff check .
All checks passed!

$ ruff format --check .
1 file already formatted
```

## Pre-commit

`.pre-commit-config.yaml` in the repository root runs the `ruff-check` and
`ruff-format` hooks for this folder on every `git commit`:

```
pip install pre-commit
pre-commit install
pre-commit run --all-files
```
