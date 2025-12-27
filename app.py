import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Bankruptcy Risk Assessment",
    page_icon="📉",
    layout="wide"
)

# ------------------ LOAD MODEL (SAFE) ------------------
MODEL_PATH = "LOGISTIC_REGRESSION.pkl"

if not os.path.exists(MODEL_PATH):
    st.error(f"❌ Model file not found: {MODEL_PATH}")
    st.stop()

try:
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
except Exception as e:
    st.error("❌ Failed to load model")
    st.exception(e)
    st.stop()

# ------------------ SIDEBAR ------------------
st.sidebar.title("📊 Business Risk Inputs")

industrial_risk = st.sidebar.slider("Industrial Risk", 0.0, 1.0, 0.25)
management_risk = st.sidebar.slider("Management Risk", 0.0, 1.0, 0.30)
financial_flexibility = st.sidebar.slider("Financial Flexibility", 0.0, 1.0, 0.40)
credibility = st.sidebar.slider("Credibility", 0.0, 1.0, 0.35)
competitiveness = st.sidebar.slider("Competitiveness", 0.0, 1.0, 0.30)
operating_risk = st.sidebar.slider("Operating Risk", 0.0, 1.0, 0.25)

# ------------------ INPUT DATA ------------------
X = pd.DataFrame(
    [[
        industrial_risk,
        management_risk,
        financial_flexibility,
        credibility,
        competitiveness,
        operating_risk
    ]],
    columns=[
        "industrial_risk",
        "management_risk",
        "financial_flexibility",
        "credibility",
        "competitiveness",
        "operating_risk"
    ]
)

# ------------------ MAIN UI ------------------
st.title("🏦 Bankruptcy Risk Assessment System")
st.markdown(
    "A machine learning tool to estimate bankruptcy risk based on key business indicators."
)

# ------------------ INPUT SNAPSHOT ------------------
st.subheader("📌 Model Input Snapshot")
st.dataframe(X, width='stretch')

# ------------------ PREDICTION ------------------
prediction = model.predict(X)[0]
proba = model.predict_proba(X)[0]

# Handle class order safely
class_labels = list(model.classes_)
non_bankrupt_prob = proba[class_labels.index(0)]
bankrupt_prob = proba[class_labels.index(1)]

# ------------------ RESULT ------------------
st.subheader("🔍 Risk Assessment Result")

if prediction == 1:
    st.error("⚠️ High Bankruptcy Risk Detected")
else:
    st.success("✅ Low Bankruptcy Risk")

# ------------------ PROBABILITY ------------------
st.subheader("📈 Prediction Confidence")

col1, col2 = st.columns(2)
col1.metric("Non-Bankrupt Probability", f"{non_bankrupt_prob * 100:.2f}%")
col2.metric("Bankrupt Probability", f"{bankrupt_prob * 100:.2f}%")

# ------------------ FEATURE IMPORTANCE ------------------
if hasattr(model, "coef_"):
    st.subheader("🧠 Key Risk Drivers")

    importance_df = pd.DataFrame({
        "Feature": X.columns,
        "Impact": model.coef_[0]
    }).sort_values(by="Impact", ascending=False)

    st.bar_chart(importance_df.set_index("Feature"))

# ------------------ DISCLAIMER ------------------
st.info(
    """
    **Disclaimer:**  
    This tool provides a probabilistic risk estimate based on historical data.
    It is intended for analytical support only and should not be considered financial advice.
    """
)
