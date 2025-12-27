import streamlit as st

def show():
    st.header("🩺 Diabetes Risk Analysis Dashboard")

    st.markdown("""
    ### 📌 Executive Summary
    Dashboard ini dikembangkan untuk menganalisis faktor risiko **Diabetes Mellitus**
    menggunakan pendekatan **Biostatistika dan Machine Learning** berbasis
    **Regresi Logistik**.

    **Dataset:** Bangladesh Diabetes Dataset  
    **Metode utama:** Statistik deskriptif, uji hipotesis, Regresi Logistik  
    **Tujuan:** Identifikasi faktor risiko & prediksi Diabetes  

    ---
    """)

    col1, col2 = st.columns([4, 6])

    with col1:
        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/3/3a/InsulinPump.jpg",
            caption="Diabetes Mellitus",
            use_container_width=True
        )

    with col2:
        st.markdown("""
        **Diabetes Mellitus** adalah penyakit kronis yang ditandai dengan
        meningkatnya kadar glukosa darah akibat gangguan insulin.

        Penyakit ini berkontribusi besar terhadap:
        - Penyakit jantung
        - Stroke
        - Gagal ginjal
        - Penurunan kualitas hidup

        Dashboard ini bersifat **edukatif & analitis**, bukan diagnosis medis.
        """)

    st.subheader("🎯 Tujuan Analisis")
    st.markdown("""
    1. Menyajikan statistik deskriptif data Diabetes  
    2. Menguji perbedaan karakteristik pasien diabetes dan non-diabetes  
    3. Membangun model prediksi berbasis Regresi Logistik  
    4. Menyediakan simulasi prediksi risiko Diabetes  
    """)
