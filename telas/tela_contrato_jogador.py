import streamlit as st
from entidades.contrato_jogador import ContratoJogador


class TelaContratoJogador:
    def tela_inicial_contrato_jogador(self):
        if st.session_state.tela_atual != 'contrato_jogador':
            return None

        # Limpa a tela principal
        st.empty()

        # Título centralizado
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.title("Gerenciamento de Contratos de Jogadores")

        # Menu lateral organizado
        with st.sidebar:
            st.title("Menu")
            st.divider()

            menu_items = {
                "Contratar Jogador": "contratar",
                "Alterar Contrato": "alterar",
                "Demitir Jogador": "demitir",
                "Listar Contratos": "listar",
                "Retornar": "retornar"
            }

            for label, value in menu_items.items():
                if st.button(label, key=f"contrato_j_btn_{value}", use_container_width=True):
                    if value == "retornar":
                        st.session_state.tela_atual = 'clube'
                        st.session_state.sub_tela = None
                        st.rerun()
                        return 0
                    st.session_state.sub_tela = value
                    return menu_items[label]
        return None

    def pega_dados_contrato(self):
        if st.session_state.sub_tela != 'contratar':
            return None

        st.header("Dados do Contrato")

        with st.form(key="contrato_jogador"):
            col1, col2 = st.columns(2)
            with col1:
                cpf = st.text_input(
                    "CPF do jogador (somente números)", key="contrato_j_cpf", max_chars=11)
                salario = st.number_input("Salário do jogador (R$)",
                                          min_value=0.0,
                                          step=1000.0,
                                          format="%.2f",
                                          key="contrato_j_salario")
            with col2:
                multa_rescisoria = st.number_input("Multa Rescisória (R$)",
                                                   min_value=0.0,
                                                   step=10000.0,
                                                   format="%.2f",
                                                   key="contrato_j_multa")
                contrato_produtividade = st.checkbox("Contrato com Produtividade",
                                                     key="contrato_j_produtividade")

            submitted = st.form_submit_button(
                "Confirmar Contrato", use_container_width=True)

            if submitted:
                if not cpf or not cpf.isdigit() or len(cpf) != 11:
                    st.error("CPF deve conter 11 dígitos numéricos!")
                    return None
                if salario <= 0:
                    st.error("Salário deve ser maior que zero!")
                    return None
                if multa_rescisoria < 0:
                    st.error("Multa rescisória não pode ser negativa!")
                    return None

                return {
                    "cpf": cpf,
                    "salario": salario,
                    "multa_rescisoria": multa_rescisoria,
                    "contrato_produtividade": contrato_produtividade
                }
        return None

    def mostra_contrato(self, contrato):
        if st.session_state.sub_tela != 'listar':
            return None

        with st.expander(f"Contrato de {contrato.jogador.nome}", expanded=True):
            col1, col2 = st.columns(2)
            with col1:
                st.write("**CPF:**", contrato.jogador.cpf)
                st.write("**Salário:** R$", f"{contrato.salario:,.2f}")
                st.write("**País:**", contrato.jogador.pais)
            with col2:
                st.write("**Multa Rescisória:** R$",
                         f"{contrato.multa_rescisoria:,.2f}")
                st.write("**Contrato com Produtividade:**",
                         'Sim' if contrato.contrato_produtividade else 'Não')
                st.write("**Posição:**", str(contrato.jogador.posicao.nome))
            st.divider()

    def seleciona_contrato(self):
        if st.session_state.sub_tela not in ['alterar', 'demitir']:
            return None

        st.subheader("Selecionar Contrato")

        with st.form(key="seleciona_contrato_jogador"):
            cpf = st.text_input("CPF do Jogador:",
                                key="contrato_j_select_cpf", max_chars=11)
            submitted = st.form_submit_button(
                "Buscar", use_container_width=True)

            if submitted:
                if not cpf.isdigit() or len(cpf) != 11:
                    st.error("CPF deve conter 11 dígitos numéricos!")
                    return None
                return cpf
        return None

    def confirma_demissao(self, contrato):
        if st.session_state.sub_tela != 'demitir':
            return None

        st.subheader("Confirmar Demissão")

        st.write(f"Deseja realmente demitir o jogador {contrato.jogador.nome}?")
        st.write("**Dados do contrato:**")
        st.write(f"- Salário: R$ {contrato.salario:,.2f}")
        st.write(f"- Multa Rescisória: R$ {contrato.multa_rescisoria:,.2f}")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Confirmar Demissão", key="contrato_j_btn_confirmar_demissao"):
                return True
        with col2:
            if st.button("Cancelar", key="contrato_j_btn_cancelar_demissao"):
                st.session_state.sub_tela = None
                st.rerun()
        return None

    def mostra_mensagem(self, mensagem):
        st.warning(mensagem)
