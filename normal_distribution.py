import streamlit as st
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt


def show_normal_distribution():
    st.title("Normal Distribution")

    # ユーザーから平均と標準偏差を入力
    mean = st.number_input('Enter the mean (μ):', value=0.0)
    std_dev = st.number_input('Enter the standard deviation (σ):', value=1.0)
    x_value = st.number_input('Enter a value for x (Normal Distribution):', value=0.0)

    # 正規分布の図を表示
    x = np.linspace(mean - 4*std_dev, mean + 4*std_dev, 1000)
    y = norm.pdf(x, loc=mean, scale=std_dev)
    
    fig, ax = plt.subplots()
    ax.plot(x, y, label=f'Normal Distribution (μ={mean}, σ={std_dev})')
    ax.fill_between(x, 0, y, where=(x <= x_value), color='green', alpha=0.3)
    ax.axvline(x=x_value, color='red', linestyle='--')
    ax.legend()

    st.pyplot(fig)

    # p値を計算して表示
    p_value = norm.cdf(x_value, loc=mean, scale=std_dev)
    st.write(f'The p-value for x = {x_value} (Normal Distribution) is: {p_value:.4f}')
