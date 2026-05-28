# Travel & Hospitality: Customer Retention and Dynamic Pricing Analysis

## Executive Summary
This project addresses revenue leakage in the hospitality sector by analyzing historical booking data. The primary objective is to uncover the drivers of customer cancellations (churn) and provide the analytical foundation for dynamic pricing and targeted retention strategies.

## Business Objectives
* **Optimize Revenue Per Available Room (RevPAR):** Identifying periods of high demand elasticity to adjust pricing dynamically.
* **Reduce Cancellation Rates:** Understanding key drivers such as lead time, deposit types, and customer segments to mitigate churn.
* **Strategic Segmentation:** Providing actionable insights for the Marketing Director to design targeted retention campaigns.

## Dashboard Visualizations

### 1. Executive Overview
![Overview](Dashboad/views/overview.png)
*Provides high-level revenue aggregations and key performance indicators for the Revenue Manager.*

### 2. Predictive Analytics
![Predictive Analytics](Dashboad/views/predictive%20Analytics.png)
*Visualizes booking patterns and cancellation probabilities derived from the classification models.*

### 3. Prescriptive Actions
![Prescriptive Actions](Dashboad/views/prescripive%20Actions.png)
*Delivers actionable insights for marketing and operations teams to optimize promotional spend and inventory strategies.*

## Technical Stack
* **Data Processing & EDA:** Python (Pandas, NumPy).
* **Statistical Visualization:** Matplotlib, Seaborn.
* **Predictive Analytics:** Scikit-Learn (Logistic Regression, Decision Trees).
* **Dashboarding:** Power BI / Tableau.

## Project Roadmap
* **Week 1: Data Acquisition & Cleaning:** Handled missing values, treated outliers, and engineered key features.
* **Week 2: Exploratory Data Analysis (EDA):** Performed univariate and bivariate analysis to identify cancellation drivers.
* **Week 3: Predictive Modeling:** Built and evaluated classification models to predict churn.
* **Week 4: Reporting & Dashboarding:** Finalized interactive dashboards and documentation.

## Repository Structure
* `/data`: (Note: Raw datasets are excluded via `.gitignore` for security).
* `/notebooks`: Contains step-by-step Jupyter Notebooks for cleaning, EDA, and modeling.
* `/Dashboad/views`: Contains high-resolution screenshots of the final dashboard.

---
*Note: This project adheres to strict version control practices, with consistent commits across all 4 weeks of development.*
