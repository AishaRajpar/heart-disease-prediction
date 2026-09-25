import streamlit as st
import joblib
import pandas as pd

# --------------------------------------------------
# PAGE SETTINGS
# --------------------------------------------------

st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>
.main {
    background-color: #f5f8fa;
}
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1200px;
}
/* Header */
.header-box {
    background-color: #0f766e;
    padding: 30px;
    border-radius: 15px;
    color: white;
    margin-bottom: 25px;
}
.header-title {
    font-size: 38px;
    font-weight: bold;
    margin-bottom: 8px;
}
.header-text {
    font-size: 17px;
}
/* Section headings */
.section-heading {
    font-size: 24px;
    font-weight: bold;
    color: #164e63;
    margin-top: 20px;
    margin-bottom: 15px;
}
/* Predict button */
.stButton > button {
    width: 100%;
    height: 55px;
    background-color: #0f766e;
    color: white;
    border: none;
    border-radius: 10px;
    font-size: 18px;
    font-weight: bold;
}
.stButton > button:hover {
    background-color: #115e59;
    color: white;
}
/* Result */
.result-box {
    padding: 25px;
    border-radius: 15px;
    margin-top: 25px;
    text-align: center;
}
.success-box {
    background-color: #ecfdf5;
    border: 2px solid #10b981;
}
.danger-box {
    background-color: #fff1f2;
    border: 2px solid #f43f5e;
}
.result-title {
    font-size: 27px;
    font-weight: bold;
}
.probability {
    font-size: 20px;
    font-weight: bold;
    margin-top: 10px;
}
/* Sidebar */
.sidebar-title {
    font-size: 23px;
    font-weight: bold;
    color: #0f766e;
}
.info-box {
    background-color: #f0fdfa;
    padding: 15px;
    border-radius: 10px;
    border-left: 4px solid #0f766e;
}
.footer {
    text-align: center;
    color: #64748b;
    margin-top: 40px;
    padding: 20px;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# LOAD MODEL FILES
# --------------------------------------------------

model = joblib.load("logistic_regression_model.pkl")
scaler = joblib.load("scaler.pkl")
expected_columns = joblib.load("column.pkl")

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:
    st.markdown("<h2 style='color:#0f766e;'>❤️ Heart Health</h2>", unsafe_allow_html=True)
    st.markdown("---")

    st.subheader("About This App")
    st.write(
        "This application uses a Machine Learning model "
        "to predict the likelihood of heart disease based "
        "on selected patient health information."
    )

    st.subheader("How it works")
    st.write("1. Enter patient information")
    st.write("2. Click the Predict button")
    st.write("3. The ML model analyzes the information")
    st.write("4. View the prediction probability")

    st.markdown("---")

    st.warning(
        "⚠️ This application is for educational purposes "
        "only and should not be used as a medical diagnosis."
    )

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown("""
<div class="header-box">
<div class="header-title">❤️ Heart Disease Prediction</div>
<div class="header-text">Machine Learning based heart disease risk prediction system</div>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# PATIENT INFORMATION
# --------------------------------------------------

st.markdown("<div class='section-heading'>👤 Patient Information</div>", unsafe_allow_html=True)

# Two columns
col1, col2 = st.columns(2)

# --------------------------------------------------
# LEFT COLUMN
# --------------------------------------------------

with col1:
    age = st.slider("Age", 18, 100, 40)

    sex = st.selectbox("Sex", ["M", "F"])

    cp = st.selectbox("Chest Pain Type", ["ATA", "NAP", "TA", "ASY"])

    trestbps = st.slider("Resting Blood Pressure", 90, 200, 120)

    chol = st.slider("Serum Cholesterol", 120, 564, 240)

    fbs = st.selectbox(
        "Fasting Blood Sugar",
        [0, 1],
        format_func=lambda x: "Yes" if x == 1 else "No"
    )

# --------------------------------------------------
# RIGHT COLUMN
# --------------------------------------------------

with col2:
    restecg = st.selectbox("Resting ECG Results", ["Normal", "ST", "LVH"])

    thalach = st.slider("Maximum Heart Rate Achieved", 70, 202, 150)

    exang = st.selectbox("Exercise Induced Angina", ["Yes", "No"])

    oldpeak = st.slider("ST Depression", 0.0, 6.2, 1.0, step=0.1)

    slope = st.selectbox("Slope of Peak Exercise ST Segment", ["Up", "Flat", "Down"])

# --------------------------------------------------
# PREDICTION SECTION
# --------------------------------------------------

st.markdown("<div class='section-heading'>🔍 Prediction</div>", unsafe_allow_html=True)

if st.button("❤️ Predict Heart Disease Risk"):

    # Create input data
    input_data = pd.DataFrame({
        "age": [age],
        "sex": [1 if sex == "M" else 0],
        "cp": [cp],
        "trestbps": [trestbps],
        "chol": [chol],
        "fbs": [fbs],
        "restecg": [restecg],
        "thalach": [thalach],
        "exang": [1 if exang == "Yes" else 0],
        "oldpeak": [oldpeak],
        "slope": [slope]
    })

    # Match columns with training data
    input_data = input_data.reindex(columns=expected_columns, fill_value=0)

    # Scale input
    scaled_input = scaler.transform(input_data)

    # Prediction
    prediction = model.predict(scaled_input)
    prediction_proba = model.predict_proba(scaled_input)

    # --------------------------------------------------
    # RESULT
    # --------------------------------------------------

    if prediction[0] == 1:
        probability = prediction_proba[0][1] * 100

        st.markdown(f"""
<div class="result-box danger-box">
<div class="result-title">⚠️ Heart Disease Risk Detected</div>
<div class="probability">Predicted Probability: {probability:.2f}%</div>
<p>The model predicts that the patient may have a higher likelihood of heart disease.</p>
</div>
""", unsafe_allow_html=True)

        st.progress(float(prediction_proba[0][1]))

    else:
        probability = prediction_proba[0][0] * 100

        st.markdown(f"""
<div class="result-box success-box">
<div class="result-title">✅ Lower Heart Disease Risk</div>
<div class="probability">Predicted Probability: {probability:.2f}%</div>
<p>The model predicts that the patient is less likely to have heart disease.</p>
</div>
""", unsafe_allow_html=True)

        st.progress(float(prediction_proba[0][0]))

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("""
<div class="footer">
❤️ Heart Disease Prediction System<br>
Machine Learning Project | Educational Purpose Only
</div>
""", unsafe_allow_html=True)