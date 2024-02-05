import pandas as pd


def apply(st):
    # タイトルの追加
    st.title("ファイルアップロードのデモ")

    # ファイルのアップロード
    uploaded_file = st.file_uploader(
        "CSVファイルをアップロードしてください", type=["csv"]
    )

    # アップロードされたファイルがある場合
    if uploaded_file is not None:
        # アップロードされたファイルをデータフレームに読み込み
        data = pd.read_csv(uploaded_file)

        # 読み込まれたデータの表示
        st.write("アップロードされたデータ:", data)
    else:
        st.write("ファイルはまだアップロードされていません。")

    # # URLパスによるページの切り替え
    # page = st.sidebar.selectbox("Choose a page", ["Home", "About", "Contact"])

    # if page == "Home":
    #     st.title("Home Page")
    #     # ここにHomeページのコンテンツを追加する
    # elif page == "About":
    #     st.title("About Page")
    #     # ここにAboutページのコンテンツを追加する
    # elif page == "Contact":
    #     st.title("Contact Page")
    #     # ここにContactページのコンテンツを追加する
