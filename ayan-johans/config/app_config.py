import oracledb
import traceback
import os
from dotenv import load_dotenv

load_dotenv()

# Constantes
DB_DSN =  os.getenv('DB_DSN')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')

def conectar_db():
    """CONEXION A DB ORACLE"""
    try:
        conn = oracledb.connect(
            user = DB_USER,
            password = DB_PASS,
            dsn = DB_DSN
        )
        return conn
    except Exception as e:
        print(f"Error al conectar a DB | {e}")
        traceback.print_exc()
        return None
