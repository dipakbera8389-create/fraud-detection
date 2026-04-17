import streamlit as st
import joblib
import numpy as np
# load model
model = joblib.load("fraud_model.pkl")

st.title("💳 Online Payment Fraud Detection")

st.write("Enter Transaction Details:")

features = []

# V1 to V28
for i in range(1, 29):
    val = st.number_input(f"V{i}", value=0.0)
    features.append(val)
# Amount
amount = st.number_input("Amount", value=0.0)
features.append(amount)
# convert
input_data = np.array(features).reshape(1, -1)
# prediction
if st.button("Check Transaction"):
    pred = model.predict(input_data)
    if pred[0] == 1:
        st.error("🚨 Fraud Transaction Detected!")
    else:
        st.success("✅ Normal Transaction")


        # python -m streamlit run app.py