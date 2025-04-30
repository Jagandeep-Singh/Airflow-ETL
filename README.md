# ETL Pipeline with Apache Airflow and SQLite

## Overview
This project demonstrates how to build an ETL (Extract, Transform, Load) pipeline using Apache Airflow. The pipeline reads sales data from a SQLite database, applies a transformation to calculate total sales, and writes the transformed data back to the database.

---

## Features
- 🔄 Automated daily ETL pipeline using Airflow DAG
- 🧮 Transformation logic using pandas
- 🗃️ Lightweight SQLite database for quick prototyping
- 💡 Modular design with extract, transform, and load tasks

---

## Requirements
- WSL with Ubuntu (if using Windows)
- Python 3.8+
- Apache Airflow 2.8.1
- pandas
- sqlite3

---

## Setup Instructions

### 1. Install WSL and Ubuntu
```bash
wsl --install
```

### 2. Install Python and Virtualenv
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip sqlite3 -y
pip3 install virtualenv
```

### 3. Create and Activate Virtual Environment
```bash
mkdir ~/airflow_etl_project && cd ~/airflow_etl_project
python3 -m venv airflow_venv
source airflow_venv/bin/activate
```

### 4. Install Apache Airflow
```bash
pip install apache-airflow==2.8.1 --constraint \
  "https://raw.githubusercontent.com/apache/airflow/constraints-2.8.1/constraints-3.8.txt"
```

### 5. Initialize Airflow
```bash
export AIRFLOW_HOME=~/airflow
airflow standalone
```

### 6. Configure DAG
```bash
mkdir -p ~/airflow/dags
nano ~/airflow/dags/etl_pipeline.py
```
Paste the DAG content (from `Working ETL DAG file.txt`) and save.

### 7. Setup SQLite Connection in Airflow
1. Go to http://localhost:8080
2. Login using the credentials shown after running `airflow standalone`
3. Navigate to Admin > Connections > + Add
   - Conn Id: `sqlite_connect`
   - Conn Type: `SQLite`
   - Host: `/home/<youruser>/airflow/sqlite_dbs/sales.db`

### 8. Trigger DAG
- Enable and trigger `etl_pipeline` from the UI.
- View output: `/tmp/sales_transformed.csv`
- View updated DB table: `sales_transformed` inside your SQLite DB.

---

## Access SQLite DB from Windows
Use this path to open in DB browser:
```
\\wsl.localhost\Ubuntu\home\<youruser>\airflow\sqlite_dbs\sales.db
```

---

## DAG Tasks
- **Extract**: Query `sales` table from SQLite, export to CSV.
- **Transform**: Calculate `total_sale = quantity * price` using pandas.
- **Load**: Save the transformed data back to SQLite.

---

## requirements.txt
```txt
apache-airflow==2.8.1
pandas
```

---

## Future Improvements
- Add unit tests for each task
- Integrate anomaly detection
- Switch to PostgreSQL or cloud DB
- Visualize output in a dashboard

---

## Author
Created by Jagandeep Singh

