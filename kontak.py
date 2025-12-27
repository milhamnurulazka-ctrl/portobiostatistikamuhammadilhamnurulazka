import streamlit as st

def contact_me():
    st.header("📬 Kontak & Informasi Pengembang")
    st.markdown(
        """
        Halaman ini berisi informasi pengembang dashboard **Diabetes Risk Analysis**.
        Silakan menghubungi saya jika terdapat pertanyaan, masukan, atau kebutuhan
        kerja sama akademik dan pengembangan data kesehatan.
        """
    )

    st.divider()

    col1, col2 = st.columns([4, 6])

    with col1:
        st.image(
            "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
            width=180,
            caption="Data Analyst | Biostatistics"
        )

    with col2:
        st.markdown("""
        ### 👤 Profil Singkat
        **Nama:** Muhammad Ilham Nurul Azka  
        **Bidang:** Statistika • Biostatistika • Data Science Kesehatan  
        **Institusi:** Universitas Muhammadiyah Semarang  

        Dashboard ini dikembangkan sebagai bagian dari:
        - UAS Biostatistika  
        - Project Analisis Data Kesehatan  
        - Portofolio Machine Learning  
        """)

    st.divider()

    st.subheader("📞 Informasi Kontak")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        📧 **Email**  
        [milhamnurulazka@gmail.com](mailto:milhamnurulazka@gmail.com)
        """)

    with c2:
        st.markdown("""
        📱 **WhatsApp**  
        [Chat via WhatsApp](https://wa.me/6285878599921)
        """)

    with c3:
        st.markdown("""
        💻 **GitHub**  
        [github.com/usernamekamu](https://github.com/milhamnurulazka-ctrl/portobiostatistikamuhammadilhamnurulazka.git)
        """)

    st.divider()

    st.info("""
    📌 **Catatan:**  
    Dashboard ini bersifat **edukatif** dan digunakan untuk pembelajaran
    analisis risiko Diabetes Mellitus menggunakan data populasi.
    Tidak dimaksudkan sebagai alat diagnosis medis.
    """)
