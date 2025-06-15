from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys


sys.path.append('/opt/airflow/data_project/scripts')


from scripts.generate_data import generate_patient_data, generate_doctor_data


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2023, 10, 1),
    "retries": 1,
    
}

with DAG(
    dag_id="hospital_data_generation",
    description="Orchestrator for Hospital Data Generation",
    tags=["hospital", "data_generation"],
    schedule_interval=timedelta(minutes=5),
    catchup=False,
    default_args=default_args,
) as dag:

    generate_patient_data_task = PythonOperator(
        task_id="generate_patient_data",
        python_callable=generate_patient_data,
        op_kwargs={"num_records": 400},
    )

    generate_doctor_data_task = PythonOperator(
        task_id="generate_doctor_data",
        python_callable=generate_doctor_data,
        op_kwargs={"num_records": 100},
    
    )

    generate_patient_data_task >> generate_doctor_data_task
