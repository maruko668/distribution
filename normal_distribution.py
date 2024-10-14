import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def show_normal_distribution(language):
    st.title("Normal Distribution")

    # ユーザーから平均と標準偏差を入力
    mean = st.number_input('Enter the mean (μ):', value=0.0, step=0.1)
    std_dev = st.number_input('Enter the standard deviation (σ):', value=1.0, step=0.1, min_value=0.1)

    # ユーザーからx値またはp値のどちらかを入力
    x_value_input = st.text_input('Enter a value for x (Normal Distribution):', value="")
    p_value_input = st.text_input('Enter a p-value (between 0 and 1):', value="")

    # 初期化
    x_value = None
    p_value = None

    # どちらかが入力されたら計算
    if x_value_input:
        try:
            x_value = float(x_value_input)
            p_value = norm.cdf(x_value, loc=mean, scale=std_dev)
        except ValueError:
            st.error("Invalid x-value")

    elif p_value_input:
        try:
            p_value = float(p_value_input)
            if 0 <= p_value <= 1:
                x_value = norm.ppf(p_value, loc=mean, scale=std_dev)
            else:
                st.error("p-value must be between 0 and 1")
        except ValueError:
            st.error("Invalid p-value")

    # 計算結果の表示
    if x_value is not None and p_value is not None:
        st.write(f"The x-value is: {x_value:.4f}")
        st.write(f"The p-value is: {p_value:.4f}")

        # 正規分布の図を表示
        x = np.linspace(mean - 4*std_dev, mean + 4*std_dev, 1000)
        y = norm.pdf(x, loc=mean, scale=std_dev)

        # 図のサイズを半分に設定
        fig, ax = plt.subplots(figsize=(5, 3))
        ax.plot(x, y, label=f'Normal Distribution (μ={mean}, σ={std_dev})')
        ax.fill_between(x, 0, y, where=(x <= x_value), color='green', alpha=0.3)
        ax.axvline(x=x_value, color='red', linestyle='--')
        ax.legend()

        st.pyplot(fig)
