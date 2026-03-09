🏦 Customer Engagement & Product Utilization Analytics for Retention Strategy
📌 Project Overview

Customer retention is one of the biggest challenges in the banking industry. This project analyzes customer engagement behavior and product utilization patterns to identify churn risk and design retention strategies using Data Analytics, Machine Learning, and Streamlit Dashboard Visualization.

The project focuses on understanding how customer activity, product adoption, and financial behavior influence long-term loyalty.

🎯 Objectives
Primary Objectives

Analyze relationship between engagement and churn

Evaluate product utilization impact on customer retention

Identify disengaged high-value customers

Secondary Objectives

Support engagement-driven retention strategies

Improve product bundling decisions

Detect silent churn among premium customers

📊 Dataset Description

The dataset contains European banking customer records including behavioral, demographic, and financial attributes.

Column	Description
CustomerId	Unique customer identifier
CreditScore	Customer credit score
Geography	Country (France, Spain, Germany)
Gender	Customer gender
Age	Customer age
Tenure	Years with bank
Balance	Account balance
NumOfProducts	Number of banking products
HasCrCard	Credit card ownership
IsActiveMember	Activity indicator
EstimatedSalary	Annual salary
Exited	Churn indicator
🛠 Tech Stack
Programming Language

Python

Libraries & Frameworks

Pandas

NumPy

Matplotlib

Seaborn

Scikit-Learn

Streamlit

Joblib




🔍 Exploratory Data Analysis (EDA)

The analysis includes:

Data cleaning and validation

Engagement classification

Product utilization analysis

Financial commitment evaluation

Sticky customer identification

Engagement Profiles Created

Active Engaged Customers

Active Low Product Customers

Inactive Disengaged Customers

Inactive High Balance Customers

📈 Key Performance Indicators (KPIs)
⭐ Engagement Retention Ratio

Measures churn difference between active and inactive customers.

⭐ Product Depth Index

Analyzes churn probability based on number of products used.

⭐ High Balance Disengagement Rate

Identifies premium customers with churn risk.

⭐ Credit Card Stickiness Score

Measures retention impact of credit card ownership.

⭐ Relationship Strength Index

Combined engagement and product loyalty metric.

🤖 Machine Learning Model

Two models were implemented:

1️⃣ Logistic Regression

Baseline churn prediction model.

2️⃣ Random Forest (Final Model)

Selected due to higher accuracy and better churn prediction.

Model Performance
Model	Accuracy
Logistic Regression	81.5%
Random Forest	86.8%
🌐 Streamlit Dashboard Features

The interactive dashboard provides:

Engagement vs Churn Visualization

Product Utilization Insights

High-Value Customer Risk Detection

KPI Monitoring Panels

Real-Time Churn Prediction Tool

🚀 How To Run Project
Step 1 — Clone Repository
git clone https://github.com/your-username/Customer_Retention_Project.git

Step 2 — Install Requirements
pip install -r requirements.txt

Step 3 — Run Analysis
python notebooks/analysis.py

Step 4 — Train Model
python models/churn_model.py

Step 5 — Run Dashboard
streamlit run streamlit_app/app.py

💡 Business Insights

Customer engagement strongly influences retention.

Multi-product customers demonstrate higher loyalty.

High-balance customers can still churn if engagement is low.

AI-based churn prediction enables proactive retention strategies.



Customer lifetime value prediction



👨‍💻 Author

Chetan Zope
AI & Machine Learning Enthusiast

📧 Email: chetanzope890@gmail.com


📜 License

This project is developed for educational and research purposes.
