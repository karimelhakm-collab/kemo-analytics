import streamlit as st
import pandas as pd
import os

# 1. إعداد الصفحة
st.set_page_config(page_title="KH Analyzer Pro", layout="wide")

# 2. كود إظهار اللوجو من الفولدر
logo_path = "logo.png.png" # تأكد إن الاسم ده هو نفس اسم الصورة في الفولدر

if os.path.exists(logo_path):
    st.image(logo_path, width=150)
else:
    st.error("⚠️ صورة اللوجو (logo.png) مش موجودة في الفولدر!")

# 3. العنوان والشكل
st.markdown("""
<style>
    .main-title { color: #f1c40f; text-align: center; font-size: 40px; font-weight: bold; }
    .stApp { background-color: #0e1117; color: white; }
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>💎 نظام KH للتحليل الذكي</div>", unsafe_allow_html=True)

# 4. رفع الملف
uploaded_file = st.file_uploader("ارفع ملف الإكسيل هنا", type=['xlsx'])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.success("✅ تم رفع البيانات")

    st.table(df)
