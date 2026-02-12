import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/European_Bank.csv")

st.title("Customer Retention Analytics Dashboard")

# =====================
# Sidebar Filters
# =====================

st.sidebar.header("Filters")

min_balance = st.sidebar.slider("Minimum Balance", 0, int(df['Balance'].max()), 0)

filtered_df = df[df['Balance'] >= min_balance]

# =====================
# Engagement vs Churn
# =====================

st.subheader("Engagement vs Churn")

engagement_churn = filtered_df.groupby('IsActiveMember')['Exited'].mean()

fig, ax = plt.subplots()
sns.barplot(x=engagement_churn.index, y=engagement_churn.values, ax=ax)
st.pyplot(fig)

# =====================
# Product Utilization
# =====================

st.subheader("Product Utilization Impact")

product_churn = filtered_df.groupby('NumOfProducts')['Exited'].mean()

fig2, ax2 = plt.subplots()
sns.barplot(x=product_churn.index, y=product_churn.values, ax=ax2)
st.pyplot(fig2)

# =====================
# High Balance Risk
# =====================

st.subheader("High Balance Disengaged Customers")

high_risk = filtered_df[
    (filtered_df['Balance'] > 100000) &
    (filtered_df['IsActiveMember'] == 0)
]

st.write("High Risk Customers Count:", len(high_risk))

# =====================
# KPI Score Cards
# =====================

st.subheader("Key Performance Indicators")

total_customers = len(df)
churn_rate = df['Exited'].mean()
active_rate = df['IsActiveMember'].mean()
avg_balance = df['Balance'].mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Customers", total_customers)
col2.metric("Churn Rate", f"{churn_rate:.2%}")
col3.metric("Active Members", f"{active_rate:.2%}")
col4.metric("Average Balance", f"${avg_balance:,.0f}")

# =====================
# Engagement Profile Distribution
# =====================

st.subheader("Engagement Profile Distribution")

df['EngagementProfile'] = df.apply(
    lambda x: "Active Engaged" if x['IsActiveMember'] == 1 and x['NumOfProducts'] >= 2
    else "Active Low Product" if x['IsActiveMember'] == 1
    else "Inactive High Balance" if x['Balance'] > 100000
    else "Inactive Disengaged",
    axis=1
)

profile_counts = df['EngagementProfile'].value_counts()

fig3, ax3 = plt.subplots()
profile_counts.plot(kind='bar', ax=ax3)
st.pyplot(fig3)

# =====================
# Geography Churn Analysis
# =====================

st.subheader("Churn by Geography")

geo_churn = df.groupby('Geography')['Exited'].mean()

fig4, ax4 = plt.subplots()
sns.barplot(x=geo_churn.index, y=geo_churn.values, ax=ax4)
st.pyplot(fig4)

# =====================
# Age Distribution of Churned Customers
# =====================

st.subheader("Age Distribution of Churn Customers")

fig5, ax5 = plt.subplots()
sns.histplot(df[df['Exited'] == 1]['Age'], bins=20, ax=ax5)
st.pyplot(fig5)

