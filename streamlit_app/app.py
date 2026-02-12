import streamlit as st
import pandas as pd
import numpy as np

import joblib
model = joblib.load("models/churn_prediction_model.pkl")
scaler = joblib.load("models/scaler.pkl")

st.title("Customer Retention Dashboard")
st.header("🔮 Churn Prediction Tool")

credit_score = st.slider("Credit Score", 300, 900, 600)
age = st.slider("Age", 18, 90, 40)
tenure = st.slider("Tenure", 0, 10, 5)
balance = st.number_input("Balance", 0.0, 300000.0, 50000.0)
num_products = st.slider("Number of Products", 1, 4, 2)
has_card = st.selectbox("Has Credit Card", [0,1])
active_member = st.selectbox("Active Member", [0,1])
salary = st.number_input("Estimated Salary", 0.0, 200000.0, 80000.0)

geo = st.selectbox("Geography", ["France","Spain","Germany"])
gender = st.selectbox("Gender", ["Male","Female"])
geo_map = {"France":0, "Germany":1, "Spain":2}
gender_map = {"Female":0, "Male":1}

geo_val = geo_map[geo]
gender_val = gender_map[gender]

if st.button("Predict Churn"):

    input_data = np.array([[2025, credit_score, geo_val, gender_val,
                            age, tenure, balance, num_products,
                            has_card, active_member, salary]])

    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0][1]

    if prediction == 1:
        st.error(f"⚠ High Churn Risk ({probability:.2f})")
    else:
        st.success(f"✅ Low Churn Risk ({probability:.2f})")
