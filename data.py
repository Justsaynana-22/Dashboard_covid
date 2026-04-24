import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data():
    # Pastikan file path benar
    df = pd.read_csv("dataset/covid_19_indonesia_time_series_all.csv")
    # Konversi kolom Date ke tipe datetime agar filtering lebih akurat
    df['Date'] = pd.to_datetime(df['Date'])
    return df

def filter_data(df, year=None):
    if year:
        # Menggunakan .dt.year karena kolom sudah bertipe datetime
        return df[df["Date"].dt.year == year]
    return df  # Kembalikan df asli jika year adalah None

def select_year():
    return st.sidebar.selectbox(
        "Pilih Tahun 📅",
        options=[None, 2020, 2021, 2022],
        format_func=lambda x: "Semua Tahun" if x is None else str(x)
    )

def show_data(df):
    # Validasi jika df kosong setelah difilter
    if df.empty:
        st.warning("Data tidak tersedia untuk filter tersebut.")
        return
        
    selected_columns = ['Location'] + list(df.loc[:, 'New Cases':'Total Recovered'].columns)
    df_selected = df[selected_columns]
    st.subheader("Data Covid-19 Indonesia 🔴⚪")
    st.dataframe(df_selected.head(10))

# Fungsi untuk perhitungan (tetap sama, namun sebaiknya handle angka besar)
def total_case(df):
    return df['Total Cases'].sum()

def total_death(df):
    return df['Total Deaths'].sum()

def total_recovery(df):
    return df['Total Recovered'].sum()

def kolom(df):
    kasus = total_case(df)
    kematian = total_death(df)
    sembuh = total_recovery(df)

    col1, col2, col3 = st.columns(3)
    # Gunakan format ribuan agar lebih enak dibaca
    col1.metric(label="Total Kasus 📈", value=f"{kasus:,}", border=True)
    col2.metric(label="Total Kematian 💀", value=f"{kematian:,}", border=True)
    col3.metric(label="Total Sembuh 🏋️", value=f"{sembuh:,}", border=True)

def pie_chart1(df):
    total_mati = total_death(df)
    total_sembuh = total_recovery(df)

    data={
        'Status' : ['Meninggal', 'Sembuh'],
        'Jumlah' : [total_mati, total_sembuh]
    }

    fig = px.pie(
        data,
        names='Status',
        values='Jumlah',
        title='Perbandingan Total Kematian VS Total Kesembuhan',
        hole=0.5,
        color_discrete_sequence=['#4de89f', '#ff6459']
    )

    st.plotly_chart(fig, use_container_width=True)