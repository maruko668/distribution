import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, uniform, triang
import pandas as pd

# カーネル関数の定義
def kernel_normal(x):
    """標準正規分布をカーネルとして使用"""
    return norm.pdf(x)

def kernel_uniform(x):
    """一様分布をカーネルとして使用"""
    return uniform.pdf(x, loc=-1, scale=2)

def kernel_triangle(x):
    """対象な三角分布をカーネルとして使用"""
    return triang.pdf(x, c=0.5, loc=-1, scale=2)

# KDE推定の関数
def kde_estimation(x, data, h, kernel_func):
    n = len(data)
    return np.sum([kernel_func((x - xi) / h) / h for xi in data]) / n

# データを選択する機能を追加
def select_data():
    data_source = st.selectbox("Choose data source:", ["Random Normal Data", "Upload CSV Data"])

    if data_source == "Random Normal Data":
        st.write("Random data will be generated from a normal distribution.")
        np.random.seed(42)
        data = np.random.normal(loc=0, scale=1, size=100)
    elif data_source == "Upload CSV Data":
        uploaded_file = st.file_uploader("Upload a CSV file with one column of data", type=["csv"])
        if uploaded_file is not None:
            data_df = pd.read_csv(uploaded_file)
            if data_df.shape[1] == 1:  # 1列のデータを期待
                data = data_df.iloc[:, 0].dropna().values  # 欠損値を除去してデータを配列に変換
                st.write("Uploaded data preview:", data_df.head())
            else:
                st.error("The CSV file must contain exactly one column.")
                data = np.array([])  # 無効なデータを防止
        else:
            data = np.array([])  # ファイルがない場合は空の配列を返す
    return data

# Streamlitでカーネル密度推定の様子を表示
def show_kde_estimation():
    st.title("Kernel Density Estimation (KDE)")

    # データの選択
    data = select_data()

    # データが無効の場合は何も表示しない
    if len(data) == 0:
        st.write("Please upload a valid CSV file or generate random data.")
        return

    # バンド幅 (h) の入力
    h = st.slider("Select the bandwidth (h)", min_value=0.1, max_value=2.0, step=0.1, value=0.5)

    # カーネルの選択
    kernel_choice = st.selectbox("Select the kernel function", ["Standard Normal", "Uniform", "Symmetric Triangle"])

    # カーネル関数を選択
    if kernel_choice == "Standard Normal":
        kernel_func = kernel_normal
    elif kernel_choice == "Uniform":
        kernel_func = kernel_uniform
    elif kernel_choice == "Symmetric Triangle":
        kernel_func = kernel_triangle

    # 推定密度関数の計算
    x_values = np.linspace(min(data) - 2, max(data) + 2, 1000)  # データ範囲に基づいてx軸を設定
    f_h_values = [kde_estimation(x, data, h, kernel_func) for x in x_values]

    # グラフの作成
    fig, ax = plt.subplots(figsize=(8, 5))
    
    # KDEのプロット
    ax.plot(x_values, f_h_values, label=f"KDE with {kernel_choice} kernel", color='blue')
    
    # 元データのヒストグラム
    ax.hist(data, bins=20, density=True, alpha=0.5, label="Data Histogram", color='gray')

    ax.set_title(f"Kernel Density Estimation with h={h}")
    ax.set_xlabel("x")
    ax.set_ylabel("Density")
    ax.legend()

    st.pyplot(fig)

