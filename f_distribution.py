import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import f
import japanize_matplotlib

def show_f_distribution(language):
    if language == "English":
        st.title("F Distribution")

        st.write("""
        The probability density function (PDF) for the F-distribution is given by the formula:

        $$
        f(x; dfn, dfd) = \\frac{(dfn/dfd)^{dfn/2} \cdot x^{dfn/2 - 1}}{B(dfn/2, dfd/2) \cdot (1 + \\frac{dfn}{dfd} \cdot x)^{(dfn + dfd)/2}}
        $$

        where:
        - $x$ is the F statistic.
        - $dfn$ is the degrees of freedom for the numerator.
        - $dfd$ is the degrees of freedom for the denominator.
        - $B(\\cdot)$ is the beta function.
        """)

        st.write("""
        The F-distribution is used primarily to compare the variances of two populations, and is commonly used in analysis of variance (ANOVA).
        """)

        # ユーザーから自由度を入力
        dfn = st.number_input('Enter the degrees of freedom for the numerator (dfn):', value=5, min_value=1)
        dfd = st.number_input('Enter the degrees of freedom for the denominator (dfd):', value=10, min_value=1)
        x_value_input = st.text_input('Enter a value for x (F-distribution):', value="")
        p_value_input = st.text_input('Enter a right-tail p-value (between 0 and 1):', value="")

        # 初期化
        x_value = None
        p_value = None

        # どちらかが入力されたら計算
        if x_value_input:
            try:
                x_value = float(x_value_input)
                p_value = 1 - f.cdf(x_value, dfn, dfd)
            except ValueError:
                st.error("Invalid x-value")

        elif p_value_input:
            try:
                p_value = float(p_value_input)
                if 0 <= p_value <= 1:
                    x_value = f.ppf(1 - p_value, dfn, dfd)
                else:
                    st.error("p-value must be between 0 and 1")
            except ValueError:
                st.error("Invalid p-value")

        # 計算結果の表示
        if x_value is not None and p_value is not None:
            st.write(f"The x-value is: {x_value:.4f}")
            st.write(f"The right-tail p-value is: {p_value:.4f}")

            # F分布の図を表示（右側塗りつぶし）
            x = np.linspace(0, 5, 1000)
            y = f.pdf(x, dfn, dfd)

            fig, ax = plt.subplots(figsize=(5, 3))
            ax.plot(x, y, label=f'F Distribution (dfn={dfn}, dfd={dfd})')
            
            # 右側塗りつぶし (x_valueより大きい部分)
            ax.fill_between(x, 0, y, where=(x >= x_value), color='blue', alpha=0.3, label="Right-tail probability")
            ax.axvline(x=x_value, color='red', linestyle='--', label=f"x = {x_value:.2f}")

            ax.legend()
            st.pyplot(fig)

    elif language == "日本語":
        st.title("F分布")

        st.write("""
        F分布の確率密度関数（PDF）は次の式で表されます：

        $$
        f(x; dfn, dfd) = \\frac{(dfn/dfd)^{dfn/2} \cdot x^{dfn/2 - 1}}{B(dfn/2, dfd/2) \cdot (1 + \\frac{dfn}{dfd} \cdot x)^{(dfn + dfd)/2}}
        $$

        ここで:
        - $x$ はF統計量です。
        - $dfn$ は分子の自由度です。
        - $dfd$ は分母の自由度です。
        - $B(\\cdot)$ はベータ関数です。
        """)

        st.write("""
        F分布は主に2つの母集団の分散を比較するために使用され、分散分析 (ANOVA) でよく用いられます。
        """)

        # ユーザーから自由度を入力
        dfn = st.number_input('分子の自由度 (dfn) を入力してください:', value=5, min_value=1)
        dfd = st.number_input('分母の自由度 (dfd) を入力してください:', value=10, min_value=1)
        x_value_input = st.text_input('x値を入力してください（F分布）:', value="")
        p_value_input = st.text_input('右側のp値を入力してください（0から1の間）:', value="")

        # 初期化
        x_value = None
        p_value = None

        # どちらかが入力されたら計算
        if x_value_input:
            try:
                x_value = float(x_value_input)
                p_value = 1 - f.cdf(x_value, dfn, dfd)
            except ValueError:
                st.error("無効な x 値です")

        elif p_value_input:
            try:
                p_value = float(p_value_input)
                if 0 <= p_value <= 1:
                    x_value = f.ppf(1 - p_value, dfn, dfd)
                else:
                    st.error("p値は 0 から 1 の間でなければなりません")
            except ValueError:
                st.error("無効な p 値です")

        # 計算結果の表示
        if x_value is not None and p_value is not None:
            st.write(f"x値は: {x_value:.4f}")
            st.write(f"右側のp値は: {p_value:.4f}")

            # F分布の図を表示（右側塗りつぶし）
            x = np.linspace(0, 5, 1000)
            y = f.pdf(x, dfn, dfd)

            fig, ax = plt.subplots(figsize=(5, 3))
            ax.plot(x, y, label=f'F分布 (dfn={dfn}, dfd={dfd})')
            
            # 右側塗りつぶし (x_valueより大きい部分)
            ax.fill_between(x, 0, y, where=(x >= x_value), color='blue', alpha=0.3, label="右側確率")
            ax.axvline(x=x_value, color='red', linestyle='--', label=f"x = {x_value:.2f}")

            ax.legend()
            st.pyplot(fig)
