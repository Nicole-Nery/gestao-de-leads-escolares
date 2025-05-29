import streamlit as st
from db import supabase
from cabecalho import *

conexao_e_cabecalho()

col1, col2 = st.columns([4,1])

with col1:
    st.write("Olá")

with col2:
    st.page_link("2_📋_Leads", label="Cadastrar Lead")
    
