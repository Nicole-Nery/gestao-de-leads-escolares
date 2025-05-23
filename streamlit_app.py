import streamlit as st
from home import show_home
from funcoes_login import *

st.set_page_config(page_title= "Título", 
                layout = "wide")

# Estilo CSS
caminho_css = "style/main.css"
with open(caminho_css) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Modos
modos_validos = ["login", "cadastro", "home"]

if "modo" not in st.session_state or st.session_state["modo"] not in modos_validos:
    st.session_state["modo"] = "login"

modo = st.session_state.get("modo", "login")

if modo in ["login", "cadastro"]:
    st.markdown("""
        <style>
            .block-container {
                padding-top: 5vh;
                max-width: 700px;
                margin: auto;
            }
        </style>
    """, unsafe_allow_html=True)

# Fluxo principal -------
if "usuario" not in st.session_state:
    if st.session_state["modo"] == "login":
        login()
    else:
        cadastro()
    st.stop()

# Exibe a tela de acordo com o modo atual
if st.session_state["modo"] == "login":
    login()
elif st.session_state["modo"] == "cadastro":
    cadastro()
elif st.session_state["modo"] == "home":
    show_home()

usuario = st.session_state.usuario
