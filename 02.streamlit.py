from operator import length_hint

import streamlit as st

# 大标题
st.title("陈都灵")
st.header("陈都灵天下第一")

st.subheader("陈都灵世一萌")

#段落文字:
st.write("<左耳>")
st.write("医学专家说,左耳靠近心脏,甜言蜜语要说给左耳听,如果有个人,对我的左耳说甜言蜜语,即使听不到也没关系")

#图像
st.image(image="./新建文件夹/resource/Screenshot_20260703_010621.jpg",width=300)
st.video("./新建文件夹/resource/video_20260703_003031.mp4")
st.logo("./新建文件夹/resource/IMG_20260706_125910.jpg")

#视频
st.video("./resource/video_20260703_003031.mp4")
#logo
st.logo("./resource/IMG_20260706_125910.jpg")
