install:
	uv sync

run:
	uv run python src/main.py

test:
	uv run pytest

spark:
	uv run python src/pipelines/spark_job.py

sql:
	uv run python src/pipelines/sql_runner.py

lint:
	uv run black . && uv run flake8 .
