# Bankruptcy Risk Assessment System

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Live-red)
![Status](https://img.shields.io/badge/Status-Production--Ready-success)
![License](https://img.shields.io/badge/License-MIT-green)

## Overview
The Bankruptcy Risk Assessment System is an end-to-end machine learning application designed to estimate the probability of business bankruptcy using key financial and operational risk indicators.

The project follows industry-standard ML engineering practices, including clear separation of experimentation, training, and inference, deployment-ready architecture, and reproducible environment setup.

## Business Problem
Early identification of bankruptcy risk allows organizations and analysts to take preventive actions before financial failure occurs.

## Solution Summary
- Exploratory data analysis to understand risk patterns
- Logistic Regression model optimized for interpretability
- Clean inference layer decoupled from training logic
- Interactive Streamlit web application for real-time predictions

## Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- Joblib
- Streamlit

## Project Architecture
```
Bankruptcy-Risk-Assessment/
├── app/
├── src/
├── model/
├── data/
├── notebooks/
├── requirements.txt
└── README.md
```

## Model Details
Algorithm: Logistic Regression  
Chosen for transparency, stability, and probability-based outputs.

## How to Run Locally
```bash
git clone https://github.com/yourusername/Bankruptcy-Risk-Assessment.git
cd Bankruptcy-Risk-Assessment
pip install -r requirements.txt
streamlit run app/app.py
```

## Disclaimer
For educational and analytical purposes only.
