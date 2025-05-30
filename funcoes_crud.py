from db import supabase
import streamlit as st

def cadastrar_registro (nome_tabela: str, dados: dict):
    try:
        response = supabase.table(nome_tabela).insert(dados).execute()
        return response
    except Exception as e:
        st.error(f"Erro no cadastro: {e}")

def buscar_registro (nome_tabela: str, ordenar_por: str, colunas=None):
    colunas_str = ", ".join(colunas) if colunas else "*"
    return supabase.table(nome_tabela).select(colunas_str).order(ordenar_por).execute().data

