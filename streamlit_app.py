import streamlit as st
from auth.funcoes_auth import *
from login_page import *

st.set_page_config(page_title= "Gestão de Leads", layout = "wide")

# Estilo CSS
with open("style/main.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Fluxo - Login ou cadastro
if "usuario" not in st.session_state:
    mostrar_tela_login_ou_cadastro()
    st.stop()

# Se já está autenticado, direciona para home
st.switch_page("pages/1_🏠_Home.py") 
