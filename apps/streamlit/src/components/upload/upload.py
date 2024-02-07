import streamlit as st


def upload(title, type, decode):
    uploaded_file = st.file_uploader(title, type=[type])

    if uploaded_file is not None:
        res = uploaded_file.getvalue().decode(decode)
        return res
