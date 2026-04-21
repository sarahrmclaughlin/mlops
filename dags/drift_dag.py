from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    "drift_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False
) as dag:

    generate = BashOperator(
        task_id="generate_data",
        bash_command="python src/generate_inference.py"
    )

    drift = BashOperator(
        task_id="check_drift",
        bash_command="python src/drift.py"
    )

    generate >> drift