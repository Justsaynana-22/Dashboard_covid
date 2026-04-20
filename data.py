import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    df = pd.read_csv("dataset/covid_19_indonesia_time_series_all.csv")
    return df

def show_data():
    df = load_data()
    
    st.subheader("📌 Data COVID-19 Indonesia")

    # --- BAGIAN FILTER KOLOM ---
    # Mengambil kolom 'Location' DAN rentang dari 'New Cases' sampai 'Total Recovered'
    # Pastikan penulisan nama kolom sesuai persis dengan di file CSV (Case Sensitive)
    try:
        # Membuat list kolom: 'Location' digabung dengan rentang kolom lainnya
        kolom_pilihan = ['Location'] + list(df.loc[:, 'New Cases':'Total Recovered'].columns)
        df_display = df[kolom_pilihan]
        
        st.write("Menampilkan kolom Lokasi dan rentang Kasus Baru hingga Total Sembuh:")
        st.dataframe(df_display.head(10), use_container_width=True)
    except KeyError:
        st.error("Pastikan nama kolom 'Location', 'New Cases', dan 'Total Recovered' sudah benar.")

    # Statistik Deskriptif (otomatis hanya untuk kolom yang dipilih)
    st.subheader("📊 Statistik Deskriptif")
    st.write(df_display.describe())