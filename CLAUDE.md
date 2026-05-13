# Project Context

## Project Overview

MLOps project for monitoring ML model drift and upstream data drift using Python, DuckDB, Airflow, and Docker.
Key Technologies

- Framework: Python with Airflow for orchestration
- Database: DuckDB for data processing and drift analysis
- Containerization: Docker & Docker Compose
- ML Monitoring: Model drift detection, data drift detection
- Github Workflows: For CI/CD 

## Key info:
- This is a project of learning where I am learning how to set-up MLOps workflows.

## Project Structure

mlops/
├── src/
│   └── utils/
│       ├── check_for_daily_drift.py      # Drift detection logic
│       ├── generate_inference.py         # Model inference pipeline
│       └── train.py                      # Model training
├── dags/                                  # Airflow DAGs
├── data/                                  # Local data storage
├── artifacts/                             # Model checkpoints
├── tests/                                 # Unit tests
├── docker-compose.yml                     # Docker services
├── Dockerfile                             # Container image
├── Makefile                               # Development commands
└── pyproject.toml                         # Dependencies

## Core Responsibilities

- Data Drift Detection: check_for_daily_drift.py monitors upstream data quality
- Model Inference: generate_inference.py generates predictions for monitoring
- Model Training: train.py handles model lifecycle
- Orchestration: Airflow DAGs coordinate daily workflows
- Containerization: Docker ensures reproducibility across environments


## Development Guidelines

- Use DuckDB for all data operations (lightweight, SQL-based)
- Write drift detection logic as reusable utilities in src/utils/
- Structure Airflow DAGs to run daily drift checks before inference
- Include unit tests in tests/ for all monitoring logic
- Use Docker Compose for local development matching production

## Git Hooks

A pre-push hook runs lint and tests before any push, mirroring GitHub CI.

Install after cloning:
```
make install-hooks
```

To bypass in an emergency: `git push --no-verify` (use sparingly).

## When to Use Claude Code

- Generating or refactoring drift detection logic
- Building Airflow DAG definitions
- Creating DuckDB schema migrations
- Writing monitoring and alerting utilities
- Debugging data pipeline issues

### Skills
- TBD 
