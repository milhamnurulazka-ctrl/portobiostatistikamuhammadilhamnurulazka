import streamlit as st
import pandas as pd
import os
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

def prediction_app():
    st.header("🧪 Prediksi Risiko Diabetes")

    base_dir = os.path.dirname(__file__)
    path = os.path.join(
        base_dir, "data",
        "DiaBD_A Diabetes Dataset for Enhanced Risk Analysis and Research in Bangladesh.csv"
    )

    df = pd.read_csv(path)
    df["diabetic"] = df["diabetic"].map({"Yes": 1, "No": 0})

    X = df[["age", "bmi", "glucose"]]
    y = df["diabetic"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = LogisticRegression()
    model.fit(X_scaled, y)

    age = st.slider("Usia", 18, 90, 40)
    bmi = st.slider("BMI", 10.0, 50.0, 25.0)
    glucose = st.slider("Glucose", 50.0, 300.0, 120.0)

    if st.button("Prediksi Risiko"):
        data = scaler.transform([[age, bmi, glucose]])
        prob = model.predict_proba(data)[0][1]

        st.metric("Probabilitas Diabetes", f"{prob*100:.2f}%")

        if prob >= 0.5:
            st.error("⚠️ Risiko Diabetes Tinggi")
        else:
            st.success("✅ Risiko Diabetes Rendah")

        st.caption("⚠️ Bukan diagnosis medis.")
