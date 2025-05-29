import streamlit as st
from db import supabase
from cabecalho import *

conexao_e_cabecalho()

col1, col2 = st.columns([4,1])

with col1:
    st.write("Olá")

with col2:
    #st.link_button("Cadastrar Lead", url="/pages/2_📋_Leads", new_tab=False)
    st.page_link("pages/2_📋_Leads.py", label="Cadastrar Lead", icon="➕", new_tab=False)
