import streamlit as st

# 大标题
st.title("陈都灵")
st.header("陈都灵天下第一")
st.subheader("陈都灵世一萌")

#段落文字:
st.write("<左耳>")
st.write("医学专家说,左耳靠近心脏,甜言蜜语要说给左耳听,如果有个人,对我的左耳说甜言蜜语,即使听不到也没关系")

#图像
st.image(image="./resource/Screenshot_20260703_010621.jpg",width=300)
st.image(image="./resource/Screenshot_20260703_004812.jpg",width=300)
st.image(image="./resource/Screenshot_20260703_004906.jpg",width=300)

#视频
st.video("./resource/video_20260703_003031.mp4")
#logo
st.logo("./resource/IMG_20260706_125910.jpg")

#表格
actor_data = {
    "姓名": ["陈都灵"],
    "出生日期": ["1993年10月18日"],
    "出生地": ["福建省厦门市"],
    "首部出道作品": ["电影《左耳》（2015年上映）"],
    "毕业院校": ["南京航空航天大学 飞行器制造工程专业"]
}

#图片
st.image(image="./resource/",width=300)
