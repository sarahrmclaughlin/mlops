# Code Review Skill: Linting and Code Quality

## Overview
This skill automatically fixes linting errors and ensures code passes pre-commit checks.

## Quick Fix Process

### Run Auto-Formatters
These tools automatically fix many linting issues:
```bash
make lint           # Runs black and flake8 (black fixes style)
uv run black .      # Auto-format whitespace
uv run isort .      # Auto-fix import ordering
uv run pre-commit run --all-files  # Run all pre-commit hooks
```

### Manually Fix Remaining Errors
Some errors (like E501 line too long) require manual fixes:
1. Break long lines across multiple lines
2. Use implicit line continuation in parentheses/brackets
3. Reword verbose strings
4. Break dict/function definitions

### Run Full Validation
```bash
make install-hooks && bash scripts/hooks/pre-push
git add .
git commit -m "fix linting errors"
git push
```

## Applied Process

### Auto-Fix Tools Run First
- **black**: Auto-formats code style ✓
- **isort**: Auto-fixes import ordering ✓
- **flake8**: Reports errors (no auto-fix)

### Manual Fixes Required
For **E501 (line too long)** errors that black can't fix:
- Break dict definitions across lines
- Break function calls across lines  
- Shorten variable/function names if reasonable
- Move conditions to separate variables

## Example: Breaking Long Lines

### Before (86 chars):
```python
"feature_1": {"mean": float(np.mean(feature_1)), "std": float(np.std(feature_1))},
```

### After (broken across lines):
```python
"feature_1": {
    "mean": float(np.mean(feature_1)),
    "std": float(np.std(feature_1)),
},
```
