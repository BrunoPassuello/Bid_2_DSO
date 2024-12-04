import streamlit as st
from telas.tela_tecnico import TelaTecnico

def main():
    st.set_page_config(page_title="Sistema de Técnicos")
    tela_tecnico = TelaTecnico()
    tela_tecnico.tela_inicial_tecnico()

if __name__ == "__main__":
    main()


