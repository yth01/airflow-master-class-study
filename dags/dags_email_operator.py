from airflow import DAG
import pendulum
import datetime
from airflow.operators.email import EmailOperator

with DAG(
        dag_id="dag_email_operator",
        schedule="0 8 1 * *",
        start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
        catchup=False
) as dag:
    send_email = EmailOperator(
        task_id="send_email",
        to="yth011026@naver.com",
        subject="Airflow 성공 메일",
        html_content="<h3> Airflow 성공 메일입니다. </h3>"
    )
