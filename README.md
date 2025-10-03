# E-commerce Analytics Project

## Project Overview
This project demonstrates a **complete data pipeline for an e-commerce dataset**, from raw data ingestion to ETL, data cleaning, analysis, and visualization. The goal is to create **curated datasets** and **interactive dashboards** that can be used for business insights, such as sales trends, top products, and customer behavior analysis.

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

