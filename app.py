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

navegacao = st.navigation(
    {
        "Mesa & Gestão": [pagina_mestre, pagina_handouts],
        "Personagem": [pagina_jogador]
    }
)


# st.sidebar.image("nivel.png", use_container_width=True)
# st.sidebar.markdown("---")

# with st.sidebar.expander("⚔️ Módulo de Combate", expanded=False):
#     if st.sidebar.button("Iniciar Turno", use_container_width=True):
#         st.toast("Turno de combate iniciado.")
#     if st.sidebar.button("Rolar Iniciativa", use_container_width=True):
#         st.toast("Iniciativas roladas com sucesso.")

# with st.sidebar.expander("📜 Documentos & Lore"):
#     st.sidebar.button("Ver Mapas", use_container_width=True)
#     st.sidebar.button("Anotações de NPCs", use_container_width=True)

# with st.sidebar.expander("⚙️ Sessão"):
#     st.sidebar.checkbox("Modo Noturno Reforçado")

#st.sidebar.markdown("---")
st.sidebar.caption("Versão (v1.0)")

navegacao.run()