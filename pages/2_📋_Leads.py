import streamlit as st
from db import supabase
from cabecalho import *

conexao_e_cabecalho()

st.html("<div class='subtitle'>Gerenciamento de Leads</div>")

tabs_leads = st.tabs(["Cadastrar", "Visualizar", "Atualizar", "Excluir"])

with tabs_leads[0]:
    with st.form("form_cadastro_leads", clear_on_submit=True):
        st.html("<div class='subsubtitle'>Informações do responsável</div>")
        nome_responsavel = st.text_input("Nome do responsável")
        telefone = st.text_input("Telefone de contato")
        email = st.text_input("E-mail")
        profissao = st.text_input("Profissão")

        st.markdown("---")

        st.html("<div class='subsubtitle'>Informações do aluno</div>")
        nome = st.text_input("Nome do aluno")
        idade = st.number_input("Idade", min_value=0)
        escola_origem = st.text_input("Escola de origem")
        serie_interesse = st.selectbox("Série de interesse", ["Maternal II", "Maternal III", "1° período", "2° período", "1° ano", "2° ano", "3° ano", "4° ano", "5° ano", "6° ano", "7° ano", "8° ano", "9° ano"], placeholder="Selecione")

        st.markdown("---")
        
        st.html("<div class='subsubtitle'>Informações do status do Lead</div>")
        status_atual = st.selectbox("Etapa atual do Lead", ["A", "B", "C"],placeholder="Selecione")
        responsavel_nome = st.selectbox("Profissional responsável por essa etapa", ["Fulano", "Ciclano", "Beltrano"], placeholder="Selecione")
        lead_finalizado = st.radio("Lead finalizado?",["Não", "Sim"], horizontal=True)

        consentimento_lgpd = st.checkbox("O responsável declara estar ciente e de acordo com o uso dos dados fornecidos para fins de contato, registro e comunicação institucional, conforme a Lei Geral de Proteção de Dados (LGPD).")

        submit = st.form_submit_button("Cadastrar Lead")

        if submit:
            if consentimento_lgpd:
                st.success("Lead cadastrado com sucesso.")
            else:
                st.error("É necessário o consentimento LGPD para prosseguir.")



