# Building Data Pipeline with Python & PySpark - Pacmann Week 8

## Overview

This project implements an end-to-end Data Pipeline using Python, PostgreSQL, REST API, Google Spreadsheet, Machine Learning, and MinIO Object Storage.

The pipeline extracts data from multiple sources, loads it into a staging area, performs data transformation, stores the result in a data warehouse, trains a machine learning model, and uploads the trained model to MinIO.

---

## Project Architecture

```text
+------------------+
|  Source Database |
|   PostgreSQL     |
+---------+--------+
          |
          |
          v
+------------------+
|     Extract      |
+------------------+
          |
          |
          +------------------+
          |                  |
          v                  v
+----------------+   +----------------+
| Google Sheet   |   |    REST API    |
| Car Brand Data |   | US States Data |
+----------------+   +----------------+
          |
          |
          v
+------------------+
|    Staging DB    |
|   PostgreSQL     |
+------------------+
          |
          |
          v
+------------------+
|   Transformation |
+------------------+
          |
          |
          v
+------------------+
|  Warehouse DB    |
|   PostgreSQL     |
+------------------+
          |
          |
          v
+------------------+
|  Preprocessing   |
+------------------+
          |
          |
          v
+------------------+
| Machine Learning |
+------------------+
          |
          |
          v
+------------------+
|      MinIO       |
| Object Storage   |
+------------------+
```

---

## Technology Stack

### Data Storage

* PostgreSQL 16
* MinIO Object Storage

### Data Processing

* Python 3.x
* Pandas
* SQLAlchemy
* Requests
* Psycopg2

### Data Sources

* PostgreSQL Database
* Google Spreadsheet
* REST API

### Machine Learning

* Scikit-Learn
* DecisionTreeRegressor
* Joblib

### Containerization

* Docker
* Docker Compose

---

## Data Sources

### 1. Source Database

Dataset: Car Sales Dataset

Records:

```text
30000 rows
17 columns
```

Stored in:

```text
source_db
```

---

### 2. Google Spreadsheet

Dataset:

```text
Car Brand Mapping
```

Records:

```text
51 rows
```

Purpose:

```text
Mapping brand_car -> brand_car_id
```

---

### 3. REST API

Source:

```text
US States Dataset
```

Records:

```text
68 rows
```

Purpose:

```text
Mapping state -> id_state
```

---

## Database Architecture

### Source Database

Tables:

```text
car_sales
```

---

### Staging Database

Tables:

```text
car_sales
car_brand
us_state
```

---

### Warehouse Database

Tables:

```text
car_sales
```

Transformation:

```text
brand_car  -> brand_car_id
state      -> id_state
```

---

## Data Exploration (EDA)

### Dataset Shape

```text
Rows    : 30000
Columns : 17
```

### Missing Values

```text
condition : 659
odometer  : 7
mmr       : 2
```

### Data Quality Findings

During transformation process:

```text
Missing brand mapping : 526
Missing state mapping : 2
```

Cause:

* Empty brand values in source dataset
* Invalid state codes not found in reference table

---

## ETL Pipeline

### Extract

Data extracted from:

* PostgreSQL Source Database
* Google Spreadsheet
* REST API

### Load Staging

Loaded into:

```text
staging_db
```

Tables:

```text
car_sales
car_brand
us_state
```

### Transform

Performed:

* Brand mapping
* State mapping
* Data cleansing
* Data quality validation

### Load Warehouse

Loaded into:

```text
warehouse_db
```

Final records:

```text
30000 rows
```

---

## Machine Learning

### Objective

Predict:

```text
sellingprice
```

### Features

```text
year
brand_car_id
id_state
condition
odometer
mmr
```

### Model

```text
DecisionTreeRegressor
```

### Train Test Split

```text
Train : 24000
Test  : 6000
```

### Evaluation

Mean Absolute Error (MAE)

```text
1431.839
```

---

## Object Storage

### MinIO

Bucket:

```text
models
```

Stored Object:

```text
car_price_model.pkl
```

Purpose:

```text
Store trained machine learning model
```

---

## Project Structure

```text
.
├── data_pipeline_exercise_4
│   ├── docker-compose.yml
│   ├── source_data
│   ├── staging_data
│   ├── warehouse_data
│   └── log_data
│
├── notebook
│   └── data_exploration.ipynb
│
├── pipeline
│   ├── extract
│   ├── helper
│   ├── load
│   ├── modeling
│   ├── preprocessing
│   ├── transform
│   └── main.py
│
├── SS
│   └── screenshots
│
└── README.md
```

---

## How To Run

### Start Infrastructure

```bash
docker compose up -d
```

### Activate Virtual Environment

```bash
cd pipeline

python -m venv venv

venv\Scripts\activate
```

### Install Dependencies

```bash
pip install pandas
pip install sqlalchemy
pip install psycopg2-binary
pip install requests
pip install gspread
pip install oauth2client
pip install scikit-learn
pip install minio
pip install joblib
```

### Run Pipeline

```bash
python main.py
```

---

## Screenshots

### Docker Services

Located in:

```text
SS/
```

### Data Exploration

Located in:

```text
SS/
```

### Machine Learning Result

Located in:

```text
SS/
```

### MinIO Storage

Located in:

```text
SS/
```

---

## GitHub Repository

Repository:

```text
https://github.com/pertapa3005/pacmann-week8-data-pipeline
```

---

## Author

Yogga Pratama

Pacmann AI Mentoring Program

Building Data Pipeline with Python & PySpark
