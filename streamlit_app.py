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
