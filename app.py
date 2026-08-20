import streamlit as st
st.markdown("<style>#MainMenu, footer {visibility: hidden;}</style>", unsafe_allow_html=True)
text = st.text_input("Enter a string")
st.write("Swapcase:", text.swapcase())