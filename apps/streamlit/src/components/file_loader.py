def apply(st):

    # URLパスによるページの切り替え
    page = st.sidebar.selectbox("Choose a page", ["Home", "About", "Contact"])

    if page == "Home":
        st.title("Home Page")
        # ここにHomeページのコンテンツを追加する
    elif page == "About":
        st.title("About Page")
        # ここにAboutページのコンテンツを追加する
    elif page == "Contact":
        st.title("Contact Page")
        # ここにContactページのコンテンツを追加する
