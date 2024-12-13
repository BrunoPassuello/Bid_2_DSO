import streamlit as st


class TelaSistema:
    def tela_opcoes(self):
        if st.session_state.tela_atual != 'sistema':
            return None

        st.title("Sistema de Gerenciamento - BID_2")

        with st.sidebar:
            st.empty()
            
            st.title("Menu Principal")
            st.divider()

            menu_items = {
                "Clube": "clube",
                "Jogador": "jogador",
                "Técnico": "tecnico",
                "Campeonato": "campeonato",
                "Finalizar Sistema": "finalizar"
            }

            for label, value in menu_items.items():
                if st.button(label, key=f"sistema_btn_{value}", use_container_width=True):
                    if value == "finalizar":
                        st.stop()
                    st.session_state.tela_atual = value
                    if hasattr(st.session_state, 'sub_tela'):
                        del st.session_state.sub_tela
                    st.rerun()
        return None

    def mostra_mensagem(self, mensagem):
        st.warning(mensagem)
