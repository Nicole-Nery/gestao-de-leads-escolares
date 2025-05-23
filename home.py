import streamlit as st
from db import supabase

def show_home():
    # Estilo CSS
    caminho_css = "style/main.css"
    with open(caminho_css) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    st.write("Oie")
