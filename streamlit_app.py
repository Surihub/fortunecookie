import streamlit as st
import pandas as pd
import random
import time
from openai import OpenAI

st.title("🥠 포춘쿠키 하나 먹어보세요!")
st.success(
    "시험 기간 지친 여러분을 위해 선생님이 포춘쿠키를 준비했어요. **by 🌝황수빈T**"
)

st.subheader("포춘쿠키 열어보기")

# 학생들의 기분 선택
mood = st.radio(
    "지금 기분이 어떤가요?",
    ("😎자신감 뿜뿜!", "😱불안해요...", "😳긴장돼요!", "🫠아무 생각 없어요")
)

# 포춘쿠키 열기 버튼
open_cookie = st.button("포춘쿠키 확인하기")

# 버튼 클릭 시 맞춤형 문구 생성
if open_cookie:
    # 이미지와 "잠시만 기다리세요..." 문구를 표시할 공간 예약
    placeholder = st.empty()

    # 이미지와 문구를 표시
    with placeholder.container():
        st.image("https://media0.giphy.com/media/gj6CShIcK24SnOWi40/giphy.gif?cid=6c09b952tdfy8qpe35xjzeora63k8ppdot47bgnxd4nusv2y&ep=v1_gifs_search&rid=giphy.gif&ct=g", width=250)
        st.write("포춘쿠키를 여는 중 입니다.... ")

    # 3초 동안 대기
    time.sleep(1)

    # OpenAI API 프롬프트
    prompt = f"오늘 모의고사를 보는 학생들에게 힘을 줄 수 있는 감동적인 응원을 해줘. 편안한 마음으로 보되 그래도 긴장을 너무 안하진 말고 끝까지 열심히 풀고 최선을 다 할 수 있도록! 학생들의 기분은 '{mood}'이므로 이 기분을 고려해서 그에 적절한 응원을 해줘야해. 두 문장으로 말해줘."

    client = OpenAI(api_key=st.secrets.OpenAI.apikey)

    # OpenAI API 호출하여 문구 생성
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
            "role": "system",
            "content": [
                {
                "type": "text",
                "text": prompt,
                }
            ]
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        response_format={
            "type": "text"
        }
        )
    

    # 생성된 문구 추출
    fortune = response.choices[0].message.content

    # 이미지를 제거하고 맞춤형 메시지 표시
    placeholder.empty()  # 이미지와 문구를 제거
    st.balloons()
    st.warning(f"오늘의 운세: **{fortune}**", icon="🔮")