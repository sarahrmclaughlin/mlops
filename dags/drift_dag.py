from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import subprocess
import logging

default_args = {
    "owner": "sarah",
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

def run_script(script_name, date_str):
    logging.info(f"Running {script_name} with date {date_str}")
    result = subprocess.run(
        ["python", f"/opt/airflow/src/{script_name}", date_str],
        capture_output=True,
        text=True
    )
    logging.info(f"STDOUT: {result.stdout}")
    logging.info(f"STDERR: {result.stderr}")

    result.check_returncode()

with DAG(
    dag_id="drift_pipeline",
    default_args=default_args,
    schedule="@daily",
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:

    generate = PythonOperator(
        task_id="generate_data",
        python_callable=run_script,
        op_args=["generate_inference.py", "{{ ds }}"],
    )

    drift = PythonOperator(
        task_id="check_drift",
        python_callable=run_script,
        op_args=["check_for_daily_drift.py", "{{ ds }}"],
    )

    generate >> drift