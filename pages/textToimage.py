import streamlit as st
from zhipuai import ZhipuAI
model=ZhipuAI(api_key="cea8acbc4cf7c069ff1bbdb7bfa4fefa.gZVpuDGVp8MpQwfz")

if "cache" not in st.session_state:
    st.session_state.cache = []
else:
    for message in st.session_state.cache:
        if message['role']== "user":
            with st.chat_message(message['role']):
                st.write(message['content'])
        else:
            with st.chat_message("assistant"):
                st.image(message["content"], width=200)
st.title("文生图小程序")
#创建输入框
desc=st.chat_input("请输入图片的描述")
if desc:
    with st.chat_message("user"):
        st.write(desc)
    st.session_state.cache.append({"role":"assistant","content":desc})
    #调用智谱AI的文生图大模型生成图片
    response=model.images.generations(
        model="cogview-3-plus",
        prompt=desc,
    )
    with st.chat_message("assistant"):
        image_data = response.data[0]
        st.image(image_data.url, width=300)
     # 将图片url写入cache
    st.session_state.cache.append({"role": "assistant", "content": image_data.url})