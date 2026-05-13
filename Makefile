install:
	uv sync

run:
	uv run python src/main.py

# test:
# 	uv run pytest || [ $$? -eq 5 ]

spark:
	uv run python src/pipelines/spark_job.py

sql:
	uv run python src/pipelines/sql_runner.py

lint:
	uv run black . && uv run flake8 .

install-hooks:
	cp scripts/hooks/pre-push .git/hooks/pre-push
	chmod +x .git/hooks/pre-push
	@echo "Pre-push hook installed."
