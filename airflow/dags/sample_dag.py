from datetime import datetime

from airflow.operators.python import PythonOperator

from airflow import DAG


def task():
    print("Airflow works")


with DAG(
    "example",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
) as dag:
    PythonOperator(task_id="run", python_callable=task)
