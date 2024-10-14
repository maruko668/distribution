import streamlit as st
import standard_normal
import normal_distribution

# サイドバーにページ選択のメニューを作成
menu = st.sidebar.selectbox("Select a distribution:", ["Standard Normal Distribution", "Normal Distribution"])

# ページごとのコンテンツを表示
if menu == "Standard Normal Distribution":
    standard_normal.show_standard_normal()
elif menu == "Normal Distribution":
    normal_distribution.show_normal_distribution()

# 言語を選択するドロップダウンを右上に配置する
st.sidebar.markdown("### Language Selection")
language = st.sidebar.radio("Choose your language / 言語を選んでください", ("English", "日本語"))

# 英語と日本語に対応したテキストの定義
if language == "English":
    st.title("Welcome to the App")
    st.write("This is an example of a language switcher. Choose a language from the top right.")
    st.write("You can see this content in English now.")
elif language == "日本語":
    st.title("アプリへようこそ")
    st.write("これは言語切り替え機能の例です。右上から言語を選んでください。")
    st.write("現在、このコンテンツは日本語で表示されています。")

# 他のアプリのコンテンツに対しても、言語に基づいてテキストを表示
if language == "English":
    st.write("Here is some more content in English.")
else:
    st.write("ここでは日本語のコンテンツがさらに表示されます。")
