import streamlit as st
from controladores.controlador_sistema import ControladorSistema


def inicializa_states():
    if 'controlador' not in st.session_state:
        st.session_state.controlador = ControladorSistema()
    if 'tela_atual' not in st.session_state:
        st.session_state.tela_atual = 'sistema'
    if 'sub_tela' not in st.session_state:
        st.session_state.sub_tela = None
    if 'clube_selecionado' not in st.session_state:
        st.session_state.clube_selecionado = None


def configura_pagina():
    st.set_page_config(
        page_title="Sistema BID_2",
        page_icon="⚽",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Remove o menu padrão e o footer do Streamlit
    hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        .stDeployButton {display:none;}
        header {visibility: hidden;}
        </style>
        """
    st.markdown(hide_menu_style, unsafe_allow_html=True)


def main():
    configura_pagina()
    inicializa_states()

    # Adiciona um botão de retorno ao menu principal
    if st.session_state.tela_atual != 'sistema':
        if st.sidebar.button(" Menu Principal", use_container_width=True):
            st.session_state.tela_atual = 'sistema'
            st.session_state.sub_tela = None
            st.rerun()

    # Se houver um clube selecionado, mostra ele no topo
    if st.session_state.clube_selecionado:
        st.sidebar.success(f"Clube Selecionado: {
                           st.session_state.clube_selecionado.nome}")

    # Executa o controlador principal
    st.session_state.controlador.abre_tela()


if __name__ == "__main__":
    main()
