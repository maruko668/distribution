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
    
# 言語選択のメニューをサイドバーに追加
st.sidebar.markdown("### 言語選択 / Language Selection")
language = st.sidebar.radio("Choose your language / 言語を選んでください", ("English", "日本語"))

# メインメニューとして表示するオプション
menu = st.sidebar.selectbox(
    "Select a distribution / 分布を選んでください",
    ["Standard Normal Distribution / 標準正規分布", "Normal Distribution / 正規分布"]
)

# メニューと選択された言語に基づいて表示を切り替え
if menu == "Standard Normal Distribution / 標準正規分布":
    if language == "English":
        standard_normal.show_standard_normal()
    elif language == "日本語":
        standard_normal.show_standard_normal()

elif menu == "Normal Distribution / 正規分布":
    if language == "English":
        normal_distribution.show_normal_distribution()
    elif language == "日本語":
        normal_distribution.show_normal_distribution()
