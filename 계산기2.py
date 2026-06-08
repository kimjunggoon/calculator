# app.py

import streamlit as st
import math
import random

st.set_page_config(page_title="다기능 계산기 & 확률 시뮬레이터", page_icon="🧮")

# ---------------------------
# 사이드바 메뉴
# ---------------------------
menu = st.sidebar.radio(
    "메뉴 선택",
    ["계산기", "확률 시뮬레이터"]
)

# ===========================
# 계산기
# ===========================
if menu == "계산기":

    st.title("🧮 다기능 계산기 웹앱")

    st.write("사칙연산, 모듈러연산, 지수연산, 로그연산을 지원합니다.")

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

    if operation != "로그연산":
        num1 = st.number_input("첫 번째 숫자", value=0.0)
        num2 = st.number_input("두 번째 숫자", value=0.0)

    else:
        value = st.number_input(
            "로그를 계산할 숫자",
            value=1.0,
            min_value=0.000001
        )

        base = st.number_input(
            "로그의 밑",
            value=10.0,
            min_value=0.000001
        )

    if st.button("계산하기"):

        try:

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

            elif operation == "모듈러연산":
                result = num1 % num2

            elif operation == "지수연산":
                result = num1 ** num2

            elif operation == "로그연산":

                if value <= 0:
                    st.error("로그를 계산할 숫자는 0보다 커야 합니다.")
                    st.stop()

                if base <= 0 or base == 1:
                    st.error("로그의 밑은 0보다 크고 1이 아니어야 합니다.")
                    st.stop()

                result = math.log(value, base)

            st.success(f"결과: {result}")

        except Exception as e:
            st.error(f"오류 발생: {e}")

# ===========================
# 확률 시뮬레이터
# ===========================
elif menu == "확률 시뮬레이터":

    st.title("🎲 확률 시뮬레이터")

    simulator_type = st.selectbox(
        "실험 종류 선택",
        ["동전", "주사위"]
    )

    # -----------------------
    # 동전
    # -----------------------
    if simulator_type == "동전":

        event = st.selectbox(
            "사건 선택",
            ["앞면", "뒷면"]
        )

        st.subheader("시행 횟수")

        col1, col2, col3, col4 = st.columns(4)

        trials = None

        if col1.button("1회"):
            trials = 1

        if col2.button("10회"):
            trials = 10

        if col3.button("100회"):
            trials = 100

        if col4.button("1000회"):
            trials = 1000

        if trials:

            success = 0

            for _ in range(trials):
                result = random.choice(["앞면", "뒷면"])

                if result == event:
                    success += 1

            probability = success / trials

            st.success(f"성공 횟수: {success}")
            st.info(f"실험 확률: {probability:.4f}")

    # -----------------------
    # 주사위
    # -----------------------
    else:

        event = st.selectbox(
            "사건 선택",
            [
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "짝수",
                "홀수"
            ]
        )

        st.subheader("시행 횟수")

        col1, col2, col3, col4 = st.columns(4)

        trials = None

        if col1.button("1회"):
            trials = 1

        if col2.button("10회"):
            trials = 10

        if col3.button("100회"):
            trials = 100

        if col4.button("1000회"):
            trials = 1000

        if trials:

            success = 0

            for _ in range(trials):

                dice = random.randint(1, 6)

                if event.isdigit():

                    if dice == int(event):
                        success += 1

                elif event == "짝수":

                    if dice % 2 == 0:
                        success += 1

                elif event == "홀수":

                    if dice % 2 == 1:
                        success += 1

            probability = success / trials

            st.success(f"성공 횟수: {success}")
            st.info(f"실험 확률: {probability:.4f}")
