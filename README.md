# ETL Pipeline with Apache Airflow and SQLite

## 📌 Overview
This project showcases an ETL (Extract, Transform, Load) pipeline using Apache Airflow. The pipeline reads sales data from a SQLite database, performs basic transformations using pandas, and writes the processed data back into the database. It is designed for simplicity, local development, and educational purposes.

---

## ✨ Features
- 🔁 Scheduled ETL workflow using Apache Airflow
- 🧠 Data transformation logic using pandas
- 🗃️ SQLite integration for lightweight storage
- 🧩 Modular design with extract, transform, and load tasks

---

## ⚙️ Prerequisites
- Windows 10/11 with WSL enabled
- Ubuntu installed via WSL
- Basic knowledge of Python and terminal commands
- Git (optional, for cloning this repository)

---

## 📦 Requirements
- Python 3.8+
- Apache Airflow 2.8.1
- pandas
- sqlite3 (included with Python)

---

## 🚀 Setup Instructions

### 1️⃣ Install WSL and Ubuntu
```bash
wsl --install
```

### 2️⃣ Install Python, SQLite, and Virtualenv
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip sqlite3 -y
pip3 install virtualenv
```

### 3️⃣ Set Up Virtual Environment
```bash
mkdir ~/airflow_etl_project && cd ~/airflow_etl_project
python3 -m venv airflow_venv
source airflow_venv/bin/activate
```

### 4️⃣ Install Apache Airflow
```bash
pip install apache-airflow==2.8.1 --constraint \
  "https://raw.githubusercontent.com/apache/airflow/constraints-2.8.1/constraints-3.8.txt"
```

### 5️⃣ Initialize Airflow
```bash
export AIRFLOW_HOME=~/airflow
airflow standalone
```
This command sets up the Airflow environment and launches the web server and scheduler.

### 6️⃣ Configure the DAG
```bash
mkdir -p ~/airflow/dags
nano ~/airflow/dags/etl_pipeline.py
```
Paste the DAG content from your `etl_pipeline.py` file and save.

### 7️⃣ Create SQLite Connection in Airflow
1. Navigate to [http://localhost:8080](http://localhost:8080)
2. Login with the credentials from `airflow standalone`
3. Go to **Admin > Connections > + Add**
   - **Conn Id**: `sqlite_connect`
   - **Conn Type**: `SQLite`
   - **Host**: `/home/<youruser>/airflow/sqlite_dbs/sales.db`

### 8️⃣ Run the DAG
- Enable and trigger `etl_pipeline` in the Airflow UI.
- Output CSV: `/tmp/sales_transformed.csv`
- Updated DB table: `sales_transformed`

---

## 🗂️ Access SQLite DB from Windows
Use the following path to open the SQLite file from Windows:
```
\\wsl.localhost\Ubuntu\home\<youruser>\airflow\sqlite_dbs\sales.db
```

---

## 🔧 DAG Tasks Breakdown
- **Extract**: Read data from the `sales` table and export it to CSV
- **Transform**: Calculate `total_sale = quantity * price` using pandas
- **Load**: Write transformed data back into the `sales_transformed` table

---

## 📄 requirements.txt
```txt
apache-airflow==2.8.1
pandas==2.2.1
```

