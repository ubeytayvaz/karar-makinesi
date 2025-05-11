import streamlit as st
import pandas as pd
from datetime import datetime

# Excel dosyasını oku
@st.cache_data
def load_data():
    df = pd.read_excel("ÖDEME KOŞULLARI_20250129.xlsx", skiprows=4)
    df = df.rename(columns={
        df.columns[0]: "Taksit",
        df.columns[1]: "Tarih",
        df.columns[2]: "Min",
        df.columns[3]: "Tam",
        df.columns[4]: "Max",
        df.columns[5]: "Yüzde"
    })
    df = df.dropna(subset=["Tarih"])  # boş satırları at
    df["Tarih"] = pd.to_datetime(df["Tarih"]).dt.date
    return df

df = load_data()

st.title("📅 Ödeme Bilgisi Tanıma Makinesi")

# Kullanıcıdan giriş al
g_tarih = st.date_input("Ödeme Tarihini Girin")
g_tutar = st.number_input("Ödenen Tutarı Girin (milyon TL)", step=0.1)

if st.button("Taksiti Bul"):
    # En yakın tarihi bul
    df["Tarih Farkı"] = df["Tarih"].apply(lambda x: abs((x - g_tarih).days))
    en_yakin = df.loc[df["Tarih Farkı"].idxmin()]

    # Tutarla en yakın eşleşmeyi bul
    farklar = {
        "Min": abs(g_tutar - en_yakin["Min"]),
        "Tam": abs(g_tutar - en_yakin["Tam"]),
        "Max": abs(g_tutar - en_yakin["Max"])
    }
    en_yakin_kolon = min(farklar, key=farklar.get)

    st.success(f"""
    📌 Tespit Edilen Taksit: {int(en_yakin['Taksit'])}
    📅 Tarih: {en_yakin['Tarih']}
    💰 Uygun Aralık: {en_yakin_kolon} ({en_yakin[en_yakin_kolon]} milyon TL)
    """)

    st.caption("Not: En yakın tarih ve tutara göre eşleştirme yapılmıştır.")

