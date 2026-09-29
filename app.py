import streamlit as st

st.set_page_config(
    page_title="RPG Manager",
    page_icon="gema.png",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        "Get Help": "https://5e.tools",
        "Report a bug": "https://github.com/ArthurDaniel02/Projeto-WebAppIHC",
        "About": """
        ## RPG Manager v1.0
        Aplicação desenvolvida para a disciplina de **Interação Humano-Computador** (IFB).
        * **Equipe:** Arthur, Danilo, Matheus e Thiago.
        * **Stack:** Python, Streamlit, HTML/CSS/JS e PostgreSQL.
        """
    }
)

st.markdown(
    """
    <style>
        header[data-testid="stHeader"] {
            background: transparent !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

if "autenticado" not in st.session_state:
    st.session_state.autenticado = False
    
pagina_login = st.Page(
    "views/login.py",
    title="Entrar no Sistema",
    default=True
)
pagina_mestre = st.Page(
    "views/mestre.py", 
    title="Painel do Mestre", 
)

pagina_jogador = st.Page(
    "views/jogador.py", 
    title="Ficha do Jogador", 
)

pagina_handouts = st.Page(
    "views/handouts.py", 
    title="Biblioteca de Handouts", 
   
)

if not st.session_state.autenticado:
    navegacao = st.navigation([pagina_login], position="hidden")
else:
    navegacao = st.navigation(
        {
            "Mesa & Gestão": [pagina_mestre, pagina_handouts],
            "Personagem": [pagina_jogador]
        }
    )
    
    if st.sidebar.button("🚪 Sair da Conta", use_container_width=True):
        st.session_state.autenticado = False
        st.rerun()
    st.sidebar.caption("Versão (v1.0)")

navegacao.run()