import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def show_standard_normal():
    st.title("Standard Normal Distribution")

    # ユーザーからx値またはp値のどちらかを入力
    x_value_input = st.text_input('Enter a value for x (z-score):', value="")
    p_value_input = st.text_input('Enter a p-value (between 0 and 1):', value="")

    # 初期化
    x_value = None
    p_value = None

    # どちらかが入力されたら計算
    if x_value_input:
        try:
            x_value = float(x_value_input)
            p_value = norm.cdf(x_value)
        except ValueError:
            st.error("Invalid x-value")

    elif p_value_input:
        try:
            p_value = float(p_value_input)
            if 0 <= p_value <= 1:
                x_value = norm.ppf(p_value)
            else:
                st.error("p-value must be between 0 and 1")
        except ValueError:
            st.error("Invalid p-value")

    # 計算結果の表示
    if x_value is not None and p_value is not None:
        st.write(f"The x-value (z-score) is: {x_value:.4f}")
        st.write(f"The p-value is: {p_value:.4f}")

        # 標準正規分布の図を表示
        x = np.linspace(-4, 4, 1000)
        y = norm.pdf(x)

        # 図のサイズを半分に設定
        fig, ax = plt.subplots(figsize=(5, 3))
        ax.plot(x, y, label='Standard Normal Distribution')
        ax.fill_between(x, 0, y, where=(x <= x_value), color='blue', alpha=0.3)
        ax.axvline(x=x_value, color='red', linestyle='--')

        st.pyplot(fig)
