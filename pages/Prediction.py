import streamlit as st
import sys
import os

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.insert(0, PROJECT_ROOT)

from src.models.predict import predict_loan


st.set_page_config(
    page_icon="🔮",
    page_title="Loan Prediction",
    layout="wide"
)


st.title("Loan Approval Prediction")
st.write("Enter the applicant details below to predict")

st.divider()


st.header(" 👤 Applicant Information")
col1,col2,col3=st.columns(3)
with col1:
    applicant_id=st.number_input(
        "Applicant Id",
        min_value=1,
        max_value=2000,
        step=1

    )
    age=st.number_input(
        "Age ",
        min_value=18,
        max_value=100,
        

    )
    gender=st.selectbox(
        "Gender",
        ["Male","Female"]
       
    )
with col2:
    marital_status=st.selectbox(
        "Marital Status",
        ["Married","Single"]
    )
    dependents=st.number_input(
        "Dependents",
        min_value=1,
        max_value=8,

    )
    education_level=st.selectbox(
        "Education Level",
        ["Graduate","Not Graduate"]
    )
with col3:
    employment_status=st.selectbox(
        "Employment Status",
        ["Salaried","Self_Employed","Contract","Unemployed"]
    )
    employer_category=st.selectbox(
        "Employer Category",
        ["Private","NMC","Government"]
    )

st.divider()
st.subheader("FInancial Information")
col1,col2,col3=st.columns(3)
with col1:
    applicant_income=st.number_input(
        "Applicant Income",
        min_value=0.0,
        max_value=100000.0

    )
    coapplicant_income=st.number_input(
        "Coapplicant Income",
        min_value=0.0,
        max_value=100000.0
    )
    savings=st.number_input(
        "Savings",
        min_value=0.0,
        max_value=100000.0
        
    )
with col2:
    credit_score=st.number_input(
        "Credit Score",
        min_value=200.0,
        max_value=900.0,
        step=1.0

    )
    existing_loans=st.number_input(
        " Existing Loan",
        min_value=0.0,
        max_value=10.0,
        step=1.0
    )
    dti_ratio=st.number_input(
        "DT Ratio",
        min_value=0.0,
        max_value=1.0,
        step=0.01
        
    )
with col3:
    collateral_value=st.number_input(
        "Collateral Value",
        min_value=0.0,
        max_value=20000.0
    )
    loan_amount=st.number_input(
        "Loan Amount",
        min_value=0.0,
        max_value=100000.0
    )
    loan_term=st.number_input(
        "Loan Term",
        min_value=1.0,
        max_value=100.0
    )

st.divider()
st.subheader("Loan Information")

col1,col2=st.columns(2)
with col1:
    loan_purpose=st.selectbox(
        "Loan Purpose",
        [
            "Personal",
            "Car",
            "Business",
            "Home"
        ]

    )
with col2:
    property_area=st.selectbox(
        "Property Area",
        [
            "Urban",
            "Semiurban",
            "Rural"
        ]
    )
st.divider()
predict_button=st.button(
    "Predict Loan Approval",
    type="primary",
    use_container_width=True
)

if predict_button:
    application_data = {

        "Applicant_ID": applicant_id,

        "Applicant_Income": applicant_income,

        "Coapplicant_Income": coapplicant_income,

        "Age": age,

        "Dependents": dependents,

        "Credit_Score": credit_score,

        "Existing_Loans": existing_loans,

        "DTI_Ratio": dti_ratio,

        "Savings": savings,

        "Collateral_Value": collateral_value,

        "Loan_Amount": loan_amount,

        "Loan_Term": loan_term,

        "Employment_Status": employment_status,

        "Marital_Status": marital_status,

        "Loan_Purpose": loan_purpose,

        "Property_Area": property_area,

        "Education_Level": education_level,

        "Gender": gender,

        "Employer_Category": employer_category
    }
    try:
        prediction=predict_loan(application_data)
        st.divider()
        st.subheader("📊 Prediction Result")
        if prediction==1:
            st.success("✅ Loan Application is likely to be APPROVED")
        elif prediction==0:
             st.error("❌ Loan Application is likely to be REJECTED" )
        else:
            st.warning("Unexpected Prediction Value")


    except Exception as e:
        st.error(f"Prediction Failed{e}")
    
