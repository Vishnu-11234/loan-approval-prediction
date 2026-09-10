import streamlit as st

st.set_page_config(
    page_icon="🏠",
    page_title="Loan Prediction/Home"

)

st.title("🏦 Loan Approval Prediction System")

st.markdown("""
### Machine Learning Based Loan Approval Prediction

    This application uses a **Decision Tree Classifier** to predict
    whether a loan application is likely to be approved based on
    applicant, financial, and loan-related information."""

)
st.divider()

st.subheader("Project Overview")
st.write("""The system takes applicant information such as income, credit score,
    existing loans, savings, loan amount, employment status, and other
    relevant attributes and uses a trained machine learning model to
    generate a prediction.
""")
st.subheader("How it works")
col1,col2,col3,col4=st.columns(4)
with col1:
    st.markdown("### 1️⃣")
    st.write("Enter Applicant Details")
with col2:
    st.markdown("### 2️⃣")
    st.write("Preprocesses Input Data")
with col3:
    st.markdown("### 3️⃣")
    st.write("Decision Tree Prediction")
with col4:
    st.markdown("### 4️⃣")
    st.write("View Prediction Results")
st.divider()

st.subheader("Machine Learning Model")
col1,col2,col3=st.columns(3)
with col1:
    st.metric(
        "Algorithm",
        "Decision Tree"
    )
with col2:
    st.metric(
        "Problem Type",
        "Classification"
    )
with col3:
    st.metric(
        "Prediction",
        " Loan Approval"
    )
st.divider()
st.subheader("Get Started")
st.write(
     "Go to the **Prediction** page from the sidebar to enter "
    "an applicant's information and generate a prediction."
)