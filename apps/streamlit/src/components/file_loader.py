import streamlit as st
import xml.etree.ElementTree as ET


def apply(st):
    st.title("XML Reader App")

    # ファイルのアップロード
    uploaded_file = st.file_uploader(
        "XMLファイルをアップロードしてください", type=["xml"]
    )

    if uploaded_file is not None:
        st.success("ファイルがアップロードされました!")

        # アップロードされたXMLファイルの内容を表示
        content = uploaded_file.read()
        st.code(content, language="xml")

        # XMLファイルを解析して要素ツリーを取得
        root = read_xml(uploaded_file)

        # 要素ツリーの情報を表示
        st.subheader("XMLファイルの要素ツリー:")
        st.write(root)

        # ここで必要な追加の処理を行うことができます


def read_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    return root
