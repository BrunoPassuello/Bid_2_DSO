import streamlit as st
from entidades.licenca import Licenca


class TelaTecnico:
    def tela_inicial_tecnico(self):
        if st.session_state.tela_atual != 'tecnico':
            return None
            
        # Limpa a tela principal
        st.empty()
        
        # Título centralizado
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            st.title("Gerenciamento de Técnicos")
        
        # Menu lateral organizado
        with st.sidebar:
            st.title("Menu")
            st.divider()
            
            menu_items = {
                "Cadastrar Técnico": "cadastrar",
                "Listar Técnicos": "listar",
                "Excluir Técnico": "excluir",
                "Retornar": "retornar"
            }
            
            for label, value in menu_items.items():
                if st.button(label, key=f"tec_btn_{value}", use_container_width=True):
                    if value == "retornar":
                        st.session_state.tela_atual = 'sistema'
                        st.session_state.sub_tela = None
                        st.rerun()
                        return 0
                    st.session_state.sub_tela = value
                    return menu_items[label]
        return None

    def tela_cadastro_tecnico(self):
        if st.session_state.sub_tela != 'cadastrar':
            return None
            
        st.header("Cadastro de Técnico")
        
        with st.form(key="cadastro_tecnico"):
            col1, col2 = st.columns(2)
            with col1:
                nome = st.text_input("Nome", key="tec_nome")
                cpf = st.text_input("CPF (somente números)", key="tec_cpf", max_chars=11)
                idade = st.number_input("Idade", min_value=25, max_value=80, step=1, key="tec_idade")
            with col2:
                pais = st.text_input("País", key="tec_pais")
                licenca = st.selectbox("Licença", 
                                     ["Licença A", "Licença B", "Licença C", "Licença PRO"],
                                     key="tec_licenca")
            
            submitted = st.form_submit_button("Cadastrar Técnico", use_container_width=True)
            
            if submitted:
                if not all([nome, cpf, pais, licenca]):
                    st.error("Todos os campos são obrigatórios!")
                    return None
                
                if not cpf.isdigit() or len(cpf) != 11:
                    st.error("CPF deve conter 11 dígitos numéricos!")
                    return None

                return {
                    "nome": nome,
                    "cpf": cpf,
                    "idade": idade,
                    "pais": pais,
                    "licenca": licenca
                }
        return None

    def seleciona_tecnico(self):
        if st.session_state.sub_tela != 'excluir':
            return None
            
        st.subheader("Selecionar Técnico")
        
        with st.form(key="seleciona_tecnico"):
            cpf = st.text_input("CPF do Técnico:", key="tec_select_cpf", max_chars=11)
            submitted = st.form_submit_button("Buscar", use_container_width=True)
            
            if submitted:
                if not cpf.isdigit() or len(cpf) != 11:
                    st.error("CPF deve conter 11 dígitos numéricos!")
                    return None
                return cpf
        return None

    def mostra_tecnicos(self, tecnicos):
        if st.session_state.sub_tela != 'listar':
            return None
            
        st.header("Técnicos Cadastrados")
        
        if not tecnicos:
            st.warning("Não há técnicos cadastrados.")
            return

        for tecnico in tecnicos:
            with st.expander(f"Técnico: {tecnico.nome}", expanded=True):
                col1, col2 = st.columns(2)
                with col1:
                    st.write("**CPF:**", tecnico.cpf)
                    st.write("**Idade:**", f"{tecnico.idade} anos")
                with col2:
                    st.write("**País:**", tecnico.pais)
                    st.write("**Licença:**", tecnico.licenca.tipo)
                st.divider()

    def confirma_exclusao(self, tecnico):
        if st.session_state.sub_tela != 'excluir':
            return None
            
        st.subheader("Confirmar Exclusão")
        
        st.write(f"Deseja realmente excluir o técnico {tecnico.nome}?")
        st.write("**Dados do técnico:**")
        st.write(f"- CPF: {tecnico.cpf}")
        st.write(f"- Idade: {tecnico.idade} anos")
        st.write(f"- País: {tecnico.pais}")
        st.write(f"- Licença: {tecnico.licenca.tipo}")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Confirmar Exclusão", key="tec_btn_confirmar_exclusao"):
                return True
        with col2:
            if st.button("Cancelar", key="tec_btn_cancelar_exclusao"):
                st.session_state.sub_tela = None
                st.rerun()
        return False

    def mostra_mensagem(self, mensagem):
        st.warning(mensagem)
