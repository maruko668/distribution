import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def show_standard_normal():
    st.title("Standard Normal Distribution")

    # x値の入力
    x_value = st.number_input('Enter a value for x (Standard Normal Distribution):', value=0.0)

    # 標準正規分布の図を表示
    x = np.linspace(-4, 4, 1000)
    y = norm.pdf(x)
    
    fig, ax = plt.subplots()
    ax.plot(x, y, label='Standard Normal Distribution')
    ax.fill_between(x, 0, y, where=(x <= x_value), color='blue', alpha=0.3)
    ax.axvline(x=x_value, color='red', linestyle='--')
    ax.legend()

    st.pyplot(fig)

    # p値を計算して表示
    p_value = norm.cdf(x_value)
    st.write(f'The p-value for x = {x_value} is: {p_value:.4f}')
