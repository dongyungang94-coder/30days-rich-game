
import streamlit as st

st.set_page_config(
    page_title="나의 회사 생활 유형",
    page_icon="🏢",
    layout="centered"
)

# 회사 생활 테스트 질문
questions = [
    {
        "q": "월요일 아침, 출근하자마자 상사가 일을 준다면?",
        "options": [
            ("일단 계획부터 세운다 📋", "ace"),
            ("동료들과 일정을 맞춘다 🤝", "peace"),
            ("마감 직전까지 효율을 계산한다 ☕", "lazy"),
            ("오늘도 파이팅! 신나게 시작한다 🎉", "fun")
        ]
    },
    {
        "q": "갑자기 오늘까지 끝내야 하는 일이 생겼다!",
        "options": [
            ("우선순위를 정하고 바로 시작!", "ace"),
            ("팀원들과 나눠서 해결한다", "peace"),
            ("꼭 필요한 것부터 빠르게 처리한다", "lazy"),
            ("일단 커피부터 마시고 정신을 차린다", "fun")
        ]
    },
    {
        "q": "점심시간에 가장 듣고 싶은 말은?",
        "options": [
            ("오늘 업무 벌써 다 끝냈어?", "ace"),
            ("다 같이 밥 먹으러 가자!", "peace"),
            ("오늘은 칼퇴 가능하대!", "lazy"),
            ("오늘 점심에 맛집 가자!", "fun")
        ]
    },
    {
        "q": "팀 프로젝트에서 내가 주로 맡는 역할은?",
        "options": [
            ("일정과 결과를 책임지는 리더", "ace"),
            ("의견을 조율하는 중재자", "peace"),
            ("복잡한 일을 간단하게 만드는 효율 담당", "lazy"),
            ("분위기를 살리는 아이디어 담당", "fun")
        ]
    },
    {
        "q": "상사가 내 이름을 부르며 다가온다. 내 반응은?",
        "options": [
            ("네! 필요한 자료 준비했습니다", "ace"),
            ("무슨 일이신지 차분하게 듣는다", "peace"),
            ("제발 추가 업무만 아니길 빈다", "lazy"),
            ("혹시 좋은 소식인가요? 😆", "fun")
        ]
    },
    {
        "q": "동료가 내게 일을 도와달라고 한다면?",
        "options": [
            ("내 업무부터 정리하고 도와준다", "ace"),
            ("힘들어 보이면 바로 도와준다", "peace"),
            ("어디까지 도와야 하는지 먼저 확인한다", "lazy"),
            ("도와주는 대신 커피 한 잔을 요청한다", "fun")
        ]
    },
    {
        "q": "드디어 금요일 오후 5시!",
        "options": [
            ("남은 일을 마무리하고 퇴근한다", "ace"),
            ("동료들에게 주말 인사를 건넨다", "peace"),
            ("컴퓨터 끄고 누구보다 빠르게 퇴근!", "lazy"),
            ("퇴근 후 약속을 잡으러 간다", "fun")
        ]
    },
    {
        "q": "회사 생활에서 가장 중요한 것은?",
        "options": [
            ("성과와 성장 📈", "ace"),
            ("좋은 사람들과의 관계 💗", "peace"),
            ("시간 대비 효율과 여유 🛋️", "lazy"),
            ("즐거움과 재미 🎊", "fun")
        ]
    }
]

# 결과 데이터
results = {
    "ace": {
        "name": "🏆 회사 에이스형",
        "subtitle": "일잘러 DNA가 기본 장착된 타입",
        "desc": "책임감이 강하고 목표를 달성하는 데 집중해요. 맡은 일은 끝까지 해내는 편이라 주변의 신뢰를 얻기 쉬워요.",
        "strength": "계획력, 실행력, 책임감",
        "weakness": "모든 일을 혼자 책임지려다 지칠 수 있어요.",
        "tip": "가끔은 다른 사람에게 맡기는 것도 능력이에요!"
    },
    "peace": {
        "name": "🕊️ 평화주의자형",
        "subtitle": "우리 팀 사이좋게 지내요!",
        "desc": "사람들의 감정과 관계를 중요하게 생각해요. 갈등을 줄이고 서로 협력할 수 있는 분위기를 만드는 데 강해요.",
        "strength": "공감 능력, 협업, 배려",
        "weakness": "싫은 소리를 못 해서 일을 떠안을 수 있어요.",
        "tip": "모든 사람을 만족시킬 필요는 없어요. 내 의견도 소중해요!"
    },
    "lazy": {
        "name": "☕ 효율 추구형 월급 루팡",
        "subtitle": "일은 적게, 효율은 높게!",
        "desc": "불필요한 절차를 싫어하고 가장 빠르고 편한 방법을 찾는 타입이에요. 효율적인 업무 방식에 재능이 있을 수 있어요.",
        "strength": "효율성, 현실 감각, 우선순위 판단",
        "weakness": "귀찮은 일을 미루다가 마감에 쫓길 수 있어요.",
        "tip": "미루기 전에 5분만 시작해 보세요. 의외로 금방 끝날지도!"
    },
    "fun": {
        "name": "🎉 분위기 메이커형",
        "subtitle": "우리 회사의 인간 비타민",
        "desc": "밝은 에너지와 아이디어로 주변에 활력을 줘요. 딱딱한 분위기를 부드럽게 바꾸는 데 강점이 있어요.",
        "strength": "창의성, 친화력, 긍정 에너지",
        "weakness": "재미있는 일에 집중하다가 세부 사항을 놓칠 수 있어요.",
        "tip": "재미와 체크리스트를 함께 활용하면 최고의 조합이에요!"
    }
}

if "question_index" not in st.session_state:
    st.session_state.question_index = 0
    st.session_state.answers = []
    st.session_state.game_round = 0

st.title("🏢 나의 회사 생활 유형 테스트")
st.caption("8가지 회사 상황으로 알아보는 나의 직장 캐릭터!")
st.progress(
    min(st.session_state.question_index / len(questions), 1.0)
)

if st.session_state.question_index < len(questions):
    i = st.session_state.question_index
    question = questions[i]

    st.markdown(f"### Q{i + 1}. {question['q']}")
    st.write("가장 나다운 선택 하나를 골라 봐!")

    options = question["options"]
    selected = st.radio(
        "선택지",
        options=range(len(options)),
        format_func=lambda n: options[n][0],
        key=f"question_{st.session_state.game_round}_{i}",
        label_visibility="collapsed"
    )

    if st.button("다음 질문 ➜", type="primary", use_container_width=True):
        st.session_state.answers.append(options[selected][1])
        st.session_state.question_index += 1
        st.rerun()

else:
    scores = {
        kind: st.session_state.answers.count(kind)
        for kind in results
    }
    winner = max(scores, key=scores.get)
    result = results[winner]

    st.balloons()
    st.success("테스트 완료! 당신의 결과는...")
    st.title(result["name"])
    st.subheader(result["subtitle"])
    st.write(result["desc"])

    st.markdown("### 💪 나의 강점")
    st.write(result["strength"])

    st.markdown("### 🤔 조심할 점")
    st.write(result["weakness"])

    st.markdown("### 💡 회사 생활 꿀팁")
    st.info(result["tip"])

    st.markdown("### 📊 나의 성향 점수")
    for kind, score in scores.items():
        st.write(f"{results[kind]['name']} — {score}점")
        st.progress(score / len(questions))

    share_text = (
        f"나의 회사 생활 유형은 {result['name']}!\n"
        f"{result['subtitle']}\n{result['desc']}"
    )

    st.markdown("### 📣 친구에게 결과 공유하기")
    st.code(share_text, language=None)
    st.caption("위 결과를 복사해서 친구에게 보내 봐!")

    if st.button("🔄 다시 테스트하기", use_container_width=True):
        st.session_state.question_index = 0
        st.session_state.answers = []
        st.session_state.game_round += 1
        st.rerun()

st.divider()
st.caption("※ 재미를 위한 테스트이며 실제 업무 능력을 진단하는 검사는 아닙니다.")