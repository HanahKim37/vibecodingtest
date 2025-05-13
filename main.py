import streamlit as st

# 🎨 앱 설정
st.set_page_config(page_title="🌟 MBTI 진로 추천 웹앱", page_icon="💼", layout="wide")

# 🎆 헤더
st.markdown("""
    <h1 style='text-align: center; color: #6c5ce7;'>✨ MBTI로 알아보는 나의 진로 ✨</h1>
    <p style='text-align: center; font-size: 20px;'>당신의 MBTI를 선택하면, 어울리는 직업을 화려하게 추천해드려요! 💡🚀</p>
""", unsafe_allow_html=True)

# 🧠 MBTI 목록과 직업 매칭
mbti_jobs = {
    "INTJ": ("전략 컨설턴트 🧠", "연구원 🔬", "시스템 설계자 🧩"),
    "INTP": ("데이터 과학자 📊", "이론 물리학자 ⚛️", "프로그래머 💻"),
    "ENTJ": ("CEO 🧑‍💼", "프로젝트 매니저 🗂️", "변호사 ⚖️"),
    "ENTP": ("스타트업 창업가 🚀", "광고 기획자 🎨", "정치 분석가 🧭"),
    "INFJ": ("상담사 🧘‍♀️", "작가 ✍️", "교육자 👩‍🏫"),
    "INFP": ("시인 📜", "일러스트레이터 🎨", "사회복지사 ❤️"),
    "ENFJ": ("멘토 🌟", "홍보 담당자 📢", "교육 컨설턴트 🧑‍🏫"),
    "ENFP": ("브랜드 디자이너 🎨", "여행 작가 🌍", "인플루언서 📸"),
    "ISTJ": ("회계사 🧾", "공무원 🏛️", "데이터 분석가 📉"),
    "ISFJ": ("간호사 🏥", "교사 🧑‍🏫", "사서 📚"),
    "ESTJ": ("경영 관리자 🧑‍💼", "군 장교 🪖", "프로젝트 리더 📋"),
    "ESFJ": ("이벤트 기획자 🎉", "상담 교사 🧑‍🏫", "호텔 매니저 🏨"),
    "ISTP": ("기계공 🔧", "파일럿 🛫", "경찰 👮"),
    "ISFP": ("플로리스트 🌸", "사진작가 📷", "헤어디자이너 💇"),
    "ESTP": ("스포츠 트레이너 🏋️", "기업가 💼", "세일즈 전문가 📈"),
    "ESFP": ("연예인 🎤", "패션 디자이너 👗", "이벤트 플래너 🎪")
}

# 🌈 컬러풀 사이드바
st.sidebar.markdown("## 💖 당신의 MBTI는?")
mbti = st.sidebar.selectbox("MBTI 유형을 선택해주세요", list(mbti_jobs.keys()), index=0)

# 🎁 결과 카드
st.markdown("---")
st.subheader(f"💼 {mbti} 유형에게 어울리는 직업 추천 💼")

job_list = mbti_jobs[mbti]

# 💎 화려한 카드 형식 출력
for job in job_list:
    st.markdown(f"""
        <div style="background-color: #ffeaa7; padding: 20px; border-radius: 15px; margin-bottom: 10px; box-shadow: 2px 2px 10px rgba(0,0,0,0.1);">
            <h3 style="color: #2d3436;">{job}</h3>
        </div>
    """, unsafe_allow_html=True)

# 🌟 추가 정보
st.markdown("""
<hr>
<h4 style='text-align: center; color: #636e72;'>🎓 이 웹앱은 진로 교육을 위한 목적으로 제작되었습니다.</h4>
<p style='text-align: center;'>※ 직업 추천은 참고용입니다. 당신의 가능성은 무한하니까요! 🚀</p>
""", unsafe_allow_html=True)
