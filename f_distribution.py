import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import f

def show_f_distribution(language):
    if language == "English":
        st.title("F Distribution")

        # F分布のパラメータの説明を追加
        st.write("""
        The F-distribution is a ratio of two scaled chi-square distributions. It is primarily used to compare variances.
        - **Degrees of freedom for the numerator (dfn)**: This represents the degrees of freedom for the variance estimate in the numerator.
        - **Degrees of freedom for the denominator (dfd)**: This represents the degrees of freedom for the variance estimate in the denominator.
        """)

        # ユーザーから自由度を入力
        dfn = st.number_input('Enter the degrees of freedom for the numerator (dfn):', value=5, min_value=1)
        dfd = st.number_input('Enter the degrees of freedom for the denominator (dfd):', value=10, min_value=1)
        x_value_input = st.text_input('Enter a value for x (F-distribution):', value="")
        p_value_input = st.text_input('Enter a p-value (between 0 and 1):', value="")

        # 初期化
        x_value = None
        p_value = None

        # どちらかが入力されたら計算
        if x_value_input:
            try:
                x_value = float(x_value_input)
                p_value = f.cdf(x_value, dfn, dfd)
            except ValueError:
                st.error("Invalid x-value")

        elif p_value_input:
            try:
                p_value = float(p_value_input)
                if 0 <= p_value <= 1:
                    x_value = f.ppf(p_value, dfn, dfd)
                else:
                    st.error("p-value must be between 0 and 1")
            except ValueError:
                st.error("Invalid p-value")

        # 計算結果の表示
        if x_value is not None and p_value is not None:
            st.write(f"The x-value is: {x_value:.4f}")
            st.write(f"The p-value is: {p_value:.4f}")

            # F分布の図を表示
            x = np.linspace(0, 5, 1000)
            y = f.pdf(x, dfn, dfd)

            # 図のサイズを半分に設定
            fig, ax = plt.subplots(figsize=(5, 3))
            ax.plot(x, y, label=f'F Distribution (dfn={dfn}, dfd={dfd})')
            ax.fill_between(x, 0, y, where=(x <= x_value), color='blue', alpha=0.3)
            ax.axvline(x=x_value, color='red', linestyle='--')

            st.pyplot(fig)

    elif language == "日本語":
        st.title("F分布")

        # F分布のパラメータの説明を追加（日本語）
        st.write("""
        F分布は、2つのスケールされたカイ二乗分布の比率に基づく分布です。主に分散の比較に使用されます。
        - **分子の自由度 (dfn)**: 分子における分散の推定に関連する自由度です。
        - **分母の自由度 (dfd)**: 分母における分散の推定に関連する自由度です。
        """)

        # ユーザーから自由度を入力
        dfn = st.number_input('分子の自由度 (dfn) を入力してください:', value=5, min_value=1)
        dfd = st.number_input('分母の自由度 (dfd) を入力してください:', value=10, min_value=1)
        x_value_input = st.text_input('x値を入力してください（F分布）:', value="")
        p_value_input = st.text_input('p値を入力してください（0から1の間）:', value="")

        # 初期化
        x_value = None
