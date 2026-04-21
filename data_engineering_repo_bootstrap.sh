#!/usr/bin/env bash

# Bootstrap a new Data Engineering repo using UV (modern Python tooling)
# Usage: ./bootstrap.sh my_project

set -e

PROJECT_NAME=$1

if [ -z "$PROJECT_NAME" ]; then
  echo "Usage: ./bootstrap.sh <project_name>"
  exit 1
fi

mkdir -p $PROJECT_NAME && cd $PROJECT_NAME

# -----------------------------
# Basic structure
# -----------------------------
mkdir -p src tests data notebooks scripts .vscode logs

# -----------------------------
# Initialize UV project
# -----------------------------
uv init --name "$PROJECT_NAME"

# -----------------------------
# Add dependencies
# -----------------------------
uv add pandas requests python-dotenv
uv add --dev pytest black flake8

# -----------------------------
# Create virtual environment
# -----------------------------
uv venv

# -----------------------------
# .gitignore
# -----------------------------
cat > .gitignore <<EOF
.venv/
__pycache__/
*.pyc
.env
.vscode/
.DS_Store
logs/
data/
EOF

# -----------------------------
# README
# -----------------------------
cat > README.md <<EOF
# $PROJECT_NAME

## Setup (uv)

\`\`\`bash
uv venv
source .venv/bin/activate
uv sync
\`\`\`

## Run

\`\`\`bash
uv run python src/main.py
\`\`\`

## Test

\`\`\`bash
uv run pytest
\`\`\`

## Alternative (pip)

\`\`\`bash
uv export --format requirements-txt > requirements.txt
pip install -r requirements.txt
\`\`\`
EOF

# -----------------------------
# Makefile
# -----------------------------
cat > Makefile <<EOF
.PHONY: install run test

install:
	uv sync

run:
	uv run python src/main.py

test:
	uv run pytest
EOF

# -----------------------------
# VSCode settings
# -----------------------------
cat > .vscode/settings.json <<EOF
{
  "python.defaultInterpreterPath": "./.venv/bin/python",
  "python.testing.pytestEnabled": true
}
EOF

# -----------------------------
# Claude.md
# -----------------------------
cat > Claude.md <<EOF
# Project Context

This is a data engineering project using UV.

## Commands
- uv sync
- uv run pytest
- uv run python src/main.py
EOF

# -----------------------------
# Sample main.py
# -----------------------------
cat > src/main.py <<EOF

def main():
    print("Hello from your UV-powered template!")

if __name__ == "__main__":
    main()
EOF

# -----------------------------
# Sample test
# -----------------------------
cat > tests/test_main.py <<EOF
from src.main import main

def test_main():
    assert main() is None
EOF

# -----------------------------
# Initialize git
# -----------------------------
git init

echo "✅ UV-native repo $PROJECT_NAME bootstrapped successfully!"
