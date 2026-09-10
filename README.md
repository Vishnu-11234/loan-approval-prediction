# 🏦 Loan Approval Prediction System

A Machine Learning web application that predicts whether a loan application is likely to be approved based on applicant, financial, and loan-related information.

The application uses a **Decision Tree Classifier** with preprocessing and hyperparameter tuning, and provides an interactive interface using **Streamlit**.

---

## 📌 Project Overview

Loan approval decisions depend on several factors such as income, credit score, existing loans, savings, loan amount, employment status, and other applicant information.

This project builds a machine learning pipeline that:

- Processes missing values
- Encodes categorical features
- Trains a Decision Tree Classifier
- Tunes model hyperparameters using GridSearchCV
- Evaluates model performance
- Predicts loan approval
- Displays approval probability
- Provides data analytics through a Streamlit dashboard

---

## 🎯 Objective

The main objective is to build an end-to-end Machine Learning application that can predict:

```text
0 → Loan Rejected
1 → Loan Approved