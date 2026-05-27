# app.py
# Streamlit 계산기 웹앱

import streamlit as st
import math

st.set_page_config(page_title="다기능 계산기", page_icon="🧮")

st.title("🧮 다기능 계산기 웹앱")

st.write("사칙연산, 모듈러연산, 지수연산, 로그연산을 지원합니다.")

# 연산 선택
operation = st.selectbox(
    "원하는 연산을 선택하세요.",
    (
        "덧셈",
        "뺄셈",
        "곱셈",
        "나눗셈",
        "모듈러연산",
        "지수연산",
        "로그연산"
    )
)

# 숫자 입력
if operation != "로그연산":
    num1 = st.number_input("첫 번째 숫자", value=0.0)
    num2 = st.number_input("두 번째 숫자", value=0.0)

# 로그연산 전용 입력
else:
    value = st.number_input("로그를 계산할 숫자", value=1.0, min_value=0.000001)
    base = st.number_input("로그의 밑", value=10.0, min_value=0.000001)

# 계산 버튼
if st.button("계산하기"):

    try:
        # 사칙연산
        if operation == "덧셈":
            result = num1 + num2

        elif operation == "뺄셈":
            result = num1 - num2

        elif operation == "곱셈":
            result = num1 * num2

        elif operation == "나눗셈":
            if num2 == 0:
                st.error("0으로 나눌 수 없습니다.")
                st.stop()
            result = num1 / num2

        # 모듈러연산
        elif operation == "모듈러연산":
            result = num1 % num2

        # 지수연산
        elif operation == "지수연산":
            result = num1 ** num2

        # 로그연산
        elif operation == "로그연산":
            if value <= 0:
                st.error("로그를 계산할 숫자는 0보다 커야 합니다.")
                st.stop()

            if base <= 0 or base == 1:
                st.error("로그의 밑은 0보다 크고 1이 아니어야 합니다.")
                st.stop()

            result = math.log(value, base)

        # 결과 출력
        st.success(f"결과: {result}")

    except Exception as e:
        st.error(f"오류 발생: {e}")
