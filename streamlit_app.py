import streamlit as st
import standard_normal
import normal_distribution
import f_distribution
import studentized_range_distribution
import t_distribution
import kde_estimation  # カーネル密度推定モジュールを追加

# トップページの作成
def show_top_page():
    st.title("Distribution Calculator App")
    st.write("Welcome to the Distribution Calculator App! You can calculate probabilities and values for different distributions.")
    st.write("分布計算サイトへようこそ! ここでは様々な分布の確率が計算できます。")
    st.write("Please choose a distribution from the sidebar to begin.")
    st.write("左のメニューバーで選択してください。")

    st.subheader("Available Distributions")
    st.write("1. Standard Normal Distribution / 標準正規分布")
    st.write("2. Normal Distribution / 正規分布")
    st.write("3. F Distribution / F分布")
    st.write("4. Studentized Range Distribution / ステューデント化された範囲分布")
    st.write("5. t Distribution / t分布")
    st.write("6. Kernel Density Estimation / カーネル密度推定")

# 言語選択のメニューをサイドバーに追加
st.sidebar.markdown("### 言語選択 / Language Selection")
language = st.sidebar.radio("Choose your language / 言語を選んでください", ("English", "日本語"))

# メインメニューの作成（トップページと各分布計算ページ）
menu = st.sidebar.selectbox(
    "Select a page / ページを選んでください",
    [
        "Home",
        "Standard Normal Distribution / 標準正規分布",
        "Normal Distribution / 正規分布",
        "F Distribution / F分布",
        "Studentized Range Distribution / ステューデント化された範囲分布",
        "t Distribution / t分布",
        "Kernel Density Estimation / カーネル密度推定"
    ]
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
elif menu == "Studentized Range Distribution / ステューデント化された範囲分布":
    studentized_range_distribution.show_studentized_range(language)
elif menu == "t Distribution / t分布":
    t_distribution.show_t_distribution(language)
elif menu == "Kernel Density Estimation / カーネル密度推定":
    kde_estimation.show_kde_estimation()
