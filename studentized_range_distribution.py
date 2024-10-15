import streamlit as st
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

# 自由度とp値からx値を求める関数
def p_to_x(groups, total_data, p_value):
    dfn = groups  # グループ数
    dfd = total_data - groups  # 全体のデータ数 - グループ数
    try:
        x_value = stats.studentized_range.ppf(p_value, dfn, dfd)
        return x_value
    except Exception as e:
        return str(e)

# 自由度とx値からp値を求める関数
def x_to_p(groups, total_data, x_value):
    dfn = groups  # グループ数
    dfd = total_data - groups  # 全体のデータ数 - グループ数
    try:
        p_value = stats.studentized_range.cdf(x_value, dfn, dfd)
        return p_value
    except Exception as e:
        return str(e)

# 図を描画する関数
def plot_studentized_range(groups, total_data, x_value):
    dfn = groups
    dfd = total_data - groups
    x = np.linspace(0, 10, 500)  # x軸の範囲
    y = stats.studentized_range.pdf(x, dfn, dfd)  # 確率密度関数 (PDF)
    
    # 図の作成
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.plot(x, y, label=f"Studentized Range PDF (groups={dfn}, data={dfd})")
    
    # x_valueが存在すれば、その位置に線を引く
    if x_value is not None:
        ax.axvline(x=x_value, color='red', linestyle='--', label=f"x = {x_value:.2f}")
    
    ax.set_title("Studentized Range Distribution")
    ax.set_xlabel("x")
    ax.set_ylabel("Probability Density")
    ax.legend()
    
    return fig

# Streamlitでステューデント化された範囲分布のページを作成
def show_studentized_range(language):
    if language == "English":
        st.title("Studentized Range Distribution Calculator")

        st.write("""
        The studentized range distribution is used for multiple comparisons in statistics. It is used in the Tukey HSD test.
        You can input either p-value or x-value, and the corresponding result will be automatically calculated.
        """)

        # グループ数と全体のデータ数の入力
        groups = st.number_input("Enter the number of groups:", min_value=2, value=3)
        total_data = st.number_input("Enter the total number of data points:", min_value=groups + 1, value=10)

        # p値またはx値の入力（どちらかが入力されると計算）
        p_value_input = st.text_input("Enter the p-value (between 0 and 1):", value="")
        x_value_input = st.text_input("Enter the x-value:", value="")

        # 初期化
        x_value = None
        p_value = None

        # p値が入力された場合
        if p_value_input:
            try:
                p_value = float(1-p_value_input)
                x_value = p_to_x(groups, total_data, p_value)
            except ValueError:
                st.error("Invalid p-value")

        # x値が入力された場合
        elif x_value_input:
            try:
                x_value = float(x_value_input)
                p_value = x_to_p(groups, total_data, x_value)
            except ValueError:
                st.error("Invalid x-value")

        # 計算結果の表示
        if x_value is not None and p_value is not None:
            st.write(f"The x-value is: {x_value:.4f}")
            st.write(f"The p-value is: {p_value:.4f}")

            # 図の描画
            fig = plot_studentized_range(groups, total_data, x_value)
            st.pyplot(fig)

    elif language == "日本語":
        st.title("ステューデント化された範囲分布の計算")

        st.write("""
        ステューデント化された範囲分布は、統計における多重比較に使用され、特にテューキーのHSD検定で使用されます。
        p値またはx値のいずれかを入力すれば、対応する結果が自動的に計算されます。
        """)

        # グループ数と全体のデータ数の入力
        groups = st.number_input("グループ数を入力してください:", min_value=2, value=3)
        total_data = st.number_input("全体のデータ数を入力してください:", min_value=groups + 1, value=10)

        # p値またはx値の入力（どちらかが入力されると計算）
        p_value_input = st.text_input("p値を入力してください (0から1の間):", value="")
        x_value_input = st.text_input("x値を入力してください:", value="")

        # 初期化
        x_value = None
        p_value = None

        # p値が入力された場合
        if p_value_input:
            try:
                p_value = float(1-p_value_input)
                x_value = p_to_x(groups, total_data, p_value)
            except ValueError:
                st.error("無効な p 値です")

        # x値が入力された場合
        elif x_value_input:
            try:
                x_value = float(x_value_input)
                p_value = x_to_p(groups, total_data, x_value)
            except ValueError:
                st.error("無効な x 値です")

        # 計算結果の表示
        if x_value is not None and p_value is not None:
            st.write(f"x値は: {x_value:.4f}")
            st.write(f"p値は: {p_value:.4f}")

            # 図の描画
            fig = plot_studentized_range(groups, total_data, x_value)
            st.pyplot(fig)
