import streamlit as st
import database as db

db.initialize_database()


col_esq, col_centro, col_dir = st.columns([1, 1.8, 1])

with col_centro:
    st.markdown("<br>", unsafe_allow_html=True)
    st.title("🎲 RPG Manager")
    st.caption("Acesso ao Gerenciador RPG")
    st.markdown("---")
    aba_entrar, aba_cadastrar = st.tabs(["Acessar Conta", "Novo Cadastro"])
    with aba_entrar:
        with st.form("form_login"):
            usuario = st.text_input(
                "Login", 
                placeholder="Insira seu Usuário ou E-mail"
            )
            senha = st.text_input(
                "Senha", 
                type="password", 
                placeholder="Insira sua senha"
            )
            
            perfil = st.radio(
                "Entrar como:",
                options=["Mestre", "Jogador"],
                horizontal=True
            )

            botao_entrar = st.form_submit_button("Acessar Gerenciador", use_container_width=True)

            if botao_entrar:
                if not usuario or not senha:
                    st.error("Preencha todos os campos para continuar.")
                else: 
                    usuario_autenticado = db.auth_user(usuario, senha)
                    if usuario_autenticado:
                        st.session_state.autenticado = True
                        st.session_state.usuario_ativo = usuario_autenticado["usuario"]
                        st.session_state.perfil_ativo = perfil
                        st.success(f"Conectado como {usuario_autenticado['usuario']}!")
                        st.rerun()
                    else:
                        print("Credenciais inválidas. Tente Novamente.")
                
                    
    with aba_cadastrar:
        with st.form("form_cadastro"):
            novo_usuario = st.text_input("Nome de Usuário", placeholder="Insira Usuário")
            novo_email = st.text_input("E-mail", placeholder="Insira E-mail")
            nova_senha = st.text_input("Crie uma Senha", type="password")
            perfil_padrao = st.radio("Perfil Principal:", options=["Mestre", "Jogador"], horizontal=True)
            
            btn_cadastrar = st.form_submit_button("Criar Conta", use_container_width=True)

            if btn_cadastrar:
                if not novo_usuario or not novo_email or not nova_senha:
                    st.warning("Preencha todos os campos para efetuar o cadastro.")
                else:
                    sucesso = db.insert_user(novo_usuario, novo_email, nova_senha, perfil_padrao)
                    if sucesso:
                        st.success("Conta criada com sucesso! Acesse pela aba 'Acessar Conta'.")
                    else:
                        st.error("Nome de usuário ou e-mail já estão em uso.")
    st.markdown("---")
    st.caption("Projeto IHC • Instituto Federal de Brasília")