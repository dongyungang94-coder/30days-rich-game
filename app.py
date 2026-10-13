
import streamlit as st
import random

st.set_page_config(
    page_title="30일 부자 되기",
    page_icon="💰",
    layout="centered"
)

# -------------------------
# 1. 게임 기본 설정
# -------------------------

START_MONEY = 1_000_000
DAILY_SALARY = 100_000
WIN_MONEY = 5_000_000
TOTAL_DAYS = 30

# -------------------------
# 2. 게임 초기화
# -------------------------

def reset_game():
    st.session_state.day = 1
    st.session_state.money = START_MONEY
    st.session_state.game_over = False
    st.session_state.logs = [
        "🎮 게임 시작! 30일 안에 500만 원을 모아 보세요."
    ]
    st.session_state.first_action = True

if "day" not in st.session_state:
    reset_game()

# -------------------------
# 3. 하루 진행 함수
# -------------------------

def play_day(action):
    # 월급 받기
    st.session_state.money += DAILY_SALARY

    log = [
        f"💵 {st.session_state.day}일 차 월급 "
        f"+{DAILY_SALARY:,}원"
    ]

    money = st.session_state.money

    # 선택한 행동 실행
    if action == "저축하기":
        # 저축 보너스: 현재 자산의 0.2%
        interest = int(money * 0.002)
        st.session_state.money += interest
        log.append(f"🏦 저축 이자 +{interest:,}원")

    elif action == "투자하기":
        # 최대 10만 원을 투자
        invest = min(100_000, money)

        # 투자 수익률: -20%, -10%, 0%, +10%, +20%
        rate = random.choice([-0.2, -0.1, 0, 0.1, 0.2])
        profit = int(invest * rate)

        st.session_state.money += profit

        if profit > 0:
            log.append(f"📈 투자 성공! +{profit:,}원")
        elif profit < 0:
            log.append(f"📉 투자 손실! {profit:,}원")
        else:
            log.append("➖ 투자 손익이 없습니다.")

    elif action == "쇼핑하기":
        cost = min(50_000, money)
        st.session_state.money -= cost
        log.append(f"🛍️ 쇼핑 비용 -{cost:,}원")

        mood = random.choice([
            "마음에 쏙 드는 상품을 찾았어요!",
            "충동구매였나 봐요...",
            "할인 상품을 잘 골랐어요!",
        ])
        log.append(f"✨ {mood}")

    # 랜덤 이벤트
    event = random.choice([
        ("🎁 깜짝 보너스!", 100_000),
        ("🍀 길에서 행운을 만났어요!", 50_000),
        ("📱 휴대폰 수리비가 발생했어요.", -80_000),
        ("🎉 친구에게 선물을 받았어요!", 30_000),
        ("☔ 예상치 못한 지출이 생겼어요.", -50_000),
        ("😌 오늘은 별일이 없네요.", 0),
    ])

    event_name, event_money = event

    if event_money < 0:
        # 현재 가진 돈보다 큰 지출은 발생하지 않음
        event_money = -min(
            st.session_state.money,
            abs(event_money)
        )

    st.session_state.money += event_money

    if event_money > 0:
        log.append(f"{event_name} +{event_money:,}원")
    elif event_money < 0:
        log.append(f"{event_name} {event_money:,}원")
    else:
        log.append(event_name)

    # 하루 결과 기록
    st.session_state.logs = log + st.session_state.logs
    st.session_state.logs = st.session_state.logs[:60]

    # 다음 날로 이동
    st.session_state.day += 1

    # 승리 / 패배 판정
    if st.session_state.money <= 0:
        st.session_state.money = 0
        st.session_state.game_over = True
        st.session_state.result = "파산했어요! 💸"

    elif st.session_state.day > TOTAL_DAYS:
        st.session_state.game_over = True

        if st.session_state.money >= WIN_MONEY:
            st.session_state.result = "부자 달성! 🏆"
        else:
            st.session_state.result = "도전 종료! 💰"

# -------------------------
# 4. 게임 화면
# -------------------------

st.title("💰 30일 부자 되기")
st.write("월급을 관리하고, 소비와 투자로 나만의 자산을 만들어 보세요!")

st.progress(
    min((st.session_state.day - 1) / TOTAL_DAYS, 1.0)
)

# 자산 및 날짜 표시
c1, c2 = st.columns(2)

c1.metric(
    "💵 현재 자산",
    f"{st.session_state.money:,}원"
)

if st.session_state.game_over:
    shown_day = min(st.session_state.day - 1, TOTAL_DAYS)
else:
    shown_day = st.session_state.day

c2.metric(
    "📅 진행 날짜",
    f"{shown_day} / {TOTAL_DAYS}일"
)

st.caption(
    f"목표: {WIN_MONEY:,}원 | "
    f"매일 월급: {DAILY_SALARY:,}원"
)

st.divider()

# -------------------------
# 5. 행동 선택
# -------------------------

if not st.session_state.game_over:
    st.subheader(f"📆 {st.session_state.day}일 차")
    st.write("오늘은 어떤 행동을 할까요?")

    actions = ["저축하기", "투자하기", "쇼핑하기"]

    # 첫 행동은 쇼핑하기로 설정
    default_index = 2 if st.session_state.first_action else 0

    action = st.radio(
        "행동 선택",
        actions,
        index=default_index,
        horizontal=True
    )

    if st.button("🎲 하루 진행하기", use_container_width=True):
        st.session_state.first_action = False
        play_day(action)
        st.rerun()

else:
    st.subheader(st.session_state.result)

    if st.session_state.result == "부자 달성! 🏆":
        st.balloons()
        st.success(
            f"축하합니다! 최종 자산은 "
            f"{st.session_state.money:,}원입니다."
        )
    elif st.session_state.result == "파산했어요! 💸":
        st.error("자산이 바닥났습니다. 소비와 투자 전략을 바꿔 보세요!")
    else:
        st.info(
            f"30일 동안 모은 최종 자산: "
            f"{st.session_state.money:,}원"
        )

    if st.button("🔄 다시 시작하기", use_container_width=True):
        reset_game()
        st.rerun()

# -------------------------
# 6. 게임 기록
# -------------------------

st.divider()
st.subheader("📜 게임 기록")

for item in st.session_state.logs:
    st.write(item)
    