import streamlit as st
from db import supabase

st.markdown("""
        <style>
        /* Oculta o texto da página ativa na sidebar */
        [data-testid="stSidebarNav"] ul li:first-child a span {
            display: none;
        }
        </style>
    """, unsafe_allow_html=True)

st.set_page_config(page_title="Leads", layout="wide")

# Estilo CSS
with open("style/main.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
if "usuario" not in st.session_state:
    st.error("Você precisa estar logado para acessar esta página.")
    st.stop()

st.title("📋 Gerenciamento de Leads")
st.info("Aqui você poderá cadastrar, visualizar, editar e excluir leads.")
