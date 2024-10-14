import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def show_standard_normal():
    st.title("Standard Normal Distribution")

    # x値の入力
    x_value = st.number_input('Enter a value for x (Standard Normal Distribution):', value=0.0, step=0.1)
    p_value = st.number_input('Enter a p-value (between 0 and 1) to find the corresponding x-value:', value=0.5, min_value=0.0, max_value=1.0, step=0.01)

    # p値からx値を計算
    x_from_p = norm.ppf(p_value)

    # x_from_pの表示
    st.write(f"The x-value for p = {p_value} is: {x_from_p:.4f}")

    # グラフが変化する要因（p値またはx値の変更）に基づいて再描画する
    if st.button('Update graph'):
        # 標準正規分布の図を表示
        x = np.linspace(-4, 4, 1000)
        y = norm.pdf(x)

        # 図のサイズを半分に設定
        fig, ax = plt.subplots(figsize=(5, 3))
        ax.plot(x, y, label='Standard Normal Distribution')
        ax.fill_between(x, 0, y, where=(x <= x_value), color='blue', alpha=0.3)
        ax.axvline(x=x_value, color='red', linestyle='--')

        st.pyplot(fig)

        # x値からp値を計算して表示
        p_from_x = norm.cdf(x_value)
        st.write(f'The p-value for x = {x_value} is: {p_from_x:.4f}')
