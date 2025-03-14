import streamlit as st

st.title("🎈 Aplikasi menghitung luas persegi panjang")
panjang = st.number_input("Masukkan panjang (cm)")
st.write("panjang= ", panjang)
lebar = st.number_input("Masukkan lebar (cm)")
st.write("lebar= ", lebar)
luas=panjang*lebar
st.write("Luas= ", luas)
