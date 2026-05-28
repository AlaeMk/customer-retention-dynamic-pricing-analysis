# 🏨 Customer Retention & Dynamic Pricing Analysis 🏨
**Developed by: Alae Benelmekki** *Data Scientist & BI Analyst | Business Intelligence Student*

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)](https://www.python.org/)
[![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow?logo=powerbi)](https://powerbi.microsoft.com/)
[![GitHub](https://img.shields.io/badge/GitHub-Repo-black?logo=github)](https://github.com/AlaeMk/customer-retention-dynamic-pricing-analysis)
[![Cmder](https://img.shields.io/badge/Workflow-Cmder-green?logo=windows)](https://cmder.app/)

> **Project Submission** – An end-to-end analytics solution optimizing hospitality revenue and customer retention.

---

## 📌 Project Overview
This project addresses revenue leakage in the hospitality sector. By analyzing historical booking datasets, I developed a pipeline to uncover churn drivers, visualize seasonal demand, and establish a foundation for dynamic pricing.

**Key business questions answered:**
- What are the primary drivers of customer cancellations (churn)?
- How does lead time correlate with booking volume?
- What are the seasonal demand trends and pricing elasticities?
- How can we optimize RevPAR (Revenue Per Available Room) through data-driven decisions?

---

## 📂 Repository Structure

```text
customer-retention-dynamic-pricing-analysis/
├── README.md                # Project overview & documentation
├── .gitignore               # Excludes raw data & environment files
├── notebooks/
│   └── 01_eda_and_churn.ipynb # EDA, Churn analysis & predictive baselines
├── sql/
│   └── analytics_queries.sql  # SQL aggregations for KPIs
├── dashboard/
│   └── hotel_dashboard.pbix   # Interactive Power BI Dashboard
└── src/
    └── main_pipeline.py       # Data processing pipeline
