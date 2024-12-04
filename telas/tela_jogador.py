import streamlit as st
from entidades.posicao import Posicao


class TelaJogador:
    def tela_inicial_jogador(self):
        st.title("Gerenciamento de Jogadores")

        with st.sidebar:
            st.title("Menu")
            if st.button("Cadastrar Jogador", key="jog_btn_cadastrar"):
                return 1
            if st.button("Alterar Jogador", key="jog_btn_alterar"):
                return 2
            if st.button("Listar Jogadores", key="jog_btn_listar"):
                return 3
            if st.button("Excluir Jogador", key="jog_btn_excluir"):
                return 4
            if st.button("Retornar", key="jog_btn_retornar"):
                return 0
        return None

    def tela_cadastro_jogador(self):
        st.header("Cadastro de Jogador")

        nome = st.text_input("Nome", key="jog_nome")
        cpf = st.text_input("CPF (somente números)",
                            key="jog_cpf", max_chars=11)
        idade = st.number_input("Idade", min_value=16,
                                max_value=50, step=1, key="jog_idade")
        peso = st.number_input("Peso (kg)", min_value=50,
                               max_value=150, step=1, key="jog_peso")
        altura = st.number_input(
            "Altura (m)", min_value=1.50, max_value=2.20, step=0.01, key="jog_altura")
        pais = st.text_input("País", key="jog_pais")
        posicao = st.selectbox("Posição",
                               ["Goleiro", "Zagueiro", "Lateral",
                                   "Volante", "Meio-Campo", "Atacante"],
                               key="jog_posicao")
        estrangeiro = st.checkbox("É estrangeiro?", key="jog_estrangeiro")

        if st.button("Confirmar Cadastro", key="jog_btn_confirmar"):
            if not all([nome, cpf, pais, posicao]):
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
                "posicao": posicao,
                "peso": peso,
                "altura": altura,
                "estrangeiro": "S" if estrangeiro else "N"
            }
        return None

    def seleciona_jogador(self):
        st.subheader("Selecionar Jogador")
        cpf = st.text_input("CPF do Jogador:",
                            key="jog_select_cpf", max_chars=11)
        if st.button("Buscar", key="jog_btn_buscar"):
            if not cpf.isdigit() or len(cpf) != 11:
                st.error("CPF deve conter 11 dígitos numéricos!")
                return None
            return cpf
        return None

    def mostra_jogador(self, jogador):
        st.header("Jogadores Cadastrados")

        with st.expander(f"Jogador: {jogador.nome}"):
            st.write(f"**CPF:** {jogador.cpf}")
            st.write(f"**Idade:** {jogador.idade} anos")
            st.write(f"**País:** {jogador.pais}")
            st.write(f"**Posição:** {jogador.posicao.nome}")
            st.write(f"**Peso:** {jogador.peso} kg")
            st.write(f"**Altura:** {jogador.altura:.2f} m")
            st.write(
                f"**Estrangeiro:** {'Sim' if jogador.estrangeiro else 'Não'}")
            st.divider()

    def mostra_mensagem(self, mensagem):
        st.warning(mensagem)
