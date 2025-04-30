from airflow import DAG
from airflow.decorators import task, dag
from airflow.models import Variable
from airflow.hooks.base import BaseHook
from datetime import datetime, timedelta
import pandas as pd
import sqlite3

@dag(
    dag_id='etl_pipeline',
    schedule='@daily',
    default_args={
        'owner': 'airflow',
        'start_date': datetime(2025, 4, 22),
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
    },
    catchup=False,
)
def etl_pipeline():
    @task()
    def extract():
        # Using Airflow hook to retrieve connection info
        conn_info = BaseHook.get_connection("sqlite_connect")
        conn = sqlite3.connect(conn_info.host)  # SQLite stores file path in host field
        df = pd.read_sql("SELECT * FROM sales;", conn)
        df.to_csv('/tmp/sales_data.csv', index=False)
        conn.close()

    @task()
    def transform():
        df = pd.read_csv('/tmp/sales_data.csv')
        df['total_sale'] = df['quantity'] * df['price']
        df.to_csv('/tmp/sales_transformed.csv', index=False)

    @task()
    def load():
        # Use same DBAPI2 connection method for compatibility
        conn_info = BaseHook.get_connection("sqlite_connect")
        conn = sqlite3.connect(conn_info.host)
        df = pd.read_csv('/tmp/sales_transformed.csv')
        df.to_sql('sales_transformed', con=conn, if_exists='replace', index=False)
        conn.close()

    extract_task = extract()
    transform_task = transform()
    load_task = load()

    extract_task >> transform_task >> load_task

etl_pipeline()
