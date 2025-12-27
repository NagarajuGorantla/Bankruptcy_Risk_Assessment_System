Bankruptcy Risk Assessment System








Overview

The Bankruptcy Risk Assessment System is an end-to-end machine learning application designed to estimate the probability of business bankruptcy using key financial and operational risk indicators.

The project follows industry-standard ML engineering practices, including:

clear separation of experimentation, training, and inference

deployment-ready architecture

reproducible environment setup

interpretable modeling for financial decision support

This repository demonstrates not only model building, but how ML systems are structured, deployed, and consumed in real-world environments.

Business Problem

Early identification of bankruptcy risk allows organizations, investors, and analysts to take preventive actions before financial failure occurs.

The objective of this system is to:

classify bankruptcy risk

provide probability-based confidence scores

favor interpretability over black-box accuracy

Solution Summary

Conducted exploratory data analysis to understand risk patterns

Trained a Logistic Regression model optimized for transparency

Built a clean inference layer decoupled from training logic

Deployed an interactive Streamlit web application for real-time predictions

Tech Stack

Programming & Analysis

Python

Pandas

NumPy

Machine Learning

Scikit-learn

Application & Deployment

Streamlit

Project Architecture
Bankruptcy-Risk-Assessment/
│
├── app/                     # Application layer
│   ├── app.py               # Streamlit UI
├── model/                   # Serialized model artifacts
│   ├── logistic_regression.pkl
│
├── data/                    # Dataset
│   └── Bankruptcy_Dataset.xlsx
│
├── notebooks/               # EDA,Training & preprocessing
│   └── Bankruptcy_Risk_Assessment.ipynb
│
├── requirements.txt
├── README.md
└── .gitignore


Design principle:

Notebooks are for experimentation.
Python modules are for production.

Model Details

Algorithm: Logistic Regression

Target Variable: Bankruptcy status

Why Logistic Regression?

High interpretability (critical in financial domains)

Stable performance on structured tabular data

Probability outputs support risk-based decisions

Application Features

Interactive user input via sliders

Real-time bankruptcy risk prediction

Probability confidence score output

Lightweight and cloud-deployable interface

Live Demo

🚀 Deployed Application:
👉 https://bankruptcyriskassessmentsystem-kde95dnh3p4qzeomfgsjgu.streamlit.app/

How to Run Locally
git clone https://github.com/yourusername/Bankruptcy-Risk-Assessment.git
cd Bankruptcy-Risk-Assessment
pip install -r requirements.txt
streamlit run app/app.py

Design Decisions

Chose interpretability over complex black-box models

Decoupled training and inference for deployment safety

Used joblib instead of raw pickle for sklearn compatibility

Avoided training logic inside the application layer

Limitations

Model performance depends on historical feature quality

Threshold values may require domain-specific tuning

Not intended as a standalone financial decision system

Future Improvements

SHAP-based feature explainability

Model monitoring and retraining pipeline

Threshold optimization based on risk tolerance

CI/CD integration for automated deployment

Cloud deployment using Docker

Disclaimer

This project is for educational and analytical purposes only and should not be used as a sole basis for financial or investment decisions.

Recruiter Signal

This project demonstrates:

End-to-end ML system design

Production-ready project structuring

Deployment and environment management

Business-aware modeling decisions

Clean, maintainable, review-friendly code
📊 Explainability upgrade (SHAP)

Say the word — we keep leveling.
