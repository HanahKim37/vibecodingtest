import streamlit as st
import random
from itertools import combinations

# MBTI 궁합 매핑
mbti_match = {
    "INFP": ["ENFJ", "ENFP"],
    "ENFP": ["INFP", "INFJ", "INTJ", "INTP"],
    "INFJ": ["ENFP", "ENTP"],
    "ENFJ": ["INFP", "ISFP"],
    "INTJ": ["ENTP", "ENFP"],
    "ENTP": ["INFJ", "INTJ", "INTP"],
    "ISTJ": ["ESFP", "ISFJ"],
    "ISFJ": ["ESFP", "ESTP"],
    "ESTJ": ["ISFP", "ISTP"],
    "ESFJ": ["ISFP", "INFP"],
    "ISTP": ["ESFJ", "ENFP"],
    "ISFP": ["ESTJ", "ENFJ", "ESFJ"],
    "ESTP": ["INFP", "ISFJ"],
    "ESFP": ["ISTJ", "ISFJ"],
    "INTP": ["ENTP", "ENFP"],
    "ENTJ": ["INTP", "ENFP"]
}

# 페이지 설정
st.set_page_config(page_title="MBTI 조합 추천", page_icon="🤝", layout="centered")
st.title("🤝 MBTI 궁합 기반 조 추천 앱")

# 인원 수 입력
num_people = st.number_input("몇 명인가요?", min_value=2, max_value=20, step=1)

# 이름 + MBTI 입력받기
st.subheader("👥 각 사람의 이름과 MBTI를 입력하세요")
people = []
for i in range(num_people):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input(f"이름 {i+1}", key=f"name_{i}")
    with col2:
        mbti = st.selectbox(f"MBTI {i+1}", sorted(mbti_match.keys()), key=f"mbti_{i}")
    if name and mbti:
        people.append((name, mbti))

# 버튼을 누르면 조합 추천 실행
if st.button("✨ 좋은 조 추천 받기"):
    if len(people) < 2:
        st.warning("최소 2명 이상 입력해주세요!")
    else:
        st.subheader("💡 추천 조합 결과")

        # 가능한 모든 2인 조합
        pairs = list(combinations(people, 2))

        # 점수 매기기 (궁합일 경우 +1)
        scored_pairs = []
        for (p1, m1), (p2, m2) in pairs:
            score = 1 if m2 in mbti_match.get(m1, []) or m1 in mbti_match.get(m2, []) else 0
            scored_pairs.append(((p1, m1), (p2, m2), score))

        # 출력: 궁합이 맞는 쌍 먼저 보여주기
        good_pairs = [((a[0], b[0]), score) for a, b, score in scored_pairs if score > 0]
        other_pairs = [((a[0], b[0]), score) for a, b, score in scored_pairs if score == 0]

        if good_pairs:
            st.markdown("### 🟢 서로 잘 맞는 조")
            for (name1, name2), _ in good_pairs:
                st.success(f"✅ {name1} 🤝 {name2}")
        else:
            st.markdown("### ⚪️ 특별히 잘 맞는 조합은 없지만, 이 조들도 고려해보세요!")

        if other_pairs:
            st.markdown("### ⚪️ 일반 조합")
            for (name1, name2), _ in other_pairs:
                st.info(f"{name1} 🤝 {name2}")
