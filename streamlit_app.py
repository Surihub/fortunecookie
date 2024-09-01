import streamlit as st
import pandas as pd
import random

st.title("🥠 포춘쿠키 하나 먹어보세요!")
st.success(
    "시험 기간 지친 여러분을 위해 선생님이 포춘쿠키를 준비했어요."
)

st.subheader("포춘쿠키 열어보기")

import pandas as pd
messages = pd.read_csv("./messages/study.csv")
# st.write(messages) # 잘 불러와졌는지 확인하기

open_cookie = st.button("포춘쿠키 확인하기")

st.subheader("포춘쿠키 확인하기")

import random
import time

# 버튼 클릭 시 이미지와 문구 표시
if open_cookie:
    # 이미지와 "잠시만 기다리세요..." 문구를 표시할 공간 예약
    placeholder = st.empty()

    # 이미지와 문구를 표시
    with placeholder.container():
        st.image("https://media0.giphy.com/media/gj6CShIcK24SnOWi40/giphy.gif?cid=6c09b952tdfy8qpe35xjzeora63k8ppdot47bgnxd4nusv2y&ep=v1_gifs_search&rid=giphy.gif&ct=g", width=250)
        st.write("포춘쿠키를 여는 중 입니다.... ")

    # 3초 동안 대기
    time.sleep(3)

    # 이미지를 제거하고 메시지 표시
    placeholder.empty()  # 이미지와 문구를 제거
    fortune = random.choice(messages['message'])
    st.warning(f"오늘의 운세: **{fortune}**", icon="🔮")