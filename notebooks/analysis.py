import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("data/European_Bank.csv")

print("Dataset Loaded Successfully")
print(df.head())

# Dataset Info
print("\nDataset Info:")
print(df.info())

# Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Binary Column Check
print("\nBinary Column Check:")
print("HasCrCard:", df['HasCrCard'].unique())
print("IsActiveMember:", df['IsActiveMember'].unique())
print("Exited:", df['Exited'].unique())

# Remove unwanted columns
df.drop(['CustomerId', 'Surname'], axis=1, inplace=True)

print("\nColumns after removal:")
print(df.columns)

# Duplicate Check
print("\nDuplicate Rows:", df.duplicated().sum())

# Statistical Summary
print("\nStatistical Summary:")
print(df.describe())


# =============================
# Customer Engagement Classification
# =============================

def classify_customer(row):

    # Active and using multiple products
    if row['IsActiveMember'] == 1 and row['NumOfProducts'] >= 2:
        return "Active Engaged"

    # Inactive but high balance customers
    elif row['IsActiveMember'] == 0 and row['Balance'] > 100000:
        return "Inactive High Balance"

    # Active but only single product
    elif row['IsActiveMember'] == 1 and row['NumOfProducts'] == 1:
        return "Active Low Product"

    # Completely disengaged customers
    else:
        return "Inactive Disengaged"

df['EngagementProfile'] = df.apply(classify_customer, axis=1)

print("\nEngagement Profile Distribution:")
print(df['EngagementProfile'].value_counts())

plt.figure(figsize=(8,5))
sns.countplot(x='EngagementProfile', data=df)
plt.title("Customer Engagement Distribution")
plt.xticks(rotation=20)
plt.show()


# =============================
# Product Utilization Analysis
# =============================

product_churn = df.groupby('NumOfProducts')['Exited'].mean()

print("\nChurn Rate by Number of Products:")
print(product_churn)

plt.figure(figsize=(8,5))
sns.barplot(x=product_churn.index, y=product_churn.values)
plt.title("Churn Rate by Number of Products")
plt.xlabel("Number of Products")
plt.ylabel("Churn Rate")
plt.show()

df['ProductCategory'] = df['NumOfProducts'].apply(
    lambda x: "Single Product" if x == 1 else "Multi Product"
)

single_multi = df.groupby('ProductCategory')['Exited'].mean()

print("\nSingle vs Multi Product Churn:")
print(single_multi)

plt.figure(figsize=(6,4))
sns.barplot(x=single_multi.index, y=single_multi.values)
plt.title("Single vs Multi Product Churn")
plt.show()

print(df['NumOfProducts'].value_counts())

# =============================
# Financial Commitment vs Engagement
# =============================

plt.figure(figsize=(8,5))
sns.boxplot(x='IsActiveMember', y='Balance', data=df)
plt.title("Balance vs Activity")
plt.show()

df['SalaryBalanceRatio'] = df['Balance'] / (df['EstimatedSalary'] + 1)

print("\nSalary Balance Ratio Created")

premium_risk = df[
    (df['Balance'] > 120000) &
    (df['IsActiveMember'] == 0)
]

print("\nAt-Risk Premium Customers:", premium_risk.shape[0])

plt.figure(figsize=(6,4))
sns.countplot(x=premium_risk['Exited'])
plt.title("Premium Disengaged Customer Churn")
plt.show()

# =============================
# Retention Strength Assessment
# =============================

sticky_customers = df[
    (df['IsActiveMember'] == 1) &
    (df['NumOfProducts'] >= 2) &
    (df['Exited'] == 0)
]

print("\nSticky Customers Count:", sticky_customers.shape[0])

sticky_percentage = (sticky_customers.shape[0] / len(df)) * 100

print("Sticky Customer Percentage:", round(sticky_percentage,2), "%")

df['RelationshipScore'] = (
    df['IsActiveMember'] * 0.4 +
    (df['NumOfProducts'] / df['NumOfProducts'].max()) * 0.4 +
    df['HasCrCard'] * 0.2
)

print("\nAverage Relationship Strength:",
      round(df['RelationshipScore'].mean(),2))

plt.figure(figsize=(8,5))
sns.boxplot(x='Exited', y='RelationshipScore', data=df)
plt.title("Relationship Strength vs Churn")
plt.show()

active_churn = df[df['IsActiveMember'] == 1]['Exited'].mean()
inactive_churn = df[df['IsActiveMember'] == 0]['Exited'].mean()

engagement_retention_ratio = inactive_churn / active_churn

print("\nEngagement Retention Ratio:",
      round(engagement_retention_ratio,2))

product_depth_index = df.groupby('NumOfProducts')['Exited'].mean()

print("\nProduct Depth Index:")
print(product_depth_index)

high_balance_disengagement = df[
    (df['Balance'] > 100000) &
    (df['IsActiveMember'] == 0)
]['Exited'].mean()

print("\nHigh Balance Disengagement Rate:",
      round(high_balance_disengagement,2))

card_stickiness = df.groupby('HasCrCard')['Exited'].mean()

print("\nCredit Card Stickiness Score:")
print(card_stickiness)

plt.figure(figsize=(8,5))
sns.histplot(df['RelationshipScore'], bins=20, kde=True)
plt.title("Relationship Strength Distribution")
plt.show()

