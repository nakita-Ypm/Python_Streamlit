import streamlit as st
import xml.etree.ElementTree as ET

def read_xml(content):
    tree = ET.fromstring(content)
    return tree

st.title("XML Reader App")

# ファイルのアップロード
uploaded_file = st.file_uploader("XMLファイルをアップロードしてください", type=["xml"])

if uploaded_file is not None:
    st.success("ファイルがアップロードされました!")

    # アップロードされたXMLファイルの内容を表示
    content = uploaded_file.read()

    # XMLファイルを解析して要素ツリーを取得
    root = read_xml(content)

    # 要素ツリーの情報を表示
    st.subheader("XMLファイルの要素ツリー:")
    st.write(root)

    # ここで必要な追加の処理を行うことができます
    # 例: 特定の要素を検索して情報を表示するなど
