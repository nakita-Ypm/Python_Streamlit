# import streamlit as st

# def main():
#     st.title("Pythonだけで作るStreamlitアプリケーション")


# if __name__ == "__main__":
#     main()


import streamlit as st
import requests

# FlaskアプリのベースURL
flask_base_url = "http://flask:3001"

def call_flask_api(endpoint):
    response = requests.get(flask_base_url + endpoint)
    return response.json()

def main():
    st.title("Flask APIを叩くStreamlitアプリ")

    if st.button("Pingを実行"):
        result = call_flask_api("/ping")
        st.json(result)

if __name__ == "__main__":
    main()
