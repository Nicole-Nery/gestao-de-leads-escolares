import streamlit as st
from db import supabase

if "usuario" not in st.session.state:
    st.warning("Você precisa estar logado para acessar esta página.")
    st.stop()

usuario = st.session_state["usuario"]

st.title("🏠 Painel Inicial")
st.markdown(f"Bem-vindo, **{usuario['nome_usuario']}** ({usuario['cargo']})!")

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.page_link("pages/2_📋_Leads.py", label="📋 Gerenciar Leads", icon="📋")

with col2:
    st.page_link("pages/3_💬_Interações.py", label="💬 Histórico de Interações", icon="💬")

with col3:
    st.page_link("pages/4_📊_KPIs.py", label="📊 Painel de KPIs", icon="📊")

# Adicionais no rodapé
st.markdown("### 📈 Em breve:")
st.markdown("- Funil de conversão")
st.markdown("- Alertas automáticos")
st.markdown("- Tarefas pendentes")

st.markdown("---")
if st.button("🚪 Sair"):
    st.session_state.clear()
    st.rerun()
