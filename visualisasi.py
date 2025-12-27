import streamlit as st
import pandas as pd
import plotly.express as px
import os
from scipy.stats import ttest_ind

def chart():
    st.header("📊 Statistik Deskriptif & Eksplorasi Data")

    base_dir = os.path.dirname(__file__)
    path = os.path.join(
        base_dir, "data",
        "DiaBD_A Diabetes Dataset for Enhanced Risk Analysis and Research in Bangladesh.csv"
    )

    df = pd.read_csv(path)

    # Konversi target
    df["diabetic"] = df["diabetic"].map({"Yes": 1, "No": 0})

    st.subheader("📌 Ringkasan Dataset")
    col1, col2, col3 = st.columns(3)
    col1.metric("Jumlah Sampel", df.shape[0])
    col2.metric("Prevalensi Diabetes", f"{df['diabetic'].mean()*100:.1f}%")
    col3.metric("Rata-rata BMI", f"{df['bmi'].mean():.2f}")

    st.divider()

    st.subheader("📈 Visualisasi Utama")

    fig1 = px.histogram(df, x="diabetic", color="diabetic",
                        title="Distribusi Status Diabetes")
    st.plotly_chart(fig1, use_container_width=True)

    fig2 = px.box(df, x="diabetic", y="age",
                  title="Usia berdasarkan Status Diabetes")
    st.plotly_chart(fig2, use_container_width=True)

    fig3 = px.box(df, x="diabetic", y="bmi",
                  title="BMI berdasarkan Status Diabetes")
    st.plotly_chart(fig3, use_container_width=True)

    st.divider()

    st.subheader("🧪 Uji Statistik (t-test)")

    age_d = df[df.diabetic == 1]["age"]
    age_nd = df[df.diabetic == 0]["age"]
    _, p_age = ttest_ind(age_d, age_nd)

    bmi_d = df[df.diabetic == 1]["bmi"]
    bmi_nd = df[df.diabetic == 0]["bmi"]
    _, p_bmi = ttest_ind(bmi_d, bmi_nd)

    st.markdown(f"""
    **Hasil Uji t-test:**
    - Usia → p-value = `{p_age:.4f}`
    - BMI → p-value = `{p_bmi:.4f}`

    📌 *p-value < 0.05 menunjukkan perbedaan signifikan secara statistik.*
    """)
