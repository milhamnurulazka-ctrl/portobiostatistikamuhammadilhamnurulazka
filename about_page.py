import streamlit as st

def show():
    st.header("🩺 Diabetes Risk Analysis Dashboard")

    # =========================
    # Executive Summary
    # =========================
    st.markdown("""
    ### 📌 Executive Summary
    Dashboard ini dikembangkan untuk menganalisis faktor risiko **Diabetes Mellitus**
    menggunakan pendekatan **Biostatistika dan Machine Learning** berbasis
    **Regresi Logistik**. Analisis dilakukan menggunakan data individu yang
    merepresentasikan karakteristik demografis, indikator fisiologis, status
    antropometri, serta faktor risiko kardiometabolik.

    **Dataset:** Bangladesh Diabetes Dataset  
    **Metode utama:** Statistik deskriptif, statistik inferensial, Regresi Logistik  
    **Variabel target:** Status diabetes (Yes dan No)  

    ---
    """)

    # =========================
    # Layout Konten Utama
    # =========================
    col1, col2 = st.columns([4, 6])

    with col1:
        st.image(
            "https://static.republika.co.id/uploads/member/images/news/251118091145-643.jpg",
            caption="Ilustrasi Pemeriksaan Glukosa Darah",
            use_container_width=True
        )

    with col2:
        st.markdown("""
        **Diabetes Mellitus** dianalisis menggunakan data individu yang memuat
        variabel usia, jenis kelamin, indikator vital, status antropometri,
        serta riwayat penyakit terkait metabolik dan kardiovaskular.
        Status **diabetic** digunakan sebagai variabel keluaran biner
        untuk mengklasifikasikan individu diabetes dan non-diabetes.

        Faktor demografis terdiri dari **usia (age)** dan **jenis kelamin (gender)**.
        Risiko gangguan metabolik cenderung meningkat seiring bertambahnya usia.
        Perbedaan fisiologis antar jenis kelamin turut memengaruhi regulasi
        glukosa darah.

        Indikator fisiologis meliputi **denyut nadi (pulse_rate)**,
        **tekanan darah sistolik (systolic_bp)**, dan
        **tekanan darah diastolik (diastolic_bp)**.
        Tekanan darah tinggi berkaitan dengan resistensi insulin dan
        peningkatan risiko diabetes tipe 2.

        Variabel **glucose** merepresentasikan kadar glukosa darah dan
        menjadi indikator klinis utama dalam penentuan status diabetes.
        Peningkatan kadar glukosa berkontribusi langsung terhadap
        probabilitas kejadian diabetes.

        Status antropometri diukur melalui **tinggi badan (height)**,
        **berat badan (weight)**, dan **Body Mass Index (BMI)**.
        BMI digunakan sebagai indikator obesitas yang berperan penting
        dalam gangguan sensitivitas insulin.

        Faktor genetik dan komorbiditas direpresentasikan melalui variabel biner,
        yaitu **family_diabetes**, **hypertension**, **family_hypertension**,
        **cardiovascular**, dan **stroke**.
        Kombinasi faktor-faktor ini mencerminkan akumulasi risiko
        kesehatan individu secara menyeluruh.

        Estimasi risiko dilakukan menggunakan **Regresi Logistik**
        untuk menghitung probabilitas kejadian diabetes berdasarkan
        seluruh variabel prediktor yang tersedia.

        Dashboard ini bersifat **analitis dan prediktif**.
        Seluruh hasil tidak digunakan sebagai dasar diagnosis medis.
        """)

    # =========================
    # Tujuan Analisis
    # =========================
    st.subheader("🎯 Tujuan Analisis")
    st.markdown("""
    Analisis ini bertujuan untuk memberikan pemahaman komprehensif mengenai
    faktor risiko Diabetes Mellitus berbasis data individu.
    Tujuan analisis meliputi:

    1. Mendeskripsikan karakteristik demografis responden berdasarkan usia
       dan jenis kelamin untuk memahami struktur populasi data.

    2. Menganalisis distribusi indikator fisiologis, yaitu denyut nadi,
       tekanan darah sistolik, dan tekanan darah diastolik, sebagai gambaran
       kondisi kardiovaskular individu.

    3. Mengevaluasi kadar glukosa darah sebagai indikator klinis utama
       yang berperan langsung dalam klasifikasi status diabetes.

    4. Mengkaji status antropometri melalui tinggi badan, berat badan,
       dan Body Mass Index (BMI) untuk menilai pengaruh obesitas terhadap
       risiko diabetes.

    5. Mengidentifikasi kontribusi faktor genetik dan komorbiditas,
       meliputi riwayat diabetes keluarga, hipertensi, riwayat hipertensi
       keluarga, penyakit kardiovaskular, dan stroke.

    6. Menguji perbedaan karakteristik antara kelompok diabetes dan
       non-diabetes menggunakan pendekatan statistik inferensial.

    7. Membangun model Regresi Logistik untuk mengestimasi hubungan antara
       faktor risiko dan probabilitas kejadian Diabetes Mellitus.

    8. Menginterpretasikan pengaruh setiap variabel prediktor berdasarkan
       estimasi peluang dari model regresi.

    9. Menyediakan simulasi prediksi risiko diabetes pada tingkat individu
       sebagai bentuk penerapan model secara praktis.

    10. Menyajikan hasil analisis melalui visualisasi interaktif untuk
        meningkatkan pemahaman pengguna terhadap pola risiko diabetes.
    """)

    # =========================
    # Referensi
    # =========================
    st.subheader("📚 Referensi Ilmiah")
    st.markdown("""
    1. World Health Organization. (2023). *Diabetes*. WHO Fact Sheets.  
    2. International Diabetes Federation. (2023). *IDF Diabetes Atlas* (10th Edition).  
    3. American Diabetes Association. (2024). *Standards of Care in Diabetes*. Diabetes Care.  
    4. Khan, M. A., et al. (2022). Risk factor analysis of diabetes using logistic regression. *BMC Public Health*, 22.  
    5. Hosmer, D. W., Lemeshow, S., Sturdivant, R. X. (2021). *Applied Logistic Regression*. Wiley.
    """)

# Jalankan fungsi
show()
