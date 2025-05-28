import streamlit as st
from db import supabase
from cabecalho import *

conexao_e_cabecalho()

col1, col2, col3 = st.columns(3)

with col1:
    st.page_link("pages/2_📋_Leads.py", label="Gerenciar Leads", icon="📋")

with col2:
    st.page_link("pages/3_💬_Interações.py", label="Histórico de Interações", icon="💬")

with col3:
    st.page_link("pages/4_📊_KPIs.py", label="Painel de KPIs", icon="📊")
