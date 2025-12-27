import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

def ml_model():
    st.header("🧠 Regresi Logistik Diabetes")

    base_dir = os.path.dirname(__file__)
    path = os.path.join(
        base_dir, "data",
        "DiaBD_A Diabetes Dataset for Enhanced Risk Analysis and Research in Bangladesh.csv"
    )

    df = pd.read_csv(path)
    df["diabetic"] = df["diabetic"].map({"Yes": 1, "No": 0})
    df["gender"] = df["gender"].map({"Male": 1, "Female": 0})

    features = [
        "age", "bmi", "glucose",
        "systolic_bp", "diastolic_bp",
        "family_diabetes", "hypertensive"
    ]

    X = df[features]
    y = df["diabetic"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42
    )

    model = LogisticRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    st.metric("Accuracy", f"{accuracy_score(y_test, y_pred)*100:.2f}%")

    cm = confusion_matrix(y_test, y_pred)
    fig, ax = plt.subplots()
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", ax=ax)
    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")
    st.pyplot(fig)

    st.markdown("""
    **Interpretasi:**
    - Model menggunakan variabel klinis utama
    - Confusion matrix menunjukkan performa klasifikasi
    - Cocok untuk analisis risiko Diabetes berbasis populasi
    """)
