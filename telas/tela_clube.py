import streamlit as st


class TelaClube:
    def tela_inicial_clube(self):
        if st.session_state.tela_atual != 'clube':
            return None

        # Limpa a tela principal
        st.empty()

        # Título centralizado
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.title("Gerenciamento de Clubes")

        # Menu lateral organizado
        with st.sidebar:
            st.title("Menu")
            st.divider()

            menu_items = {
                "Selecionar Clube": "selecionar",
                "Cadastrar Clube": "cadastrar",
                "Listar Clubes": "listar",
                "Excluir Clube": "excluir",
                "Retornar": "retornar"
            }

            for label, value in menu_items.items():
                if st.button(label, key=f"clube_btn_{value}", use_container_width=True):
                    if value == "retornar":
                        st.session_state.tela_atual = 'sistema'
                        st.session_state.sub_tela = None
                        st.rerun()
                        return 0
                    st.session_state.sub_tela = value
                    return menu_items[label]
        return None

    def tela_clube_selecionado(self):
        if st.session_state.sub_tela != 'clube_selecionado':
            return None

        # Limpa a tela principal
        st.empty()

        # Menu lateral
        with st.sidebar:
            # Título do menu
            st.title("Menu")
            st.divider()

            # Menu de operações
            menu_items = {
                "Jogadores": 1,
                "Técnico": 2,
                "Campeonatos": 3,
                "Informações": 4,
                "Menu Principal": 0
            }

            for label, value in menu_items.items():
                if st.button(label, key=f"clube_sel_btn_{value}", use_container_width=True):
                    if value == 0:
                        st.session_state.sub_tela = None
                        st.session_state.tela_atual = 'sistema'
                        st.rerun()
                    return value
        return None

    def tela_cadastra_clube(self):
        if st.session_state.sub_tela not in ['cadastrar', 'alterar']:
            return None

        st.header("Cadastro de Clube")

        with st.form(key="cadastro_clube"):
            col1, col2 = st.columns(2)
            with col1:
                nome = st.text_input("Nome do Clube", key="clube_nome")
            with col2:
                pais = st.text_input("País", key="clube_pais")

            submitted = st.form_submit_button(
                "Cadastrar Clube", use_container_width=True)

            if submitted:
                if not nome or not pais:
                    st.error("Todos os campos são obrigatórios!")
                    return None
                return {"nome": nome, "pais": pais}
        return None

    def seleciona_clube(self):
        if st.session_state.sub_tela not in ['selecionar', 'alterar', 'excluir']:
            return None

        st.subheader("Selecionar Clube")

        with st.form(key="seleciona_clube"):
            nome = st.text_input("Nome do Clube:", key="clube_select_nome")
            submitted = st.form_submit_button(
                "Buscar", use_container_width=True)

            if submitted:
                if not nome:
                    st.error("Nome do clube é obrigatório!")
                    return None
                return nome
        return None

    def mostra_clube(self, clube):
        with st.expander(f"Clube: {clube.nome}", expanded=True):
            col1, col2 = st.columns(2)
            with col1:
                st.write("**País:**", clube.pais)
            with col2:
                if clube.contrato_tecnico:
                    st.write("**Técnico:**", clube.contrato_tecnico.tecnico.nome)
                else:
                    st.write("**Técnico:** Não contratado")
            
            # Mostrar jogadores do clube
            if clube.jogadores:
                st.write("**Jogadores:**")
                for jogador in clube.jogadores:
                    st.write(f"- {jogador.jogador.nome}")
            else:
                st.write("**Jogadores:** Nenhum jogador contratado")
            
            # Mostrar campeonatos do clube
            if clube.campeonatos:
                st.write("**Campeonatos:**")
                for campeonato in clube.campeonatos:
                    st.write(f"- {campeonato.nome}")
            else:
                st.write("**Campeonatos:** Não participa de nenhum campeonato")
            
            st.divider()

    def relatorio_clube(self, clube, lista_contrato_jogadores, lista_campeonatos):
        st.header(f"Relatório do Clube {clube.nome}")

        # Informações Gerais
        with st.expander("Informações Gerais", expanded=True):
            col1, col2 = st.columns(2)
            with col1:
                st.write("**Nome:**", clube.nome)
            with col2:
                st.write("**País:**", clube.pais)

        # Técnico
        with st.expander("Técnico", expanded=True):
            if clube.contrato_tecnico:
                st.write("**Nome:**", clube.contrato_tecnico.tecnico.nome)
                st.write("**Licença:**",
                         clube.contrato_tecnico.tecnico.licenca.tipo)
            else:
                st.warning("O clube não possui técnico!")

        # Jogadores
        with st.expander("Jogadores", expanded=True):
            if lista_contrato_jogadores:
                for contrato in lista_contrato_jogadores:
                    st.write(f"**{contrato.jogador.nome}**")
                    st.write(f"- Salário: R$ {contrato.salario:,.2f}")
                    st.write(f"- Multa: R$ {contrato.multa_rescisoria:,.2f}")
                    st.divider()
            else:
                st.warning("O clube não possui jogadores!")

        # Campeonatos
        with st.expander("Campeonatos", expanded=True):
            if lista_campeonatos:
                for campeonato in lista_campeonatos:
                    st.write(f"**{campeonato.nome}**")
                    st.write(f"- Premiação: R$ {campeonato.premiacao:,.2f}")
                    st.divider()
            else:
                st.warning(
                    "O clube não está participando de nenhum campeonato!")

    def mostra_mensagem(self, mensagem):
        st.warning(mensagem)

    def tela_clube_informacoes(self):
        if st.session_state.sub_tela != 'informacoes':
            return None

        clube = st.session_state.clube_selecionado
        
        st.title("Informações do Clube")
        
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Nome:**", clube.nome)
            st.write("**País:**", clube.pais)
        
        with col2:
            if clube.contrato_tecnico:
                st.write("**Técnico:**", clube.contrato_tecnico.tecnico.nome)
            else:
                st.write("**Técnico:** Não contratado")
        
        # Relatórios section
        st.subheader("Relatórios de Salários e Multas")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Jogador com Maior Salário", key="btn_maior_salario", use_container_width=True):
                st.session_state.relatorio_tipo = "maior_salario"
                st.rerun()
                
            if st.button("Jogador com Maior Multa", key="btn_maior_multa", use_container_width=True):
                st.session_state.relatorio_tipo = "maior_multa"
                st.rerun()
                
        with col2:
            if st.button("Jogador com Menor Salário", key="btn_menor_salario", use_container_width=True):
                st.session_state.relatorio_tipo = "menor_salario"
                st.rerun()
                
            if st.button("Jogador com Menor Multa", key="btn_menor_multa", use_container_width=True):
                st.session_state.relatorio_tipo = "menor_multa"
                st.rerun()
        
        # Display report result if any
        if hasattr(st.session_state, 'relatorio_tipo'):
            st.divider()
            st.subheader("Resultado do Relatório")
            # The actual result will be shown by the controller
        
        st.divider()
        
        # Mostrar jogadores do clube
        st.subheader("Jogadores")
        if clube.jogadores:
            for jogador in clube.jogadores:
                st.write(f"- {jogador.jogador.nome}")
        else:
            st.write("Nenhum jogador contratado")
        
        # Mostrar campeonatos do clube
        st.subheader("Campeonatos")
        if clube.campeonatos:
            for campeonato in clube.campeonatos:
                st.write(f"- {campeonato.nome}")
        else:
            st.write("Não participa de nenhum campeonato")

        if st.button("Retornar", key="btn_retornar_info", use_container_width=True):
            st.session_state.sub_tela = 'clube_selecionado'
            if hasattr(st.session_state, 'relatorio_tipo'):
                del st.session_state.relatorio_tipo
            st.rerun()
