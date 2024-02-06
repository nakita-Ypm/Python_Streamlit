import streamlit as st
import import_path as imp

imp.import_path("components/request")

from components.request import request as req


st.title("Python Streamlit")

if st.button("Pingを実行"):
    result = req.call_flask_api("/ping")
    st.json(result)
