import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load model and features
model = pickle.load(open('churn_model.pkl', 'rb'))
model_columns = pickle.load(open('churn_model_columns.pkl', 'rb'))

st.title("Customer Churn Prediction")

st.sidebar.header("Customer Inputs")

tenure = st.sidebar.slider("Tenure (months)", 0, 72)
monthly_charges = st.sidebar.number_input("Monthly Charges")
total_services = st.sidebar.slider("Total Services Used", 0, 10)

contract = st.sidebar.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])

internet = st.sidebar.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

payment = st.sidebar.selectbox("Payment Method", [
    "Electronic check",
    "Mailed check",
    "Bank transfer (automatic)",
    "Credit card (automatic)"
])


input_dict = {col: 0 for col in model_columns}


# Fill only known inputs
input_dict['tenure'] = tenure
input_dict['MonthlyCharges'] = monthly_charges
input_dict['TotalServices'] = total_services



# Contract mapping
if contract == "One year":
    input_dict['Contract_One year'] = 1
elif contract == "Two year":
    input_dict['Contract_Two year'] = 1

# Internet mapping
if internet == "Fiber optic":
    input_dict['InternetService_Fiber optic'] = 1
elif internet == "No":
    input_dict['InternetService_No'] = 1

# Payment mapping
if payment == "Electronic check":
    input_dict['PaymentMethod_Electronic check'] = 1
elif payment == "Mailed check":
    input_dict['PaymentMethod_Mailed check'] = 1
elif payment == "Bank transfer (automatic)":
    input_dict['PaymentMethod_Bank transfer (automatic)'] = 1
elif payment == "Credit card (automatic)":
    input_dict['PaymentMethod_Credit card (automatic)'] = 1
input_df = pd.DataFrame([input_dict])

if st.button("Predict"):
    prediction = model.predict(input_df)
    prob = round(model.predict_proba(input_df)[0][1] *100,2)
    not_churn = round( model.predict_proba(input_df)[0][0]*100, 2)
    if prediction[0] == 1:
        st.error(f"Customer is likely to churn with {prob}% ❌")
    else:
        st.success(f"Customer is not likely to churn with {not_churn}% ✅")