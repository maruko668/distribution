import streamlit as st
import standard_normal
import normal_distribution
import f_distribution  # F分布用のモジュールを追加

# トップページの作成
def show_top_page():
    st.title("Distribution Calculator App")
    st.write("Welcome to the Distribution Calculator App! You can calculate probabilities and values for different distributions.")
    st.write("Please choose a distribution from the sidebar to begin.")

    st.subheader("Available Distributions")
    st.write("1. Standard Normal Distribution (標準正規分布)")
    st.write("2. Normal Distribution (正規分布)")
    st.write("3. F Distribution (F分布)")

    st.write("Use the sidebar to select a distribution and start calculating.")

# 言語選択のメニューをサイドバーに追加
st.sidebar.markdown("### 言語選択 / Language Selection")
language = st.sidebar.radio("Choose your language / 言語を選んでください", ("English", "日本語"))

# メインメニューの作成（トップページと各分布計算ページ）
menu = st.sidebar.selectbox(
    "Select a page / ページを選んでください",
    ["Home", "Standard Normal Distribution / 標準正規分布", "Normal Distribution / 正規分布", "F Distribution / F分布"]
)

# メニューに基づいてページを切り替え
if menu == "Home":
    show_top_page()
elif menu == "Standard Normal Distribution / 標準正規分布":
    standard_normal.show_standard_normal(language)
elif menu == "Normal Distribution / 正規分布":
    normal_distribution.show_normal_distribution(language)
elif menu == "F Distribution / F分布":
    f_distribution.show_f_distribution(language)
