import streamlit as st
from auth.funcoes_login import *

st.set_page_config(page_title= "Gestão de Leads", layout = "wide")

# Estilo CSS
with open("style/main.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Modos
modos_validos = ["login", "cadastro", "home", "leads"]

if "modo" not in st.session_state or st.session_state["modo"] not in modos_validos:
    st.session_state["modo"] = "login"

modo = st.session_state.get("modo", "login")

if modo in ["login"]:
    st.markdown("""
        <style>
            .block-container {
                padding-top: 5vh;
                max-width: 500px;
                margin: auto;
            }
        </style>
    """, unsafe_allow_html=True)

if modo in ["cadastro"]:
    st.markdown("""
        <style>
            .block-container {
                padding-top: 5vh;
                max-width: 900px;
                margin: auto;
            }
        </style>
    """, unsafe_allow_html=True)

# Fluxo - Login ou cadastro
if "usuario" not in st.session_state:
    if st.session_state["modo"] == "login":
        login()
    else:
        cadastro()
    st.stop()

st.switch_page("pages/1_🏠_Home.py") 
