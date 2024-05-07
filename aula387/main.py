import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# CRUD - Create Read   Update Delete
# SQL -  INSERT SELECT UPDATE DELETE

# CUIDADO: Fazendo delete sem where
cursor.execute(
  f'DELETE FROM {TABLE_NAME}'
)

# DELETE mais cuidadoso (com where)
cursor.execute(
  f'DELETE FROM sqlite_sequence WHERE name = "{TABLE_NAME}"'
)
connection.commit()

# Cria a tabela
cursor.execute(
  f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
  '('
  'id INTEGER PRIMARY KEY AUTOINCREMENT,'
  'name TEXT,'
  'weight REAL'
  ')'
)
connection.commit()

# Registrar valores nas colunas da tabela
cursor.executemany(
  f'INSERT INTO {TABLE_NAME} (name, weight) VALUES (?, ?)',
  [('João', 70), ('Maria', 50), ('José', 80)]
)
connection.commit()

cursor.close()
connection.close()