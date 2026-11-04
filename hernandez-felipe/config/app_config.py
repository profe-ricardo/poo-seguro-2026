#python
import os

#librerias
import oracledb
from dotenv import load_dotenv

load_dotenv()

#Constantes
DB_DNS = os.getenv('DB_DNS')
DB_PASS = os.getenv('DB_PASS')
DB_USER = os.getenv('DB_USER')

def conectar_db():
    """Conexion a DB Oracle"""
    try:
        conn = oracledb.connect(
            user=DB_USER,
            password=DB_PASS,
            dsn=DB_DNS
        )
        return conn
    except oracledb.Error as e:
        print(f"[ERROR] NO se pudo conectar a la base de datos: {e}")
        return None