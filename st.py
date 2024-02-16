import streamlit as st

st.title("This is a test UI")

user_name = st.text_input("Enter your user name: ")

if st.button("Hello"):
    st.write((f"hello, {user_name}"))

    














