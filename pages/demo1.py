import streamlit as st
#langchain调用大模型，导入langchain的代码
from langchain_openai import ChatOpenAI
st.title("AI demo小程序")
model=ChatOpenAI(
    temperature=0.8,
    model="glm-4-plus",
    base_url="https://open.bigmodel.cn/api/paas/v4/",
    api_key="cea8acbc4cf7c069ff1bbdb7bfa4fefa.gZVpuDGVp8MpQwfz", #账号密码（在职谱上查）
)
if "cache" not in st.session_state:
    st.session_state.cache = []
else:
    for message in st.session_state.cache:
        with st.chat_message(message['role']):
            st.write(message['content'])

#创建一个聊天框

problem=st.chat_input("请输入你的问题")
#判断是用来确定用户有没有输入问题，如果输入问题
if problem:
    #1.将用户的问题输出到界面上，以用户的角色输出
    with st.chat_message("user"):
        st.write(problem)
        result = model.invoke(problem)
    #2.可用
    with st.chat_message("assistant"):
       st.write(result.content)
    st.session_state.cache.append({'role':"assistant","content":result.content})