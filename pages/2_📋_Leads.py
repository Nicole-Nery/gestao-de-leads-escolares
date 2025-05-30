import streamlit as st
from db import supabase
from cabecalho import *
from funcoes_crud import *
from funcoes_formatacao import *
import datetime
import pandas as pd

conexao_e_cabecalho()

st.html("<div class='subtitle'>Gerenciamento de Leads</div>")

tabs_leads = st.tabs(["Cadastrar", "Visualizar", "Atualizar", "Excluir"])

with tabs_leads[0]:
    with st.form("form_cadastro_leads", clear_on_submit=True):
        st.html("<div class='subsubtitle'>Informações do responsável</div>")
        nome_responsavel = st.text_input("Nome do responsável")
        grau_parentesco = st.radio("Grau de parentesco", ["Pai", "Mãe", "Outro"], horizontal=True)
        telefone = st.text_input("Telefone de contato")
        telefone_formatado = formatar_telefone(telefone)
        email = st.text_input("E-mail")
        profissao = st.text_input("Profissão")

        st.markdown("---")

        st.html("<div class='subsubtitle'>Informações do aluno</div>")
        nome_aluno = st.text_input("Nome do aluno")
        idade_aluno = st.number_input("Idade", min_value=0)
        data_nascimento_aluno = st.date_input("Data de nascimento", format="DD/MM/YYYY")
        escola_atual = st.text_input("Escola atual")
        serie_interesse = st.selectbox("Série de interesse", ["Maternal II", "Maternal III", "1° período", "2° período", "1° ano", "2° ano", "3° ano", "4° ano", "5° ano", "6° ano", "7° ano", "8° ano", "9° ano"], placeholder="Selecione", key='cadastrar_serie_interesse')
        especialista_acompanhante = st.selectbox("A criança é acompanhada por algum desses especialistas?", ["Neuropediatra", "Fonoaudióloga", "Terapeuta ocupacional", "Psiquiatra", "Psicopedagogo", "Psicólogo", "Não"], placeholder="Selecione", key='cadastrar_especialista_acompanhante')
        diagnostico = st.text_area("Tem algum diagnóstico? Especifique.")

        st.markdown("---")
        
        st.html("<div class='subsubtitle'>Informações do status do Lead</div>")
        canal_origem = st.selectbox("Por onde o Lead conheceu a Escola Colibri?", ["Instagram", "WhatsApp", "Facebook", "Linkedin", "Indicação", "Fachada (Passando pela rua)"], placeholder="Selecione", key='cadastrar_canal_origem')
        status_atual = st.selectbox("Etapa atual do Lead", ["A", "B", "C"], placeholder="Selecione", key='cadastrar_status_atual')
        profissional_responsavel = st.selectbox("Profissional responsável por essa etapa", ["Fulano", "Ciclano", "Beltrano"], placeholder="Selecione", key='cadastrar_responsavel_nome')
        lead_finalizado = st.radio("Matrícula realizada?", ["Não", "Sim"], horizontal=True)

        observacoes = st.text_area("Observações")

        st.markdown("---")

        consentimento_lgpd = st.checkbox("O responsável declara estar ciente e de acordo com o uso dos dados fornecidos para fins de contato, registro e comunicação institucional, conforme a Lei Geral de Proteção de Dados (LGPD).")

        # Criar o dicionário com os dados
        dict_leads = {
            "nome_responsavel": nome_responsavel,
            "grau_parentesco": grau_parentesco,
            "telefone": telefone_formatado,
            "email": email,
            "profissao": profissao,
            "nome_aluno": nome_aluno,
            "idade_aluno": idade_aluno,
            "data_nascimento_aluno": str(data_nascimento_aluno),
            "escola_atual": escola_atual,
            "serie_interesse": serie_interesse,
            "canal_origem": canal_origem,
            "status_atual": status_atual,
            "profissional_responsavel": profissional_responsavel,
            "lead_finalizado": lead_finalizado == "Sim", 
            "observacoes": observacoes,
            "consentimento_lgpd": consentimento_lgpd,
            "data_cadastro": str(datetime.date.today()) 
        }

        submit = st.form_submit_button("Cadastrar Lead")

        if submit:
            if consentimento_lgpd:
                st.success("Lead cadastrado com sucesso.")
            else:
                st.error("É necessário o consentimento LGPD para prosseguir.")

with tabs_leads[1]:
    leads_result = buscar_registro("leads", "nome_aluno")
    df_leads = pd.DataFrame(leads_result)
    df_leads = df_leads.drop(columns=["id"])
    st.dataframe(df_leads, height=500)



