import streamlit as st

class TelaCampeonato:
    def tela_inicial_campeonato(self):
        if st.session_state.tela_atual != 'campeonato':
            return None

        st.empty()

        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.title("Gerenciamento de Campeonatos")

        with st.sidebar:
            st.title("Menu")
            st.divider()

            menu_items = {
                "Cadastrar Campeonato": "cadastrar",
                "Alterar Campeonato": "alterar",
                "Listar Campeonatos": "listar",
                "Excluir Campeonato": "excluir",
                "Retornar": "retornar"
            }

            for label, value in menu_items.items():
                if st.button(label, key=f"camp_btn_{value}", use_container_width=True):
                    if value == "retornar":
                        st.session_state.tela_atual = 'sistema'
                        st.session_state.sub_tela = None
                        st.rerun()
                        return 0
                    st.session_state.sub_tela = value
                    return menu_items[label]
        return None

    def tela_cadastro_campeonato(self, dados_iniciais=None):
        if st.session_state.sub_tela not in ['cadastrar', 'alterar']:
            return None

        st.header("Cadastro de Campeonato")

        with st.form(key="cadastro_campeonato"):
            nome = st.text_input("Nome do Campeonato", value=dados_iniciais["nome"] if dados_iniciais else "", key="camp_nome")
            premiacao = st.number_input(
                "Premiação (R$)", min_value=0.0, step=1000.0, value=dados_iniciais["premiacao"] if dados_iniciais else 0.0, key="camp_premiacao")

            col1, col2 = st.columns(2)
            with col1:
                numero_times = st.number_input(
                    "Número de Times", min_value=2, max_value=50, step=1, value=dados_iniciais["numero_times"] if dados_iniciais else 2, key="camp_num_times")
                numero_estrangeiros = st.number_input(
                    "Estrangeiros por Time", min_value=0, max_value=11, step=1, value=dados_iniciais["numero_estrangeiros"] if dados_iniciais else 0, key="camp_num_estrangeiros")
            with col2:
                numero_jogadores = st.number_input(
                    "Jogadores por Time", min_value=16, max_value=32, step=1, value=dados_iniciais["numero_jogadores"] if dados_iniciais else 16, key="camp_num_jogadores")

            submitted = st.form_submit_button(
                "Cadastrar" if st.session_state.sub_tela == 'cadastrar' else "Alterar", use_container_width=True)

            if submitted:
                if not nome:
                    st.error("Nome do campeonato é obrigatório!")
                    return None

                return {
                    "nome": nome,
                    "premiacao": premiacao,
                    "numero_times": numero_times,
                    "numero_estrangeiros": numero_estrangeiros,
                    "numero_jogadores": numero_jogadores
                }
        return None

    def seleciona_campeonato(self):
        if st.session_state.sub_tela not in ['alterar', 'excluir']:
            return None

        st.subheader("Selecionar Campeonato")

        with st.form(key="seleciona_campeonato"):
            nome = st.text_input("Nome do Campeonato:", key="camp_select_nome")
            submitted = st.form_submit_button(
                "Buscar", use_container_width=True)

            if submitted:
                if not nome:
                    st.error("Nome do campeonato é obrigatório!")
                    return None
                return nome
        return None

    def mostra_campeonato(self, lista_campeonatos):
        if st.session_state.sub_tela != 'listar':
            return None

        st.header("Campeonatos Cadastrados")

        if not lista_campeonatos:
            st.warning("Não há campeonatos cadastrados.")
            return

        for campeonato in lista_campeonatos:
            with st.expander(f"Campeonato: {campeonato.nome}", expanded=True):
                col1, col2 = st.columns(2)
                with col1:
                    st.write("**Premiação:**",
                             f"R$ {campeonato.premiacao:,.2f}")
                    st.write("**Número de Times:**",
                             campeonato.regra.numero_times)
                with col2:
                    st.write("**Estrangeiros por Time:**",
                             campeonato.regra.numero_estrangeiros)
                    st.write("**Jogadores por Time:**",
                             campeonato.regra.numero_jogadores)
                st.divider()

    def mostra_mensagem(self, mensagem):
        st.warning(mensagem)
