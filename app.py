import streamlit as st
import numpy as np

# PAGE CONFIG
st.set_page_config(
    page_title="Loan Approval Prediction System",
    layout="wide",
    page_icon="💰"
)

# CSS
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #e3f2fd, #ffffff);
}
.title {
    text-align:center;
    font-size:42px;
    font-weight:bold;
    color:#0d47a1;
}
.card {
    background:White;
    padding:20px;
    border-radius:15px;
    box-shadow:0 4px 15px rgba(0,0,0,0.2);
}
.good { color:#2e7d32; font-weight:bold; }
.bad { color:#c62828; font-weight:bold; }
</style>
""", unsafe_allow_html=True)

#TITLE
st.markdown(
    '<div class="title">💰 Loan Approval Prediction</div>',
    unsafe_allow_html=True
)

st.markdown("---")

# INPUT SECTION
st.subheader("💰 Applicant Details")

col1, col2, col3 = st.columns(3)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    married = st.selectbox("Married", ["Yes", "No"])
    dependents = st.slider("Dependents", 0, 5, 0)
    education = st.selectbox("Education", ["Graduate", "Not Graduate"])

with col2:
    self_employed = st.selectbox("Self Employed", ["Yes", "No"])
    applicant_income = st.slider("Applicant Income", 1500, 80000, 5000)
    coapplicant_income = st.slider("Coapplicant Income", 0, 50000, 0)

with col3:
    loan_amount = st.slider("Loan Amount (in thousands)", 10, 700, 100)
    loan_amount_term = st.selectbox("Loan Amount Term (months)", [360, 120, 180, 300, 60, 240])
    credit_history = st.selectbox("Credit History", [0, 1])
    property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

st.markdown("---")

# RULE-BASED LOGIC
# Simple scoring logic (example, you can replace with trained ML model later)
risk_score = 0
if applicant_income < 2500: risk_score += 1
if coapplicant_income == 0: risk_score += 1
if loan_amount > 200: risk_score += 1
if credit_history == 0: risk_score += 2
if education == "Not Graduate": risk_score += 1
if self_employed == "Yes": risk_score += 1
if property_area == "Rural": risk_score += 1

# RESULT
st.markdown("---")
st.subheader("💰 Prediction Result")

if st.button("💰 Predict Loan Approval"):
    if risk_score >= 4:
        st.markdown("""
        <div class="card bad">
        💰 <b>High Risk / Likely Loan Rejection</b><br>
        Applicant may need to improve profile or collateral.
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="card good">
        💰 <b>Low Risk / Likely Loan Approval</b><br>
        Applicant profile seems good for approval.
        </div>
        """, unsafe_allow_html=True)

# FOOTER
st.markdown("""
<br>
<center>
<b>End-to-End Loan Approval Prediction Project</b><br>
Data Science & Machine Learning
</center>
""", unsafe_allow_html=True)
