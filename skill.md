# Code Review Skill: Linting and Code Quality

## Overview
This skill reviews code for linting errors and fixes them systematically.

## Process

### Step 1: Identify Linting Errors
Run the pre-push hook or `make lint` to identify all linting violations:
- **E501**: Line too long (>79 characters)
- **F401**: Imported but unused
- **Other flake8 violations**: Fix as needed

### Step 2: Fix Long Lines
For E501 errors (lines > 79 chars):
- Break dictionary/function definitions across multiple lines
- Use implicit line continuation in parentheses
- Reword verbose strings where possible
- Indent continuation lines for readability

### Step 3: Remove Unused Imports
For F401 errors:
- Remove unused `import X` statements
- Remove unused `from X import Y` statements
- Verify the import isn't needed elsewhere before deleting

### Step 4: Fix Other Style Issues
- Ensure consistent spacing and indentation
- Follow PEP 8 conventions
- Use isort for import ordering (runs via pre-commit)

### Step 5: Verify Fixes
```bash
make lint        # Run linting locally
make test        # Run tests
make install-hooks && bash scripts/hooks/pre-push  # Smoke-test hook
```

## Applied Fixes

### Issue 1: Unused Import in `src/generate_inference.py`
**Error**: F401 'datetime.datetime' imported but unused (line 6)
**Fix**: Remove the unused import line

### Issue 2: Long Lines in `src/check_for_daily_drift.py`
**Errors**:
- Line 1: Docstring (80 > 79 chars)
- Line 43: Dict assignment (85 > 79 chars)
- Line 75: Log message (84 > 79 chars)
- Line 79: Log message (80 > 79 chars)

**Fix**: Break lines using implicit continuation or reword strings

### Issue 3: Long Lines in `src/train.py`
**Errors**:
- Line 20: Dict value (86 > 79 chars)
- Line 21: Dict value (86 > 79 chars)

**Fix**: Break dict definitions across multiple lines
