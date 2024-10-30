#基于历史聊天记录的对话模型
import streamlit as st
from langchain.chains.llm import LLMChain
#引入一个记忆模块对象
from langchain.memory import ConversationBufferMemory
#langchain调用大模型，导入langchain的代码
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
model=ChatOpenAI(
    temperature=0.8,
    model="glm-4-plus",
    base_url="https://open.bigmodel.cn/api/paas/v4/",
    api_key="cea8acbc4cf7c069ff1bbdb7bfa4fefa.gZVpuDGVp8MpQwfz", #账号密码（在职谱上查）
)
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory()
memory=ConversationBufferMemory(memory_key="history")
prompt=PromptTemplate.from_template("你叫克拉，你现在扮演的是一个朋友的角色，你现在要和你的朋友对话，你朋友的话是{input}，你需要对你的朋友的话做出回应，而且只做回应，你和你朋友的历史对话为{history}")
chain=LLMChain(
    llm=model,
    prompt=prompt,
    memory=st.session_state.memory,
)
st.title("小十七正在为您服务")


if "cache" not in st.session_state:
    st.session_state.cache = []
else:
    for message in st.session_state.cache:
        with st.chat_message(message['role']):
            st.write(message['content'])

#创建一个聊天框

problem=st.chat_input("你的小十七正在等待你的回应")
#判断是用来确定用户有没有输入问题，如果输入问题
if problem:
    #1.将用户的问题输出到界面上，以用户的角色输出
    with st.chat_message("user"):
        st.write(problem)
    st.session_state.cache.append({'role': "assistant", "content": problem})
    result=chain.invoke({"input": problem})
    #2.可用
    with st.chat_message("assistant"):
       st.write(result)
    st.session_state.cache.append({'role':"assistant","content":result})
