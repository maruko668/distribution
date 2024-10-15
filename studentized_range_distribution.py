import streamlit as st
import scipy.stats as stats

# 自由度とp値からx値を求める関数
def p_to_x(groups, total_data, p_value):
    """
    グループ数と全体のデータ数に基づいて p値 から x値 を求める (studentized range distribution).
    
    Parameters:
    groups (int): グループ数
    total_data (int): 全体のデータ数
    p_value (float): p値
    
    Returns:
    float: 対応する x値
    """
    dfn = groups  # グループ数
    dfd = total_data - groups  # 全体のデータ数 - グループ数
    try:
        x_value = stats.studentized_range.ppf(p_value, dfn, dfd)
        return x_value
    except Exception as e:
        return str(e)

# 自由度とx値からp値を求める関数
def x_to_p(groups, total_data, x_value):
    """
    グループ数と全体のデータ数に基づいて x値 から p値 を求める (studentized range distribution).
    
    Parameters:
    groups (int): グループ数
    total_data (int): 全体のデータ数
    x_value (float): x値
    
    Returns:
    float: 対応する p値
    """
    dfn = groups  # グループ数
    dfd = total_data - groups  # 全体のデータ数 - グループ数
    try:
        p_value = stats.studentized_range.cdf(x_value, dfn, dfd)
        return p_value
    except Exception as e:
        return str(e)

# Streamlitでステューデント化された範囲分布のページを作成
def show_studentized_range(language):
    if language == "English":
        st.title("Studentized Range Distribution Calculator")

        st.write("""
        The studentized range distribution is used for multiple comparisons in statistics. It is used in the Tukey HSD test.
        You can input either p-value or x-value, and the corresponding result will be automatically calculated.
        """)

        # グループ数と全体のデータ数の入力
        groups = st.number_input("Enter the number of groups:", min_value=2, value=3)
        total_data = st.number_input("Enter the total number of data points:", min_value=groups + 1, value=10)

        # p値またはx値の入力（どちらかが入力されると計算）
        p_value_input = st.text_input("Enter the p-value (between 0 and 1):", value="")
        x_value_input = st.text_input("Enter the x-value:", value="")

        # 初期化
        x_value = None
        p_value = None

        # p値が入力された場合
        if p_value_input:
            try:
                p_value = float(p_value_input)
                x_value = p_to_x(groups, total_data, p_value)
            except ValueError:
                st.error("Invalid p-value")

        # x値が入力された場合
        elif x_value_input:
            try:
                x_value = float(x_value_input)
                p_value = x_to_p(groups, total_data, x_value)
            except ValueError:
                st.error("Invalid x-value")

        # 計算結果の表示
        if x_value is not None and p_value is not None:
            st.write(f"The x-value is: {x_value:.4f}")
            st.write(f"The p-value is: {p_value:.4f}")

    elif language == "日本語":
        st.title("ステューデント化された範囲分布の計算")

        st.write("""
        ステューデント化された範囲分布は、統計における多重比較に使用され、特にテューキーのHSD検定で使用されます。
        p値またはx値のいずれかを入力すれば、対応する結果が自動的に計算されます。
        """)

        # グループ数と全体のデータ数の入力
        groups = st.number_input("グループ数を入力してください:", min_value=2, value=3)
        total_data = st.number_input("全体のデータ数を入力してください:", min_value=groups + 1, value=10)

        # p値またはx値の入力（どちらかが入力されると計算）
        p_value_input = st.text_input("p値を入力してください (0から1の間):", value="")
        x_value_input = st.text_input("x値を入力してください:", value="")

        # 初期化
        x_value = None
        p_value = None

        # p値が入力された場合
        if p_value_input:
            try:
                p_value = float(p_value_input)
                x_value = p_to_x(groups, total_data, p_value)
            except ValueError:
                st.error("無効な p 値です")

        # x値が入力された場合
        elif x_value_input:
            try:
                x_value = float(x_value_input)
                p_value = x_to_p(groups, total_data, x_value)
            except ValueError:
                st.error("無効な x 値です")

        # 計算結果の表示
        if x_value is not None and p_value is not None:
            st.write(f"x値は: {x_value:.4f}")
            st.write(f"p値は: {p_value:.4f}")
