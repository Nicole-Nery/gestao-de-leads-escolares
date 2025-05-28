import streamlit as st
from db import supabase

# Estilo CSS
with open("style/main.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
if "usuario" not in st.session_state:
    st.error("Você precisa estar logado para acessar esta página.")
    st.stop()

st.title("📋 Gerenciamento de Leads")
st.info("Aqui você poderá cadastrar, visualizar, editar e excluir leads.")
