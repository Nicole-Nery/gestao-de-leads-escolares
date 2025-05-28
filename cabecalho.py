from pathlib import Path
import streamlit as st
from login_page import *

def conexao_e_cabecalho():
    if "usuario" not in st.session_state:
        st.error("Você precisa estar logado para acessar esta página.")
        st.stop()

    usuario = st.session_state["usuario"]

    # Botão de sair
    with st.sidebar:
        if st.button("🚪 Sair"):
            st.session_state.clear()
            mostrar_tela_login_ou_cadastro()
            st.rerun()

    # Caminhos absolutos baseados na raiz do projeto
    raiz = Path(__file__).parent
    css_path = raiz / "style" / "main.css"
    logo_path = raiz / "assets" / "logo-sigah.svg"

    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    '''with st.container():
        st.markdown('<div class="fixed-header">', unsafe_allow_html=True)
        col1, col2 = st.columns([1,5])
        with col1:
            st.image(str(logo_path), width=300)
        with col2:
            st.html("<div class='header-title'>Funil Inteligente de Leads</div>")
        st.markdown('</div>', unsafe_allow_html=True)

        st.title("Funil Inteligente de Leads Escolares")
        st.markdown(f"Bem-vindo, **{usuario['nome_usuario']}** ({usuario['cargo']})!")'''
    
    st.title("Funil Inteligente de Leads Escolares")
    st.markdown(f"Bem-vindo, **{usuario['nome_usuario']}** ({usuario['cargo']})!")

    st.markdown("---")
