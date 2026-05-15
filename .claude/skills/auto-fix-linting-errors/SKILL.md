# Skill: Auto-Fix Linting Errors

**Purpose**: When the pre-push hook fails with linting errors, Claude uses this skill to automatically fix them.

**Trigger**: Pre-push hook fails → Claude analyzes errors → applies fixes → user can immediately push

---

## How to Use This Skill

When you see pre-push hook failures, ask Claude:
> "Use the Auto-Fix Linting Errors skill to fix the failing checks"

Claude will:
1. Read the error output from the pre-push hook
2. Identify the specific files and line numbers with errors
3. Apply fixes automatically using the patterns below
4. Commit the fixes

---

## Error Patterns & Fixes

### E501: Line Too Long (>79 characters)

**Pattern**: Lines with strings, dicts, or function calls that exceed 79 chars

**Fix Strategy**:
1. Break dict/list definitions across multiple lines
2. Use implicit line continuation in parentheses
3. Move long strings to variables
4. Reword verbose messages

**Example**:
```python
# Before (85 chars)
results[col] = {"p_value": float(p_value), "drift_detected": int(p_value < 0.05)}

# After (fixed)
results[col] = {
    "p_value": float(p_value),
    "drift_detected": int(p_value < 0.05),
}
```

### F401: Imported But Unused

**Pattern**: `import X` or `from X import Y` that's never used

**Fix Strategy**:
1. Remove the unused import line
2. Verify the symbol isn't used elsewhere in the file

**Example**:
```python
# Before
from datetime import datetime  # F401

# After
# (line removed)
```

### isort: Import Ordering

**Pattern**: Imports not in standard order (stdlib, third-party, local)

**Fix Strategy**:
1. Run `uv run isort .` to auto-fix
2. Or manually reorder: stdlib first, then third-party, then local

---

## Automated Steps

When Claude encounters pre-push hook failures:

```bash
# 1. Read the error output
# 2. Identify affected files and error types
# 3. Edit files to fix errors using patterns above
# 4. Run verification
uv run pre-commit run --all-files

# 5. If verification passes, commit
git add .
git commit -m "fix linting errors"
git push
```

---

## Common Errors & Quick Fixes

| Error | File | Fix |
|-------|------|-----|
| E501 line too long | `src/train.py:20` | Break dict across lines |
| E501 line too long | `src/check_for_daily_drift.py:43` | Break dict across lines |
| F401 unused import | `src/generate_inference.py:6` | Remove import |
| isort import order | Any | Run `uv run isort .` |

---

## Example Workflow

```
Pre-push hook fails with:
  - src/train.py:20 E501 (86 > 79)
  - src/check_for_daily_drift.py:43 E501 (85 > 79)

Claude action:
  1. Read src/train.py, find line 20
  2. Break the long dict definition across lines
  3. Read src/check_for_daily_drift.py, find line 43
  4. Break the long dict definition across lines
  5. Run: uv run pre-commit run --all-files
  6. If passes: commit and push
```

---

## When to Use This Skill

✅ **Use when**:
- Pre-push hook reports linting errors
- You want Claude to auto-fix them immediately
- You don't want to manually edit files

❌ **Don't use when**:
- Tests are actually failing (not just missing)
- Logic errors need fixing
- You want to review changes first