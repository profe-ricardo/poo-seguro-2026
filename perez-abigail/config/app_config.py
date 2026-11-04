# Python
import os

# Librerias Externas
import oracledb
from dotenv import load_dotenv

load_dotenv()

DB_DSN = os.getenv('DB_DSN')
DB_PASS = os.getenv('DB_PASS')
DB_USER = os.getenv('DB_USER')

def conectar_db():
    try:
        conn = oracledb.connect(
            user = DB_USER,
            dsn = DB_DSN,
            password = DB_PASS
        )
    except Exception as e:
        print(f"[ERROR] No se pudo conectar a BD | {e}")
        return None