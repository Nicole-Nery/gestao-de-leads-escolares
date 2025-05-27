import streamlit as st
from db import supabase

def show_home():
    # Estilo CSS
    caminho_css = "style/main.css"
    with open(caminho_css) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    st.title("Bem-vindo ao Painel de Gestão de Leads")
    st.write("Escolha uma funcionalidade abaixo:")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("📋 Ver Leads"):
            st.session_state["modo"] = "leads"
            st.rerun()

    with col2:
        if st.button("💬 Interações"):
            st.session_state["modo"] = "interacoes"
            st.rerun()

    with col3:
        if st.button("📊 Dashboard"):
            st.session_state["modo"] = "dashboard"
            st.rerun()

    st.markdown("---")
    if st.button("⚙️ Configurações"):
        st.session_state["modo"] = "configuracoes"
        st.rerun()
