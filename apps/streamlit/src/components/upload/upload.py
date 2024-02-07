import streamlit as st


def upload(title, type):
    uploaded_file = st.file_uploader(title, type=[type])

    if uploaded_file is not None:
        res = uploaded_file.getvalue().decode("utf-8")
        return res
