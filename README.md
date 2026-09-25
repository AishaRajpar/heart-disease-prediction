# ❤️ Heart Disease Prediction App

A Machine Learning–powered web application built with **Streamlit** that predicts the likelihood of heart disease based on a patient's health information.

🔗 **Live Demo:** [https://heart-disease-prediction-meccyfr2gqn48ely7fdewd.streamlit.app/](https://heart-disease-prediction-meccyfr2gqn48ely7fdewd.streamlit.app/)

---

## 📋 Overview

This app takes basic patient health parameters (age, blood pressure, cholesterol, chest pain type, etc.) as input and uses a trained **Logistic Regression** model to predict whether the patient is at higher or lower risk of heart disease, along with a probability score.

> ⚠️ **Disclaimer:** This project is built for **educational purposes only** and must not be used as a substitute for professional medical diagnosis or advice.

---

## ✨ Features

- Clean, modern, card-based UI built entirely with Streamlit + custom CSS
- Interactive sliders and dropdowns for entering patient data
- Real-time prediction with probability score
- Visual risk indicator (progress bar + color-coded result card)
- Sidebar with app info and usage instructions

---

## 🗂️ Project Structure

```
HeartDiseases/
│
├── app.py                          # Main Streamlit application
├── logistic_regression_model.pkl   # Trained ML model
├── scaler.pkl                      # Feature scaler used during training
├── column.pkl                      # Expected input columns for the model
├── requirements.txt                # Python dependencies
└── README.md                       # Project documentation
```

---

## 🧠 How It Works

1. User enters patient details (age, sex, chest pain type, blood pressure, cholesterol, etc.)
2. Input is converted into a DataFrame and aligned with the model's expected columns
3. Data is scaled using the saved `scaler.pkl`
4. The trained Logistic Regression model (`logistic_regression_model.pkl`) predicts the outcome
5. The result — risk level and probability — is displayed in a styled result card

---

## 🩺 Input Parameters

| Parameter | Description |
|---|---|
| Age | Patient's age |
| Sex | Male (M) / Female (F) |
| Chest Pain Type | ATA, NAP, TA, ASY |
| Resting Blood Pressure | mm Hg |
| Serum Cholesterol | mg/dl |
| Fasting Blood Sugar | Yes / No (> 120 mg/dl) |
| Resting ECG Results | Normal, ST, LVH |
| Maximum Heart Rate Achieved | bpm |
| Exercise Induced Angina | Yes / No |
| ST Depression (Oldpeak) | Numeric value |
| Slope of Peak Exercise ST Segment | Up, Flat, Down |

---

## ⚙️ Installation & Local Setup

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/heart-disease-prediction.git
cd heart-disease-prediction
```

### 2. Create a virtual environment (optional but recommended)
```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`.

---

## 📦 Requirements

```
streamlit
pandas
scikit-learn
joblib
```

---

## ☁️ Deployment (Streamlit Community Cloud)

1. Push the project (including the `.pkl` files and `requirements.txt`) to a public GitHub repository.
2. Go to [Streamlit Community Cloud](https://streamlit.io/cloud) and sign in with GitHub.
3. Click **Create app → Deploy a public app from GitHub**.
4. Select your repository, branch (`main`), and main file path (`app.py`).
5. Click **Deploy** — you'll get a public link. This project is live at:
   ```
   https://heart-disease-prediction-meccyfr2gqn48ely7fdewd.streamlit.app/
   ```

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** – UI framework
- **scikit-learn** – Machine Learning model & scaling
- **pandas** – Data handling
- **joblib** – Model serialization

---

## 📄 License

This project is open-source and available for educational and learning purposes.

---

## 🙋 Author
Aisha Rajpar Software Engineering Student

Built as a Machine Learning learning project. Contributions and suggestions are welcome!
