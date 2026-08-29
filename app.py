import streamlit as st

st.title("🔄 Swapcase Tool")
st.write("Convert uppercase letters to lowercase and lowercase letters to uppercase.")

text = st.text_input("enter string  whatever you want ")
st.write("Result:", text.swapcase())