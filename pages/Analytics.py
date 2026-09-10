import streamlit as st
import pandas as pd
import matplotlib.pylab as plt
import numpy as np
import seaborn as sns

st.set_page_config(
    page_icon="📊",
    page_title="Analytics",
    layout="wide"
)

def load_data():
    df=pd.read_csv("data/cleaned/cleaned_data.csv")
    return df

df=load_data()
st.title("📊 Loan Analysis")
st.write( "Explore the loan dataset through key statistics, "
    "distributions, and approval trends.")

st.divider()

st.header("📋 Dataset Overview")

col1,col2,col3,col4=st.columns(4)
with col1:
    st.metric(
        "Total Data Points",
        len(df)
    )
with col2:
    approved=(
        df["Loan_Approved"].value_counts().get(1,0)

    )
    st.metric(
        "Approved",
        approved
    )
with col3:
    rejected=(
            df["Loan_Approved"].value_counts().get(0,0)
    
        )
    st.metric(
            "Rejected",
            rejected
        )
with col4:
    approval_rate=(
        approved/(approved+rejected)*100
    )
    st.metric(
        "Approval Rate",
        f"{approval_rate:.2f} %"
    )

st.divider()


col1,col2=st.columns(2)
with col1:
    approval_count=df["Loan_Approved"].value_counts()
    
    fig,ax=plt.subplots()
    ax.bar(
        approval_count.index,
        approval_count.values
    )
    ax.set_xlabel("Loan Approval")
    ax.set_ylabel(" Number Of Applications")
    ax.set_title("Loan Approval Distribution")
    st.pyplot(fig)
with col2:
    st.subheader("Approval Summary")
    summary=pd.DataFrame({
        'Status': approval_count.index,
        "Applications":approval_count.values
    })
    st.dataframe(summary,hide_index=True)
st.divider()

col1,col2=st.columns(2)
with col1:
    st.subheader("Applicant Income Distribution")
    fig,ax=plt.subplots()
    ax.hist(
        df["Applicant_Income"].dropna(),
        bins=20
    )
    ax.set_xlabel("Applicant Income")
    ax.set_ylabel("Number Of Applicants")
    ax.set_title("Applicant Income Distribution")
    st.pyplot(fig)

with col2:
    st.subheader("Credit Score vs Loan Approval")
    fig, ax = plt.subplots()

    df.boxplot(
        column="Credit_Score",
        by="Loan_Approved",
        ax=ax
    )

    ax.set_title("Credit Score vs Loan Approval")
    ax.set_xlabel("Loan Approval")
    ax.set_ylabel("Credit Score")

    plt.suptitle("")

    st.pyplot(fig)

st.divider()
st.subheader("Distribution")
col1,col2=st.columns(2)
with col1:
    
    fig,ax=plt.subplots()
    sns.scatterplot(
        data=df,
        x="Loan_Amount",
        y="Credit_Score",
        hue="Loan_Approved"
    )
    ax.set_xlabel("Loan Amount")
    ax.set_ylabel("Credit Score ")
    ax.set_title("Loan Amount And Credit Score Distribution")
    st.pyplot(fig)
with col2:
    fig,ax=plt.subplots()
    sns.scatterplot(
        data=df,
        x="DTI_Ratio",
        y="Credit_Score",
        hue="Loan_Approved"
    )
    ax.set_xlabel(" DTI Ratio")
    ax.set_ylabel("Credit Score ")
    ax.set_title("DTI Ratio And Credit Score Distribution")
    st.pyplot(fig)
st.divider()
st.subheader("Dataframe Overview")
st.dataframe(
    df.head(10)
)