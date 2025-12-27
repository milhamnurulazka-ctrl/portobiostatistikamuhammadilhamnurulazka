import streamlit as st

st.set_page_config(
    page_title="Diabetes Risk Analysis Dashboard",
    page_icon="🩺",
    layout="wide"
)

st.title("🩺 Diabetes Risk Analysis & Prediction")
st.markdown("""
**Dashboard Biostatistika & Machine Learning**  
Universitas Muhammadiyah Semarang
""")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📘 About Dataset",
    "📊 Dashboard",
    "🧠 Machine Learning",
    "🧪 Prediction",
    "📬 Contact"
])

with tab1:
    import about_page
    about_page.show()

with tab2:
    import visualisasi
    visualisasi.chart()

with tab3:
    import machine_learning
    machine_learning.ml_model()

with tab4:
    import prediction
    prediction.prediction_app()

with tab5:
    from kontak import contact_me
    contact_me()
