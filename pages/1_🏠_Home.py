import streamlit as st
from db import supabase
from cabecalho import *

conexao_e_cabecalho()

col1, col2 = st.columns([4,1])

with col1:
    st.write("Olá")

with col2:
    st.link_button("📋 Cadastrar Lead", url="/pages/2_📋_Leads")
    st.link_button("💬 Histórico de Interações", url="/pages/3_💬_Interações")
    st.link_button("📊 Painel de KPIs", url="/pages/4_📊_KPIs")
