import streamlit as st
import random

st.title("Bugünkü Karar Makinesi 🎱")
st.write("Aklında bir soru tut ve butona bas...")

if st.button("Bana bir işaret ver!"):
    yanitlar = [
        "Kesinlikle EVET ✅",
        "Hayır, unut gitsin ❌",
        "Belki, emin değilim 🤔",
        "Şansını denemelisin 🎲",
        "Zamanı değil ⏳",
        "Evet ama dikkatli ol 🕵️‍♂️"
    ]
    st.success(random.choice(yanitlar))