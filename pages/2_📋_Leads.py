import streamlit as st
from db import supabase
from cabecalho import *

conexao_e_cabecalho()

st.subheader("Gerenciamento de Leads")

tabs_leads = st.tabs(["Cadastrar", "Visualizar", "Atualizar", "Excluir"])

with tabs_leads[0]:
    with st.form("form_cadastro_leads"):
        st.subheader("👨‍👩‍👧 Informações dos Responsáveis")
        nome_responsavel = st.text_input("Nome do responsável")
        telefone = st.text_input("Telefone de contato")
        email = st.text_input("E-mail")

        st.markdown("---")


        st.subheader("📌 Informações do Aluno")
        nome = st.text_input("Nome do aluno")
        idade = st.number_input("Idade", min_value=0)
        escola_origem = st.text_input("Nome do aluno")



