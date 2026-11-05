import os
import traceback

# Librerías
import oracledb
from dotenv import load_dotenv

load_dotenv()

# CONSTANTES
DB_DSN = os.getenv('DB_DSN')
DB_PASS = os.getenv('DB_PASS')
DB_USER = os.getenv('DB_USER')

def conectar_db():
    """ Conexión a BD oracle """
    try:
        conn = oracledb.connect(
            user=DB_USER,
            password=DB_PASS,
            dsn=DB_DSN
        )

        return conn
    except Exception as e:
        print(f"[ERROR] No se pudo conectar a BD:")
        traceback.print_exc()
        return None
