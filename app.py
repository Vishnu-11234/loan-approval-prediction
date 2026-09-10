import streamlit as st


st.set_page_config(
    page_icon="🏦",
    page_title="Loan Approval Predictor",
    layout="wide"
)


# -------------------------------
# Define Pages
# -------------------------------

home = st.Page(
    "pages/Home.py",
    title="Home",
    icon="🏠"
    
)

prediction = st.Page(
    "pages/Prediction.py",
    title="Prediction",
    icon="🔮"
)

analytics = st.Page(
    "pages/Analytics.py",
    title="Analytics",
    icon="📊"
)

about = st.Page(
    "pages/About.py",
    title="About",
    icon="ℹ️"
)


# -------------------------------
# Navigation
# -------------------------------

pg = st.navigation(
    [
        home,
        prediction,
        analytics,
        about
    ],
    position="top"
)


# -------------------------------
# Run Selected Page
# -------------------------------

pg.run()