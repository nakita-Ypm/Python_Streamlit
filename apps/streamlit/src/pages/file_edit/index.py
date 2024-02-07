import streamlit as st
import import_path as imp

imp.import_path("components/upload")
from components.upload import upload as up
from components.request import post


def apply(req):
    st.title(req["title"])

    uploaded_file = up.upload(req["upload_title"], req["type"], req["decode"])

    if uploaded_file is not None:
        push_button(req, uploaded_file)


def push_button(req, uploaded_file):
    if st.button(req["button"]):
        res = post.post_file(req["api_endpoint"], req["flie_type"], uploaded_file)
        st.text(res.text)
