import streamlit as st

st.set_page_config(
    page_icon="ℹ️",
    page_title="About",
    layout="wide"
)
#page title
st.title("ℹ️ About The Project")
st.write("A MAchine Learning application that predicts wether "
         "a loan application is likely to be approved based on"
         "applicant, financial,and loan related information")

st.divider()

st.subheader("📌 Project Overview")
st.write("This project uses a Decision Tree Classifier to predict"
         "loan approval. THe Machine Learning pipeline includes data preprocessing," 
         "missing-value handeling,categorical encoding,model training and evaluation")

st.divider()
st.subheader("Machine Learning Pipeline")
st.markdown(
     """
    **1. Data Collection**
    
    - Loan application data is loaded from the dataset.

    **2. Data Preprocessing**
    
    - Missing numerical values are handled using Mean Imputation
    - Missing categorical values are handled using Most Frequent Imputation
    - Categorical variables are converted using One-Hot Encoding

    **3. Model Training**
    
    - A Decision Tree Classifier is trained on the processed data.

    **4. Hyperparameter Tuning**
    
     - GridSearchCV was used to find suitable Decision Tree
    hyperparameters.

    **5. Prediction**
    
    - The trained pipeline predicts whether a loan application
    is likely to be approved or rejected.
    """
)
st.divider()

#model information
st.subheader("Model Information")
col1,col2=st.columns(2)
with col1:
    st.subheader("Algorithm")
    st.write("Decision Tree Classifier")
    st.subheader("Splitting Criterion")
    st.write("Gini Impurity")
with col2:
    st.subheader("Maximum Depth")
    st.write("5")
    st.subheader("Maximum Sample Per Leaf")
    st.write("4")
st.divider()

#technologies used
st.subheader("Technologies Used")
col1,col2,col3=st.columns(3)
with col1:
    st.subheader("Data Handeling")
    st.write("Python")
    st.write("Pandas")
    st.write("Numpy")
with col2:
    st.subheader("Machine Learning")
    st.write("Scikit-learn")
    st.write("Decision Tree")
    st.write("GridSearch CV")
with col3:
    st.subheader(" Visualization & App")
    st.write(" Matplotlib")
    st.write(" Seaborn")
    st.write(" Streamlit")
    st.write(" Pickle")



#Project Architecture
st.header("📁 Project Architecture")

st.code(
    """
Decision_Tree/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   ├── raw/
│   │   └── loan_approval_data.csv
│   │
│   └── cleaned/
│       └── cleaned_data.csv
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_model_training.ipynb
│   └── 04_model_evaluation.ipynb
│
├── src/
│   ├── data/
│   │   └── preprocess.py
│   │
│   |
│   │
│   ├── models/
│       ├── train.py
│       └── predict.py
│   
│   
│       
│
├── models/
│   └── model_pipeline.pkl
│
└── pages/
    ├── Home.py
    ├── Prediction.py
    ├── Analytics.py
    └── About.py
    """,
    language="text"
)
st.divider()


st.header("⚠️ Disclaimer")

st.info(
    """
    This application provides a machine learning prediction
    based on historical data. The prediction should not be
    considered a final financial or lending decision.
    """
)



st.divider()
#Caption
st.caption(
    "Loan Approval Prediction System • Machine Learning Project"
)