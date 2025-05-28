import streamlit as st
from db import supabase
from cabecalho import *

conexao_e_cabecalho()

st.title("📋 Gerenciamento de Leads")
st.info("Aqui você poderá cadastrar, visualizar, editar e excluir leads.")
