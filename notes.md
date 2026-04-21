## General Notes for DE
#### *This file can be deleted after cloning this template*

### uv
#### 🚀 What is uv
- Drop-in replacement for pip, pip-tools, virtualenv
- Much faster (Rust-based)
- Handles:
    - venv creation
    - dependency install
    - locking

#### First time set-up for uv
- ✅ Step 1 — Install uv
```bash 
curl -Ls https://astral.sh/uv/install.sh | sh
```
- Restart terminal, then check:
```bash 
uv --version
```
- ✅ Step 2 — Initialize your project
    - Inside your repo:
```bash 
uv init
```
    - This creates a clean pyproject.toml
- ✅ Step 3 — Add dependencies
    - Instead of editing manually:
```bash 
uv add pandas requests python-dotenv
```
    - For dev dependencies:
```bash 
uv add --dev pytest black flake8
``` 
- ✅ Step 4 — Create and use venv
```bash 
uv venv
source .venv/bin/activate
```
    - 👉 Note: uv uses .venv/ (better than venv/, more standard now)
- ✅ Step 5 — Install everything
    - Creates a lockfile (uv.lock)
    - Installs exact versions
```bash 
uv sync
```
- 📦 What your project now has
    - pyproject.toml   # dependencies (source of truth)
    - uv.lock          # exact versions (like requirements.txt but better)
    - .venv/           # environment

#### Run files using uv

```bash
uv run python src/main.py
```

### Run Test using uv

```bash
uv run pytest
```

#### Virtual Environment with uv

- Don't activate, just run 
```bash
uv run python src/main.py
uv run pytest
```

- Activate
```bash
source .venv/bin/activate
python src/main.py
pytest
```
#### Common uv commands
```bash
Task	            Command
List dependencies	uv pip list
Add package	        uv add <package>
Add dev package	    uv add --dev <package>
Remove package	    uv remove <package>
Remove dev package	uv remove --dev <package>
Sync env(post update)	uv sync 
Run script inside venv	uv run python src/main.py
```

#### uv with pre-commit or other packages
- First time set-up
    - add it to packages
    - install pre-commit
```bash
uv add pre-commit
uv run pre-commit install
```

#### Alternative to uv(pip)

```bash
uv export --format requirements-txt > requirements.txt
pip install -r requirements.txt
```

