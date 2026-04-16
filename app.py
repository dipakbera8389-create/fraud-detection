import streamlit as st
import pandas as pd
import joblib
model = joblib.load("fraud_model.pkl")
st.title("Fraud Detection")
amount = st.number_input("Transaction Amount")
account_age = st.number_input("Account Age (days)")
num_txn = st.number_input("Transactions last 24h")
is_international = st.selectbox("Is International?", [0, 1])
device_trusted = st.selectbox("Device Trusted?", [0, 1])
input_data = pd.DataFrame({
    "transaction_amount": [amount],
    "account_age_days": [account_age],
    "num_transactions_last_24h": [num_txn],
    "is_international": [is_international],
    "device_trusted": [device_trusted]
})
if st.button("Predict"):
    result = model.predict(input_data)
    if result[0] == 1:
        st.error("🚨 Fraud")
    else:
        st.success("✅ Not Fraud")








