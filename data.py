import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data():
    df = pd.read_csv("dataset/covid_19_indonesia_time_series_all.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    # Pastikan data terurut berdasarkan tanggal agar filter/pengambilan data terakhir akurat
    df = df.sort_values('Date')
    return df

def filter_data(df, year=None):
    if year:
        return df[df["Date"].dt.year == year]
    return df

def select_year():
    return st.sidebar.selectbox(
        "Pilih Tahun 📅",
        options=[None, 2020, 2021, 2022],
        index=0, # Default ke 'Semua Tahun'
        format_func=lambda x: "Semua Tahun" if x is None else str(x)
    )

def show_data(df):
    if df.empty:
        st.warning("Data tidak tersedia untuk filter tersebut.")
        return
        
    st.subheader("Sampel Data Covid-19 Indonesia 🔴⚪")
    # Mengambil kolom secara spesifik lebih aman daripada slicing [:]
    cols = ['Date', 'Location', 'New Cases', 'Total Cases', 'Total Deaths', 'Total Recovered']
    available_cols = [c for c in cols if c in df.columns]
    st.dataframe(df[available_cols].tail(10)) # Menampilkan data terbaru di bawah

def kolom(df):
    # Menggunakan .max() karena data bersifat akumulatif per lokasi
    # Jika ingin total nasional, pastikan memfilter Location == 'Indonesia' terlebih dahulu
    df_nasional = df[df['Location'] == 'Indonesia']
    
    kasus = df_nasional['Total Cases'].max()
    kematian = df_nasional['Total Deaths'].max()
    sembuh = df_nasional['Total Recovered'].max()

    col1, col2, col3 = st.columns(3)
    col1.metric(label="Total Kasus 📈", value=f"{kasus:,.0f}", border=True)
    col2.metric(label="Total Kematian 💀", value=f"{kematian:,.0f}", border=True)
    col3.metric(label="Total Sembuh 🏋️", value=f"{sembuh:,.0f}", border=True)

def pie_chart1(df):
    df_nasional = df[df['Location'] == 'Indonesia']
    total_mati = df_nasional['Total Deaths'].max()
    total_sembuh = df_nasional['Total Recovered'].max()

    data = {
        'Status': ['Meninggal', 'Sembuh'],
        'Jumlah': [total_mati, total_sembuh]
    }

    fig = px.pie(
        data,
        names='Status',
        values='Jumlah',
        title='Perbandingan Total Kematian vs Kesembuhan',
        hole=0.5,
        # Merah untuk Meninggal, Hijau untuk Sembuh
        color_discrete_map={'Meninggal': '#ff6459', 'Sembuh': '#4de89f'} 
    )

    st.plotly_chart(fig, use_container_width=True)