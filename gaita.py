import streamlit as st

st.write("Aplikasi Menghitung Kadar Air")

W1=st.number_input("masukkan nilai bobot sebelum dipanaskan")
W2=st.number_input("masukkan nilai bobot setelah dipanaskan")
W=st.number_input("masukkan nilai bobot sampel")

tombol=st.button("hitung nilai kadar air suatu sampel")

if tombol:
    nilai_kadar_air=(W1-W2)*100/W
    st.success(f"nilai kadar air suatu sampel adalah {nilai_kadar_air}")
