import streamlit as st

if "usuario" not in st.session_state:
    st.switch_page("pages/0_🔐_Login.py")

st.title("KPI's")
