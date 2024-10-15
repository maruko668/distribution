import streamlit as st
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

# 自由度とp値からt値を求める関数
def p_to_t(df, p_value):
    """
    自由度 (df) と p値 から t値 を求める (t-distribution).
    
    Parameters:
    df (int): 自由度
    p_value (float): p値
    
    Returns:
    float: 対応する t値
    """
    try:
        t_value = stats.t.ppf(1 - p_value / 2, df)
        return t_value
    except Exception as e:
        return str(e)

# 自由度とt値からp値を求める関数
def t_to_p(df, t_value):
    """
    自由度 (df) と t値 から p値 を求める (t-distribution).
    
    Parameters:
    df (int): 自由度
    t_value (float): t値
    
    Returns:
    float: 対応する p値
    """
    try:
        p_value = 2 * (1 - stats.t.cdf(abs(t_value), df))
        return p_value
    except Exception as e:
        return str(e)

# 図を描画する関数
def plot_t_distribution(df, t_value):
    x = np.linspace(-5, 5, 500)  # x軸の範囲
    y = stats.t.pdf(x, df)  # 確率密度関数 (PDF)
    
    # 図の作成
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.plot(x, y, label=f"t-Distribution PDF (df={df})")
    
    # t_valueが存在すれば、その位置に線を引く
    if t_value is not None:
        ax.axvline(x=t_value, color='red', linestyle='--', label=f"t = {t_value:.2f}")
    
    ax.set_title("t-Distribution")
    ax.set_xlabel("t")
    ax.set_ylabel("Probability Density")
    ax.legend()
    
    return fig

# Streamlitでt分布のページを作成
def show_t_distribution(language):
    if language == "English":
        st.title("t-Distribution Calculator")

        st.write("""
        The t-distribution is used to estimate population parameters when the sample size is small and/or population variance is unknown.
        You can input either p-value or t-value, and the corresponding result will be automatically calculated.
        """)

        # 自由度の入力
        df = st.number_input("Enter the degrees of freedom (df):", min_value=1, value=10)

        # p値またはt値の入力（どちらかが入力されると計算）
        p_value_input = st.text_input("Enter the p-value (between 0 and 1):", value="")
        t_value_input = st.text_input("Enter the t-value:", value="")

        # 初期化
        t_value = None
        p_value = None

        # p値が入力された場合
        if p_value_input:
            try:
                p_value = float(p_value_input)
                t_value = p_to_t(df, p_value)
            except ValueError:
                st.error("Invalid p-value")

        # t値が入力された場合
        elif t_value_input:
            try:
                t_value = float(t_value_input)
                p_value = t_to_p(df, t_value)
            except ValueError:
                st.error("Invalid t-value")

        # 計算結果の表示
        if t_value is not None and p_value is not None:
            st.write(f"The t-value is: {t_value:.4f}")
            st.write(f"The p-value is: {p_value:.4f}")

            # 図の描画
            fig = plot_t_distribution(df, t_value)
            st.pyplot(fig)

    elif language == "日本語":
        st.title("t分布の計算")

        st.write("""
        t分布は、標本サイズが小さく、母集団の分散が不明な場合に母集団のパラメータを推定するために使用されます。
        p値またはt値のいずれかを入力すれば、対応する結果が自動的に計算されます。
        """)

        # 自由度の入力
        df = st.number_input("自由度 (df) を入力してください:", min_value=1, value=10)

        # p値またはt値の入力（どちらかが入力されると計算）
        p_value_input = st.text_input("p値を入力してください (0から1の間):", value="")
        t_value_input = st.text_input("t値を入力してください:", value="")

        # 初期化
        t_value = None
        p_value = None

        # p値が入力された場合
        if p_value_input:
            try:
                p_value = float(p_value_input)
                t_value = p_to_t(df, p_value)
            except ValueError:
                st.error("無効な p 値です")

        # t値が入力された場合
        elif t_value_input:
            try:
                t_value = float(t_value_input)
                p_value = t_to_p(df, t_value)
            except ValueError:
                st.error("無効な t 値です")

        # 計算結果の表示
        if t_value is not None and p_value is not None:
            st.write(f"t値は: {t_value:.4f}")
            st.write(f"p値は: {p_value:.4f}")

            # 図の描画
            fig = plot_t_distribution(df, t_value)
            st.pyplot(fig)
