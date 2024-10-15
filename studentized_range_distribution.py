import streamlit as st
import scipy.stats as stats

# 自由度とp値からx値を求める関数
def p_to_x(dfn, dfd, p_value):
    """
    自由度 (dfn, dfd) と p値 から x値 を求める (studentized range distribution).
    
    Parameters:
    dfn (int): 分子の自由度
    dfd (int): 分母の自由度
    p_value (float): p値
    
    Returns:
    float: 対応する x値
    """
    try:
        x_value = stats.studentized_range.ppf(p_value, dfn, dfd)
        return x_value
    except Exception as e:
        return str(e)

# 自由度とx値からp値を求める関数
def x_to_p(dfn, dfd, x_value):
    """
    自由度 (dfn, dfd) と x値 から p値 を求める (studentized range distribution).
    
    Parameters:
    dfn (int): 分子の自由度
    dfd (int): 分母の自由度
    x_value (float): x値
    
    Returns:
    float: 対応する p値
    """
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
        You can convert p-value to x-value and vice versa for a given degrees of freedom.
        """)

        # 自由度の入力
        dfn = st.number_input("Enter the numerator degrees of freedom (dfn):", min_value=1, value=5)
        dfd = st.number_input("Enter the denominator degrees of freedom (dfd):", min_value=1, value=10)

        # 計算モードの選択
        mode = st.radio("Choose a calculation mode:", ("p-value to x-value", "x-value to p-value"))

        if mode == "p-value to x-value":
            st.subheader("Convert p-value to x-value")
            p_value = st.number_input("Enter the p-value (between 0 and 1):", min_value=0.0, max_value=1.0, value=0.05)
            
            if st.button("Calculate x-value"):
                x_value = p_to_x(dfn, dfd, p_value)
                st.write(f"For p-value = {p_value}, the corresponding x-value is: {x_value}")
        
        elif mode == "x-value to p-value":
            st.subheader("Convert x-value to p-value")
            x_value = st.number_input("Enter the x-value:")
            
            if st.button("Calculate p-value"):
                p_value = x_to_p(dfn, dfd, x_value)
                st.write(f"For x-value = {x_value}, the corresponding p-value is: {p_value}")

    elif language == "日本語":
        st.title("ステューデント化された範囲分布の計算")

        st.write("""
        ステューデント化された範囲分布は、統計における多重比較に使用され、特にテューキーのHSD検定で使用されます。
        自由度を指定して、p値からx値、またはx値からp値を計算できます。
        """)

        # 自由度の入力
        dfn = st.number_input("分子の自由度 (dfn) を入力してください:", min_value=1, value=5)
        dfd = st.number_input("分母の自由度 (dfd) を入力してください:", min_value=1, value=10)

        # 計算モードの選択
        mode = st.radio("計算モードを選択してください:", ("p値からx値", "x値からp値"))

        if mode == "p値からx値":
            st.subheader("p値からx値を計算")
            p_value = st.number_input("p値を入力してください (0から1の間):", min_value=0.0, max_value=1.0, value=0.05)
            
            if st.button("x値を計算"):
                x_value = p_to_x(dfn, dfd, p_value)
                st.write(f"p値 = {p_value} のとき、対応するx値は: {x_value} です。")
        
        elif mode == "x値からp値":
            st.subheader("x値からp値を計算")
            x_value = st.number_input("x値を入力してください:")
            
            if st.button("p値を計算"):
                p_value = x_to_p(dfn, dfd, x_value)
                st.write(f"x値 = {x_value} のとき、対応するp値は: {p_value} です。")
