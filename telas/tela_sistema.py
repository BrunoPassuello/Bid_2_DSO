import streamlit as st


class TelaSistema:
    def tela_opcoes(self):
        if st.session_state.tela_atual != 'sistema':
            return None

        # Limpa a tela principal
        st.empty()

        # Título centralizado
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.title("Sistema de Gerenciamento - BID_2")

        # Menu lateral mais organizado
        with st.sidebar:
            st.title("Menu Principal")
            st.divider()

            menu_items = {
                "Clube": "clube",
                "Jogador": "jogador",
                "Técnico": "tecnico",
                "Campeonato": "campeonato",
                "Finalizar Sistema": None
            }

            for label, value in menu_items.items():
                if st.button(label, key=f"sistema_btn_{value if value else 'finalizar'}", use_container_width=True):
                    if value is None:
                        st.session_state.tela_atual = None
                        return 0
                    st.session_state.tela_atual = value
                    st.rerun()
        return None

    def mostra_mensagem(self, mensagem):
        st.warning(mensagem)
