import streamlit as st

# 페이지 설정
st.set_page_config(page_title="MBTI 진로 & 조합 추천", page_icon="🌟", layout="centered")

# 메인 화면
st.title("🌟 MBTI 기반 진로 및 조합 추천 사이트")
st.markdown("""
안녕하세요! 이 웹사이트는 여러분의 MBTI를 기반으로  
- **💼 적합한 직업 추천**
- **🤝 궁합이 잘 맞는 조합 추천**  

을 도와주는 교육용 웹앱입니다.

좌측 사이드바에서 기능을 선택해 주세요! 👈
""")

st.image("https://cdn-icons-png.flaticon.com/512/2721/2721264.png", width=200)
