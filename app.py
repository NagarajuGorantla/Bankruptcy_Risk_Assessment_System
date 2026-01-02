import streamlit as st
import pandas as pd
import joblib
import os

st.set_page_config(page_title="Bankruptcy Risk Assessment", layout="centered")

st.title("🏦 Bankruptcy Risk Assessment System")
st.write("Predict bankruptcy risk using a trained ML model.")

# Paths (RELATIVE — deployment safe)
MODEL_PATH = os.path.join("model", "LOGISTIC_REGRESSION.pkl")
DATA_PATH = os.path.join("data", "Bankruptcy_Dataset.xlsx")

# Load model
@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

model = load_model()

# Sidebar inputs (example)
st.sidebar.header("Input Features")

industrial_risk = st.sidebar.slider("Industrial Risk", 0.0, 1.0, 0.5)
management_risk = st.sidebar.slider("Management Risk", 0.0, 1.0, 0.5)
financial_flexibility = st.sidebar.slider("Financial Flexibility", 0.0, 1.0, 0.5)
credibility = st.sidebar.slider("Credibility", 0.0, 1.0, 0.5)
competitiveness = st.sidebar.slider("Competitiveness", 0.0, 1.0, 0.5)
operating_risk = st.sidebar.slider("Operating Risk", 0.0, 1.0, 0.5)

input_df = pd.DataFrame([[
    industrial_risk,
    management_risk,
    financial_flexibility,
    credibility,
    competitiveness,
    operating_risk
]], columns=[
    "industrial_risk",
    "management_risk",
    "financial_flexibility",
    "credibility",
    "competitiveness",
    "operating_risk"
])

if st.button("Predict"):
    prediction = model.predict(input_df)[0]
    if prediction == 1:
        st.error("⚠️ High Bankruptcy Risk")
    else:
        st.success("✅ Low Bankruptcy Risk")
