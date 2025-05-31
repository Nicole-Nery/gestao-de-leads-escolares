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
    with st.form("form_cadastro_leads", clear_on_submit=False):
        st.html("<div class='subsubtitle'>Informações do responsável 1</div>")
        col1, col2 = st.columns([2,1])
        with col1:
            nome_responsavel_1 = st.text_input("Nome do responsável", key='nome_responsavel_1')
        with col2:
            grau_parentesco_1 = st.radio("Grau de parentesco", ["Pai", "Mãe", "Outro"], horizontal=True, key='parentesco_1')

        col1, col2, col3 = st.columns([1,1,1])
        with col1:
            telefone_1 = st.text_input("Telefone de contato", key='telefone_1')
            telefone_formatado_1 = formatar_telefone(telefone_1)
        with col2:
            email_1 = st.text_input("E-mail", key='email_1')
        with col3:
            profissao_1 = st.text_input("Profissão", key='profissao_1')

        st.html("<div class='subsubtitle'>Informações do responsável 2</div>")
        col1, col2 = st.columns([2,1])
        with col1:
            nome_responsavel_2 = st.text_input("Nome do responsável", key='nome_responsavel_2')
        with col2:
            grau_parentesco_2 = st.radio("Grau de parentesco", ["Pai", "Mãe", "Outro"], horizontal=True, key='parentesco_2')

        col1, col2, col3 = st.columns([1,1,1])
        with col1:
            telefone_2 = st.text_input("Telefone de contato", key='telefone_2')
            telefone_formatado_2 = formatar_telefone(telefone_2)
        with col2:
            email_2 = st.text_input("E-mail", key='email_2')
        with col3:
            profissao_2 = st.text_input("Profissão", key='profissao_2')
        
        st.markdown("---")

        st.html("<div class='subsubtitle'>Informações do aluno 1</div>")
        col1, col2 = st.columns([2,1])
        with col1:
            nome_aluno_1 = st.text_input("Nome do aluno", key='nome_aluno_1')
        with col2:
            idade_aluno_1 = st.number_input("Idade", min_value=0, key='idade_aluno_1')
        
        col1, col2, col3 = st.columns([1,1,1])
        with col1:
            data_nascimento_aluno_1 = st.date_input("Data de nascimento", format="DD/MM/YYYY",  min_value=datetime.date(1930, 1, 1),
    max_value=datetime.date.today(), key='data_nascimento_aluno_1')
        with col2:
            escola_atual_1 = st.text_input("Escola atual", key='escola_atual_1')
        with col3:
            serie_interesse_1 = st.selectbox("Série de interesse", ["Maternal II", "Maternal III", "1° período", "2° período", "1° ano", "2° ano", "3° ano", "4° ano", "5° ano", "6° ano", "7° ano", "8° ano", "9° ano"], placeholder="Selecione", key='cadastrar_serie_interesse_1')
        
        especialista_acompanhante_1 = st.selectbox("A criança é acompanhada por algum desses especialistas?", ["Neuropediatra", "Fonoaudióloga", "Terapeuta ocupacional", "Psiquiatra", "Psicopedagogo", "Psicólogo", "Não"], placeholder="Selecione", key='cadastrar_especialista_acompanhante_1')
        diagnostico_1 = st.text_area("Tem algum diagnóstico? Especifique.", key='diagnostico_aluno_1')

        st.html("<div class='subsubtitle'>Informações do aluno 2</div>")
        col1, col2 = st.columns([2,1])
        with col1:
            nome_aluno_2 = st.text_input("Nome do aluno", key='nome_aluno_2')
        with col2:
            idade_aluno_2 = st.number_input("Idade", min_value=0, key='idade_aluno_2')
        
        col1, col2, col3 = st.columns([1,1,1])
        with col1:
            data_nascimento_aluno_2 = st.date_input("Data de nascimento", format="DD/MM/YYYY", key='data_nascimento_aluno_2', min_value=datetime.date(1930, 1, 1), max_value=datetime.date.today())
        with col2:
            escola_atual_2 = st.text_input("Escola atual", key='escola_atual_2')
        with col3:
            serie_interesse_2 = st.selectbox("Série de interesse", ["Maternal II", "Maternal III", "1° período", "2° período", "1° ano", "2° ano", "3° ano", "4° ano", "5° ano", "6° ano", "7° ano", "8° ano", "9° ano"], placeholder="Selecione", key='cadastrar_serie_interesse_2')
        
        especialista_acompanhante_2 = st.selectbox("A criança é acompanhada por algum desses especialistas?", ["Neuropediatra", "Fonoaudióloga", "Terapeuta ocupacional", "Psiquiatra", "Psicopedagogo", "Psicólogo", "Não"], placeholder="Selecione", key='cadastrar_especialista_acompanhante_2')
        diagnostico_2 = st.text_area("Tem algum diagnóstico? Especifique.", key='diagnostico_aluno_2')


        st.html("<div class='subsubtitle'>Informações do aluno 3</div>")
        col1, col2 = st.columns([2,1])
        with col1:
            nome_aluno_3 = st.text_input("Nome do aluno", key='nome_aluno_3')
        with col2:
            idade_aluno_3 = st.number_input("Idade", min_value=0, key='idade_aluno_3')
        
        col1, col2, col3 = st.columns([1,1,1])
        with col1:
            data_nascimento_aluno_3 = st.date_input("Data de nascimento", format="DD/MM/YYYY", key='data_nascimento_aluno_3', min_value=datetime.date(1930, 1, 1), max_value=datetime.date.today())
        with col2:
            escola_atual_3 = st.text_input("Escola atual", key='escola_atual_3')
        with col3:
            serie_interesse_3 = st.selectbox("Série de interesse", ["Maternal II", "Maternal III", "1° período", "2° período", "1° ano", "2° ano", "3° ano", "4° ano", "5° ano", "6° ano", "7° ano", "8° ano", "9° ano"], placeholder="Selecione", key='cadastrar_serie_interesse_3')
        
        especialista_acompanhante_3 = st.selectbox("A criança é acompanhada por algum desses especialistas?", ["Neuropediatra", "Fonoaudióloga", "Terapeuta ocupacional", "Psiquiatra", "Psicopedagogo", "Psicólogo", "Não"], placeholder="Selecione", key='cadastrar_especialista_acompanhante_3')
        diagnostico_3 = st.text_area("Tem algum diagnóstico? Especifique.", key='diagnostico_aluno_3')


        st.markdown("---")
        
        st.html("<div class='subsubtitle'>Informações do status do Lead</div>")
        canal_origem = st.selectbox("Por onde o Lead conheceu a Escola Colibri?", ["Instagram", "WhatsApp", "Facebook", "Linkedin", "Indicação", "Fachada (Passando pela rua)"], placeholder="Selecione", key='cadastrar_canal_origem')
        col1, col2, col3 = st.columns([1,1,1])
        with col1:
            status_atual = st.selectbox("Etapa atual do Lead", ["A", "B", "C"], placeholder="Selecione", key='cadastrar_status_atual')
        with col2:
            profissional_responsavel = st.selectbox("Profissional responsável por essa etapa", ["Fulano", "Ciclano", "Beltrano"], placeholder="Selecione", key='cadastrar_responsavel_nome')
        with col3:
            lead_finalizado = st.radio("Matrícula realizada?", ["Não", "Sim"], horizontal=True)
        observacoes = st.text_area("Observações")

        st.markdown("---")

        st.markdown("""
            **Declaração de Consentimento (LGPD)**  
            Em observância à Lei nº 13.709/18 - LGPD (Lei Geral de Proteção de Dados), autorizo de forma informada, livre, expressa e consciente que a Escola Colibri realize o tratamento dos dados pessoais e sensíveis fornecidos, incluindo a inclusão destes na lista de alunos com interesse em vagas na instituição e, em caso de matrícula, no cadastro oficial de alunos.  
            - Estou ciente de que a Escola Colibri não compartilhará os dados com parceiros ou prestadores de serviços, restringindo-se às suas próprias funções e atividades.  
            - Estou ciente de que a Escola Colibri poderá tomar decisões automatizadas ou não com base nos dados fornecidos.
            """)

        consentimento_lgpd = st.checkbox("Declaro que li e concordo com o termo de consentimento acima.")

        # Criar o dicionário com os dados
        dict_leads = {
            "nome_responsavel_1": nome_responsavel_1,
            "grau_parentesco_1": grau_parentesco_1,
            "telefone_1": telefone_formatado_1,
            "email_1": email_1,
            "profissao_1": profissao_1,

            "nome_responsavel_2": nome_responsavel_2,
            "grau_parentesco_2": grau_parentesco_2,
            "telefone_2": telefone_formatado_2,
            "email_2": email_2,
            "profissao_2": profissao_2,

            "nome_aluno_1": nome_aluno_1,
            "idade_aluno_1": idade_aluno_1,
            "data_nascimento_aluno_1": str(data_nascimento_aluno_1),
            "escola_atual_1": escola_atual_1,
            "serie_interesse_1": serie_interesse_1,
            "especialista_acompanhante_1": especialista_acompanhante_1,
            "diagnostico_1": diagnostico_1,

            "nome_aluno_2": nome_aluno_2,
            "idade_aluno_2": idade_aluno_2,
            "data_nascimento_aluno_2": str(data_nascimento_aluno_2),
            "escola_atual_2": escola_atual_2,
            "serie_interesse_2": serie_interesse_2,
            "especialista_acompanhante_2": especialista_acompanhante_2,
            "diagnostico_2": diagnostico_2,

            "nome_aluno_3": nome_aluno_3,
            "idade_aluno_3": idade_aluno_3,
            "data_nascimento_aluno_3": str(data_nascimento_aluno_3),
            "escola_atual_3": escola_atual_3,
            "serie_interesse_3": serie_interesse_3,
            "especialista_acompanhante_3": especialista_acompanhante_3,
            "diagnostico_3": diagnostico_3,

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
                try:
                    cadastrar_registro("leads", dict_leads)
                    st.success("Lead cadastrado com sucesso.")
                except Exception as e:
                    st.error(f"Erro ao cadastrar Lead: {e}")
            else:
                st.error("É necessário o consentimento LGPD para prosseguir.")

#with tabs_leads[1]:
    #leads_result = buscar_registro("leads", "nome_aluno")
    #df_leads = pd.DataFrame(leads_result)
    #df_leads = df_leads.drop(columns=["id"])
    #st.dataframe(df_leads, height=500)


