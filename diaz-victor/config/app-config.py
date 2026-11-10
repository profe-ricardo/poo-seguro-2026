import os
import traceback

import oracledb #importa oracle?
from dotenv import load_dotenv

load_dotenv()

DB_DSN = os.getenv('DB_DSN') #credenciales de la base de datos
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

        return conn #abreviatura de
    except Exception as e:
        print(f"No se pudo conectar a la base de datos:")
        traceback.print_exc()
        return None