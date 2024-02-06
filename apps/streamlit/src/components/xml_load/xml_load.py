import streamlit as st
import xml.etree.ElementTree as ET


def apply():
    # ファイルのアップロード
    uploaded_file = st.file_uploader("XMLファイルを選択してください", type=["xml"])

    if uploaded_file is not None:
        # XMLファイルの解析
        tree = ET.parse(uploaded_file)
        root = tree.getroot()

        # XMLの内容を表示
        st.write("XMLファイルの内容:")
        st.write(ET.tostring(root, encoding="unicode", method="xml"))
