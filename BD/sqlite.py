import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent

DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'clientes'

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# CRIA A TABELA
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'nome TEXT,'
    'peso REAL'
    ')'
)

conn.commit()


"""
# INSERE DADOS
# PERIGO DE SQL INJECTION

cursor.execute(
    f'INSERT INTO {TABLE_NAME}'
    '(id, nome,peso)'
    'VALUES'
    '(NULL,"Luiz Otávio", 9.9)'
)
"""

# ULTILIZANDO BINDS DIFICULTA O SQL INJECTION
sql = (
    f'INSERT INTO {TABLE_NAME} (nome, peso)'
    'VALUES (? , ?)'
)
# INSERINDO 1 VALOR
cursor.execute(sql, ['Joana', 2])

# INSERINDO 2+ VALORES
cursor.executemany(sql, [['Thiago', 99], ['Lucas', 80]])

conn.commit()

cursor.close()
conn.close()
