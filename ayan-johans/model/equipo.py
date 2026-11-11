#Generar conexión con DB para guardar equipos
from config.app_config import conectar_db, oracledb
class Equipo:
    def __init__(self, tipo: str, marca: str, modelo: str, serie: str):
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.serie = serie

        validar_tabla_equipo()
        insertar_datos_equipo(self.tipo, self.marca, self.modelo, self.serie)

    def mostrar_datos(self):
        return f'Equipo: {self.tipo} | Marca: {self.marca} | Modelo: {self.modelo}'

def validar_tabla_equipo():
    consulta_sql = """
        create table if not exists equipos(
            id number generated always as identity (start with 1 increment by 1) primary key,
            tipo varchar2(100),
            marca varchar2(100),
            modelo varchar2(100),
            serie varchar2(100),
            constraint uq_equipo unique (serie)
        )
    """

    conn = None
    cursor = None

    try:
        conn = conectar_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute(consulta_sql)
            print("[INFO] Tabla 'equipos' creada correctamente")
    except Exception as e:
        print(f"[ERROR] Creación de tabla 'equipos' | {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
def insertar_datos_equipo(tipo: str, marca: str , modelo: str, serie: str):
    consulta_insert = """
        insert into equipos (tipo, marca, modelo, serie) values (:1, :2, :3, :4)
    """
    conn = None
    cursor = None

    try:
        conn = conectar_db()

        if conn:
            cursor = conn.cursor()
            cursor.execute(consulta_insert, (tipo, marca, modelo, serie))
            conn.commit()

            print("[INFO] Equipo insertado correctamente")
    except oracledb.IntegrityError as e:
        if conn:
            conn.rollback()
        error = e.args[0]
        if error.code == 1:
            print("[ADVERTENCIA] El equipo ya está registrado")
        else:
            print(f"[ERROR] Error de integridad | {e}")

    except Exception as e:
        if conn:
            conn.rollback()
        print(f"[ERROR] Equipo no registrado | {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()