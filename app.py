import streamlit as st
text = st.text_input("enter a string ")
st.write("Swapcase: ",text.swapcase())