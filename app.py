import streamlit as st
import pickle

model = pickle.load(open("fraud_model.pkl", "rb"))

st.title("💳AI Fraud Detection")
st.markdown("This application predicts whether a transaction is fraudlent using Machine Learning.")

amount = st.number_input("Transaction Amount")

hour = st.slider("Transaction Hour", 0, 23)

online = st.selectbox(
    "Online Transaction",
    ["No", "Yes"]
)

card_present = st.selectbox(
    "Card Present",
    ["No", "Yes"]
)

new_device = st.selectbox(
    "New Device",
    ["No", "Yes"]
)

high_risk_country = st.selectbox(
    "High Risk Country",
    ["No", "Yes"]
)

if st.button("Check Fraud Risk"):

    input_data = [[
        amount,
        hour,
        1 if online == "Yes" else 0,
        1 if card_present == "Yes" else 0,
        1 if new_device == "Yes" else 0,
        1 if high_risk_country == "Yes" else 0
    ]]

    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)[0][1]

    if prediction[0] == 1:
        st.error(f"Fraud Risk: HIGH 🚨 (Probability: {probability:.2f})")
    else:
        st.success("Legitimate Transaction ✅")