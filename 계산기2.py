# app.py

import streamlit as st
import math
import random

st.set_page_config(
    page_title="다기능 계산기 & 확률 시뮬레이터",
    page_icon="🧮"
)

# ==================================================
# 하늘색 배경 커스텀 테마
# ==================================================

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #87CEEB 0%, #ADD8E6 100%);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ==================================================
# 사이드바 메뉴
# ==================================================

menu = st.sidebar.radio(
    "메뉴 선택",
    ["계산기", "확률 시뮬레이터"]
)

# ==================================================
# 계산기
# ==================================================

if menu == "계산기":

    st.title("🧮 다기능 계산기")

    st.write(
        "사칙연산, 모듈러연산, 지수연산, 로그연산을 지원합니다."
    )

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

        num1 = st.number_input(
            "첫 번째 숫자",
            value=0.0
        )

        num2 = st.number_input(
            "두 번째 숫자",
            value=0.0
        )

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

                if num2 == 0:
                    st.error("0으로 나눌 수 없습니다.")
                    st.stop()

                result = num1 % num2

            elif operation == "지수연산":
                result = num1 ** num2

            elif operation == "로그연산":

                if value <= 0:
                    st.error(
                        "로그를 계산할 숫자는 0보다 커야 합니다."
                    )
                    st.stop()

                if base <= 0 or base == 1:
                    st.error(
                        "로그의 밑은 0보다 크고 1이 아니어야 합니다."
                    )
                    st.stop()

                result = math.log(value, base)

            st.success(f"결과: {result}")

        except Exception as e:
            st.error(f"오류 발생: {e}")

# ==================================================
# 확률 시뮬레이터
# ==================================================

elif menu == "확률 시뮬레이터":

    st.title("🎲 확률 시뮬레이터")

    simulator_type = st.selectbox(
        "실험 종류 선택",
        ["동전", "주사위"]
    )

    # 동전 선택 시 수학적 확률 계산 함수
    def get_theoretical_probability_coin(event):
        return 0.5

    # 주사위 선택 시 수학적 확률 계산 함수
    def get_theoretical_probability_dice(event):
        if event in ["1", "2", "3", "4", "5", "6"]:
            return 1 / 6
        elif event == "짝수":
            return 3 / 6  # 2, 4, 6
        elif event == "홀수":
            return 3 / 6  # 1, 3, 5

    # 사건 선택
    if simulator_type == "동전":

        event = st.selectbox(
            "사건 선택",
            ["앞면", "뒷면"]
        )

        theoretical_probability = get_theoretical_probability_coin(event)

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

        theoretical_probability = get_theoretical_probability_dice(event)

    # ==================================================
    # 세션 상태 초기화
    # ==================================================

    if "total_trials" not in st.session_state:
        st.session_state.total_trials = 0

    if "total_success" not in st.session_state:
        st.session_state.total_success = 0

    current_event = f"{simulator_type}_{event}"

    if "last_event" not in st.session_state:
        st.session_state.last_event = current_event

    # 사건 변경 시 자동 초기화
    if st.session_state.last_event != current_event:

        st.session_state.total_trials = 0
        st.session_state.total_success = 0
        st.session_state.last_event = current_event

    st.divider()

    # ==================================================
    # 초기화 버튼
    # ==================================================

    if st.button("🔄 통계 초기화"):

        st.session_state.total_trials = 0
        st.session_state.total_success = 0
        st.rerun()

    st.subheader("시행 횟수")

    col1, col2, col3, col4 = st.columns(4)

    trials = 0

    if col1.button("1회"):
        trials = 1

    if col2.button("10회"):
        trials = 10

    if col3.button("100회"):
        trials = 100

    if col4.button("1000회"):
        trials = 1000

    # ==================================================
    # 동전 실험
    # ==================================================

    if trials > 0:

        success = 0

        if simulator_type == "동전":

            for _ in range(trials):

                result = random.choice(
                    ["앞면", "뒷면"]
                )

                if result == event:
                    success += 1

        # ==================================================
        # 주사위 실험
        # ==================================================

        else:

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

        st.session_state.total_trials += trials
        st.session_state.total_success += success

    # ==================================================
    # 결과 표시
    # ==================================================

    if st.session_state.total_trials > 0:

        experimental_probability = (
            st.session_state.total_success
            / st.session_state.total_trials
        )

    else:

        experimental_probability = 0

    st.divider()

    st.success(
        f"누적 성공 횟수: {st.session_state.total_success}"
    )

    st.info(
        f"누적 시행 횟수: {st.session_state.total_trials}"
    )

    # 실험 확률 표시
    st.metric(
        "누적 실험 확률",
        f"{experimental_probability:.4f}"
    )

    st.divider()

    # ==================================================
    # 수학적 확률 표시
    # ==================================================

    st.subheader("📐 수학적 확률 (이론적 확률)")

    if simulator_type == "동전":
        st.metric(
            f"'{event}'이 나올 확률",
            f"{theoretical_probability:.4f}",
            help="동전 한 번 던질 때 앞면이 나올 확률은 1/2"
        )

    else:
        if event in ["1", "2", "3", "4", "5", "6"]:
            st.metric(
                f"주사위에서 '{event}'이 나올 확률",
                f"{theoretical_probability:.4f}",
                help=f"주사위 한 번 던질 때 특정 숫자가 나올 확률은 1/6"
            )

        elif event == "짝수":
            st.metric(
                f"주사위에서 '짝수'가 나올 확률",
                f"{theoretical_probability:.4f}",
                help=f"짝수: 2, 4, 6 → 확률 = 3/6 = 1/2"
            )

        elif event == "홀수":
            st.metric(
                f"주사위에서 '홀수'가 나올 확률",
                f"{theoretical_probability:.4f}",
                help=f"홀수: 1, 3, 5 → 확률 = 3/6 = 1/2"
            )
