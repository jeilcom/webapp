from openai import OpenAI
#from dotenv import load_dotenv
import streamlit as st
#import os
# OpenAI API 키 설정
def chatbot(q):
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
    completion = client.chat.completions.create(
    model="gpt-4o-mini-2024-07-18",
    messages=[
        {"role": "system", "content": "너는 안동의 명물인지를 판별하는 봇이야. 맞다면 y 틀리면 n으로만 대답해줘"},
        {"role": "user", "content": q}
    ]
    )

    return (completion.choices[0].message.content)


question='안동에서 유명한 것은?'
answer=st.text_input(question)

if st.button("확인"):
    ans=chatbot(answer)
    if ans=='y':
        st.success('정답입니다.')
    else:
        st.error('오답입니다.')
    