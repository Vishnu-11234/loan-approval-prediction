import pandas as pd
import pickle


with open("models/model_pipeline.pkl","rb")as file:
    model_pipeline=pickle.load(file)

def predict_loan(application_data):
    df=pd.DataFrame([application_data])
   
    prediction=model_pipeline.predict(df)[0]
    return prediction

if __name__ == "__main__":

    sample_application = {
        "Applicant_ID": 1001,
        "Applicant_Income": 50000,
        "Coapplicant_Income": 10000,
        "Age": 30,
        "Dependents": 1,
        "Credit_Score": 750,
        "Existing_Loans": 1,
        "DTI_Ratio": 0.30,
        "Savings": 50000,
        "Collateral_Value": 200000,
        "Loan_Amount": 100000,
        "Loan_Term": 20,
        "Employment_Status": "Employed",
        "Marital_Status": "Married",
        "Loan_Purpose": "Home",
        "Property_Area": "Urban",
        "Education_Level": "Graduate",
        "Gender": "Male",
        "Employer_Category": "Private"
    }

    prediction = predict_loan(sample_application)


    print("Prediction:", prediction)
