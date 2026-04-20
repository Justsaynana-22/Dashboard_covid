import streamlit as st
from data import *

# Judul dashboard
def judul():
    st.title("Dashboard COVID-19")
    st.write("📊 Selamat Datang di Dashboard Interaktif untuk Menganalisis Data COVID-19 di Indonesia")

# Fungsi Footer dengan Nama dan NPM
def footer():
    st.markdown(
        """
        <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #000000;
            color: #6c757d; /* Warna abu-abu yang soft */
            text-align: center;
            padding: 10px;
            font-size: 12px;
            z-index: 100;
        }
        </style>
        <div class="footer">
            <hr style="margin-bottom: 5px;">
            <p>© 2026 Dashboard COVID-19 | <b>Rina Helmina</b> | NPM: <b>184240011</b></p>
        </div>
        """,
        unsafe_allow_html=True
    )

# Sidebar Navigasi
st.sidebar.title("Navigasi")
menu = st.sidebar.radio("Pilih Halaman", ["Home", "Halaman Data"])

# Logika Halaman
if menu == "Home":
    judul()
elif menu == "Halaman Data":
    judul()
    show_data()

# Panggil footer di baris paling bawah agar selalu muncul
footer()