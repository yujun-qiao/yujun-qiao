import streamlit as st
st.title("AIcomeing~~~")
col,col1,col2=st.columns(3)
#语言大模型应用程序入口
with col:
    st.image("ZLY1.jfif",use_column_width=True)#图片尽量找大小一样的
    flag=st.button("御乔畅言",use_container_width=True)
    if flag:
        st.switch_page("pages/youhui.py")
#文生图大模型应用程序入口
with col1:
    st.image("ZLY1.jfif", use_column_width=True)
    flag = st.button("御乔绘图",use_container_width=True)
    if flag:
        st.switch_page("pages/textToimage.py")
with col1:
    st.image("ZLY1.jfif", use_column_width=True)
    flag = st.button("职业问答",use_container_width=True)
    if flag:
        st.switch_page("pages/job-ai.py")
# c1,c2,c3,c4,c5=st.columns(5)
# with c1:
#    flag= st.button("基础版")
#    if flag:
#         st.switch_page("pages/demo.py")
# with c2:
#     flag1=st.button("进阶版1")
#     if flag1:
#         st.switch_page("pages/demo1.py")
# with c3:
#     flag2=st.button("进阶版2")
#     if flag2:
#         st.switch_page("pages/demo2.py")
# with c4:
#     flag3=st.button("最终版")
#     if flag3:
#         st.switch_page("pages/.py")
# with c5:
#     flag4 = st.button("文生图")
#     if flag4:
#         st.switch_page("pages/textToimage.py")
