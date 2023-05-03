import streamlit as st

st.header(':blue[ini adalah aplikasi kalkulator penjumblahan]')
st.subheader('silahkan masukkan angka yang ingin dihitung :sunglasses:')
number1 =st.number_input('masukkan angka 1')
st.write(f'angka pertama adalah {number1}')

number2 =st.number_input('masukkan angka 2')
st.write(f'angka kedua adalah {number2}')

if st.button ('hitung :sunglasses:'):
	hasil = number1+number2
	st.success(f'hasil penjumblahan {number1} +{number2} = {hasil}')
else:
	st.write('goblok lu ngitung aja pakek ginian')