import streamlit as st

st.write("Aplikasi Menghitung Kadar Air")

W1=st.number_input("Masukkan nilai bobot sebelum dipanaskan")
W2=st.number_input("Masukkan nilai bobot setelah dipanaskan")
W=st.number_input("Masukkan nilai bobot sampel")

tombol=st.button("Hitung nilai kadar air suatu sampel")

if tombol:
    nilai_kadar_air=(W1-W2)*100/W
    st.success(f"nilai kadar air suatu sampel adalah {nilai_kadar_air}")
