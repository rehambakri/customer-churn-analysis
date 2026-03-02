# 📊 Telecom Customer Churn Analysis  
### Orange Digital Center – Data Analysis with AI Final Project

---

## 🚀 Project Overview

This project analyzes customer churn behavior in a telecom company to identify high-risk customer segments and provide actionable business insights.

The main objective is to answer:

> Why are customers churning, and how can the company reduce churn rate?

The analysis was performed using **Python for data cleaning and exploration** and **Power BI for interactive dashboards and business storytelling**.

---

## 🛠️ Tools & Technologies

- Python (Pandas, Matplotlib, Seaborn)
- Power BI
- DAX (Data Analysis Expressions)
- Kaggle Dataset (IBM Telco Customer Churn)

---

## 📂 Dataset Description

The dataset includes customer-level information such as:

- Customer demographics (Gender, Senior Citizen, Dependents)
- Services subscribed (Internet, Streaming, Tech Support, etc.)
- Contract type
- Payment method
- Monthly Charges
- Total Charges
- Tenure (Customer Lifetime)
- Churn status (Yes / No)

---

## 🧹 Data Preparation (Python)

Key preprocessing steps:

- Converted `TotalCharges` from text to numeric and handled missing values
- Cleaned categorical columns
- Handled special values like:
  - "No internet service"
  - "No phone service"
- Created new analytical features:
  - Customer Lifetime Value (MonthlyCharges × Tenure)
  - Tenure Groups (0–1 year, 1–2 years, etc.)

Exploratory Data Analysis (EDA) was conducted to understand churn patterns before building dashboards.

---

## 📊 Power BI Dashboard Features

### 🔹 KPI Cards
- Total Customers
- Churned Customers
- Churn Rate %
- Average Monthly Charges
- Average Tenure

### 🔹 Visual Analysis
- Churn by Contract Type
- Churn by Internet Service
- Monthly Charges vs Churn
- Tenure Group vs Churn
- Payment Method Impact

### 🔹 Interactive Filters (Slicers)
- Contract Type
- Internet Service
- Payment Method
- Gender
- Senior Citizen

---

## 📈 Key Insights

- Customers with **Month-to-Month contracts** have the highest churn rate.
- Customers within their **first year** are more likely to churn.
- Higher monthly charges are associated with increased churn.
- Certain payment methods show higher churn behavior.

---

## 💡 Business Recommendations

- Offer loyalty discounts for month-to-month customers.
- Launch retention campaigns targeting new customers.
- Create bundled service offers for high-charge customers.
- Improve onboarding experience to increase early retention.

---

## 🖼️ Dashboard Screenshots

_Add your screenshots below by placing them inside a `screenshots` folder._

### Main Dashboard
![Main Dashboard](./dashboards-screenshots/Screenshot%202026-02-01%20132409.png)

### Churn Analysis Page
![Revenue&Customer Value](./dashboards-screenshots/Screenshot%202026-02-01%20132439.png)

![Churn Drivers Analysis](./dashboards-screenshots/Screenshot%202026-02-01%20132423.png)

![Customer Segment Details](./dashboards-screenshots/Screenshot%202026-02-01%20132501.png)




---
