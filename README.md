# E-commerce Analytics Project

[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/)
[![PySpark](https://img.shields.io/badge/PySpark-3.4-orange)](https://spark.apache.org/)
[![Power BI](https://img.shields.io/badge/PowerBI-Desktop-green)](https://powerbi.microsoft.com/)

## Project Overview
This project demonstrates a **complete data pipeline for an e-commerce dataset**, from raw data ingestion to ETL, data cleaning, analysis, and visualization. The goal is to create **curated datasets** and **interactive dashboards** that provide business insights, such as sales trends, top products, and customer behavior.

---

## Features
- **ETL pipeline:** Merge orders, customers, and products datasets.
- **Data cleaning and enrichment:** Handle missing values, type conversions, and compute derived metrics (e.g., revenue).
- **Analysis using Spark SQL and PySpark:** Monthly revenue trends, unique customers, product performance.
- **Visualization:** Interactive Power BI dashboards for business insights.

---

## Dataset
The project uses three main datasets:

1. **Orders**
   - `order_id`, `customer_id`, `product_id`, `order_date`, `quantity`, `price`, `channel`, `order_status`, `revenue`
2. **Customers**
   - `customer_id`, `name`, `signup_date`, `city`, `state`, `age_group`
3. **Products**
   - `product_id`, `product_name`, `category`, `cost_price`, `list_price`

> The **curated dataset** after ETL: `sales_curated.csv`

---

## Tech Stack
- **Databricks (Community Edition)**: PySpark notebooks
- **Python Libraries:** Pandas, NumPy, Matplotlib, Seaborn
- **SQL:** Spark SQL for data analysis
- **Power BI Desktop:** Interactive dashboards

---

## Folder Structure

ecommerce-project/
├── notebook/
│ └── ecommerce_notebook.py # Databricks notebook (PySpark ETL)
├── powerbi/
│ └── ecommerce_report.pbix # Power BI dashboard
├── data/
│ └── sales_curated.csv # Curated dataset after ETL
└── README.md # Project overview


---

## How to Run

### 1️⃣ Databricks Notebook
- Open `notebook/ecommerce_notebook.py` in **Databricks Community Edition** or locally with PySpark.
- Follow the steps to load raw CSVs, clean data, and generate `sales_curated.csv`.

### 2️⃣ Power BI Dashboard
- Open `powerbi/ecommerce_report.pbix` in **Power BI Desktop**.
- Connect to `sales_curated.csv` in the `data/` folder.
- Explore interactive charts:
  - Monthly revenue trends
  - Top products by revenue
  - Customer distribution by city, state, age group
  - Channel-wise sales performance

---

## Key Insights (Sample)
- Monthly revenue trends for completed orders.
- Top-performing products by revenue.
- Customer distribution by city, state, and age group.
- Channel-wise sales performance.

---

## Try it Yourself
1. Clone the repo.
2. Open the notebook in Databricks or Jupyter (local PySpark).
3. Run the ETL steps to generate sales_curated.csv.
4. Open the .pbix file in Power BI Desktop and connect it to the curated CSV.
5. Explore and customize dashboards with your own insights.


## Screenshots / Dashboard Preview

screenshots

## Author

Arshad MK
Data Analyst | PySpark | SQL | Python | Power BI
