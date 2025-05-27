import streamlit as st

st.set_page_config(page_title="Leads", layout="wide")

if "usuario" not in st.session_state:
    st.switch_page("0_🔐_Login.py")

st.title("📋 Gerenciamento de Leads")
st.info("Aqui você poderá cadastrar, visualizar, editar e excluir leads.")
