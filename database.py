import sqlite3
import hashlib

DB_NAME ='rpg_banco.db'

def create_connection():
    conn = sqlite3.connect(DB_NAME, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def initialize_database():
    with create_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS usuarios(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                senha_hash TEXT NOT NULL,
                perfil_padrao TEXT NOT NULL CHECK(perfil_padrao IN ('Jogador', 'Mestre')),
                criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        conn.commit()
    

def hash_password(senha: str) -> str:
    return hashlib.sha256(senha.encode("utf-8")).hexdigest()


def insert_user(usuario: str, email: str, senha: str, perfil: str) -> bool:
    try:
        with create_connection() as conn:
            conn.execute("""
                INSERT INTO usuarios(usuario,email,senha_hash,perfil_padrao)
                VALUES (?,?,?,?)
                """,
                (usuario.strip(),email.strip().lower(),hash_password(senha),perfil)
            )
            conn.commit()
            return True
    except sqlite3.IntegrityError:
        return False

def auth_user(id: str, senha: str) -> dict | None:
    id_limpo = id.strip().lower()
    hash = hash_password(senha)

    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT id, usuario, email, perfil_padrao
            FROM usuarios
            WHERE(LOWER(usuario) = ? or LOWER(email) = ?) AND senha_hash = ?
            """,
            (id_limpo,id_limpo,hash)
        )
        linha = cursor.fetchone()
        if linha:
            return dict(linha)
        return None


