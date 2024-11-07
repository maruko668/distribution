import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

def show_chi_squared_distribution(language):
    if language == "English":
        st.title("Chi-Squared Distribution")

        st.write("""
        The chi-squared distribution is commonly used in hypothesis testing and confidence interval estimation for variance.

        The p-value is calculated as the probability of observing a value equal to or greater than the given x-value, i.e., the right-tail probability:

        $$
        p = 1 - F(x; k)
        $$

        where:
        - $x$ is the chi-squared statistic.
        - $k$ is the degrees of freedom.
        """)

        df = st.number_input('Enter the degrees of freedom (k):', value=2, step=1, min_value=1)
        x_value_input = st.text_input('Enter a value for x (Chi-Squared Distribution):', value="")
        p_value_input = st.text_input('Enter a right-tail p-value (between 0 and 1):', value="")

        x_value = None
        p_value = None

        if x_value_input:
            try:
                x_value = float(x_value_input)
                p_value = 1 - chi2.cdf(x_value, df)
            except ValueError:
                st.error("Invalid x-value")
        elif p_value_input:
            try:
                p_value = float(p_value_input)
                if 0 <= p_value <= 1:
                    x_value = chi2.ppf(1 - p_value, df)
                else:
                    st.error("p-value must be between 0 and 1")
            except ValueError:
                st.error("Invalid p-value")

        if x_value is not None and p_value is not None:
            st.write(f"The x-value is: {x_value:.4f}")
            st.write(f"The right-tail p-value is: {p_value:.4f}")

            x = np.linspace(0, chi2.ppf(0.999, df), 1000)
            y = chi2.pdf(x, df)

            fig, ax = plt.subplots(figsize=(5, 3))
            ax.plot(x, y, label=f'Chi-Squared Distribution (k={df})')
            ax.fill_between(x, 0, y, where=(x >= x_value), color='red', alpha=0.3, label="Right-tail probability")
            ax.axvline(x=x_value, color='blue', linestyle='--', label=f"x = {x_value:.2f}")

            ax.legend()
            st.pyplot(fig)

    elif language == "日本語":
        st.title("カイ二乗分布")

        st.write("""
        カイ二乗分布は、仮説検定や分散の信頼区間推定によく使用されます。

        p値は、与えられたx値以上の確率、すなわち右側の確率として計算されます：

        $$
        p = 1 - F(x; k)
        $$

        ここで:
        - $x$ はカイ二乗統計量です。
        - $k$ は自由度です。
        """)

        df = st.number_input('自由度 (k) を入力してください:', value=2, step=1, min_value=1)
        x_value_input = st.text_input('x値を入力してください（カイ二乗分布）:', value="")
        p_value_input = st.text_input('右側のp値を入力してください（0から1の間）:', value="")

        x_value = None
        p_value = None

        if x_value_input:
            try:
                x_value = float(x_value_input)
                p_value = 1 - chi2.cdf(x_value, df)
            except ValueError:
                st.error("無効な x 値です")
        elif p_value_input:
            try:
                p_value = float(p_value_input)
                if 0 <= p_value <= 1:
                    x_value = chi2.ppf(1 - p_value, df)
                else:
                    st.error("p値は 0 から 1 の間でなければなりません")
            except ValueError:
                st.error("無効な p 値です")

        if x_value is not None and p_value is not None:
            st.write(f"x値は: {x_value:.4f}")
            st.write(f"右側のp値は: {p_value:.4f}")

            x = np.linspace(0, chi2.ppf(0.999, df), 1000)
            y = chi2.pdf(x, df)

            fig, ax = plt.subplots(figsize=(5, 3))
            ax.plot(x, y, label=f'カイ二乗分布 (k={df})')
            ax.fill_between(x, 0, y, where=(x >= x_value), color='red', alpha=0.3, label="右側確率")
            ax.axvline(x=x_value, color='blue', linestyle='--', label=f"x = {x_value:.2f}")

            ax.legend()
            st.pyplot(fig)
