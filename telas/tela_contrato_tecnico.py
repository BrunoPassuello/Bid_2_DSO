import streamlit as st


class TelaContratoTecnico:
    def tela_inicial_contrato_tecnico(self):
        if st.session_state.tela_atual != 'contrato_tecnico':
            return None

        # Limpa a tela principal
        st.empty()

        # Título centralizado
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.title("Gerenciamento de Contrato do Técnico")

        # Menu lateral
        with st.sidebar:
            st.title("Menu")
            st.divider()

            menu_items = {
                "Contratar Técnico": "contratar",
                "Demitir Técnico": "demitir",
                "Informações do Contrato": "informacoes",
                "Retornar": "retornar"
            }

            for label, value in menu_items.items():
                if st.button(label, key=f"contrato_tecnico_btn_{value}", use_container_width=True):
                    if value == "retornar":
                        st.session_state.tela_atual = 'clube'
                        st.session_state.sub_tela = 'clube_selecionado'
                        st.rerun()
                        return 0
                    st.session_state.sub_tela = value
                    return menu_items[label]
        return None

    def pega_dados_contrato(self):
        if st.session_state.sub_tela != 'contratar':
            return None

        st.subheader("Contratar Técnico")

        with st.form(key="contrato_tecnico"):
            cpf = st.text_input("CPF do Técnico:", key="contrato_t_cpf", max_chars=11)
            salario = st.number_input("Salário:", key="contrato_t_salario", 
                                    min_value=0.0, format="%f")
            multa = st.number_input("Multa Rescisória:", key="contrato_t_multa", 
                                  min_value=0.0, format="%f")
            
            submitted = st.form_submit_button("Contratar", use_container_width=True)

            if submitted:
                if not cpf.isdigit() or len(cpf) != 11:
                    st.error("CPF deve conter 11 dígitos numéricos!")
                    return None
                if salario <= 0:
                    st.error("Salário deve ser maior que zero!")
                    return None
                if multa <= 0:
                    st.error("Multa rescisória deve ser maior que zero!")
                    return None
                
                return {
                    "cpf": int(cpf),
                    "salario": salario,
                    "multa_rescisoria": multa
                }
        return None

    def mostra_contrato(self, contrato):
        if st.session_state.sub_tela != 'informacoes':
            return None

        st.subheader(f"Contrato do Técnico {contrato.tecnico.nome}")
        
        col1, col2 = st.columns(2)
        with col1:
            st.write("**CPF:**", contrato.tecnico.cpf)
            st.write("**Salário:** R$", f"{contrato.salario:,.2f}")
            st.write("**País:**", contrato.tecnico.pais)
        with col2:
            st.write("**Multa Rescisória:** R$", f"{contrato.multa_rescisoria:,.2f}")
            st.write("**Licença:**", contrato.tecnico.licenca.tipo)
            st.write("**Idade:**", contrato.tecnico.idade)
        st.divider()

    def confirma_demissao(self):
        st.warning("Tem certeza que deseja demitir o técnico?")
        return st.button("Confirmar Demissão", key="btn_confirma_demissao", 
                        use_container_width=True)

    def mostra_mensagem(self, mensagem):
        st.warning(mensagem)
