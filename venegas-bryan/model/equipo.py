from config.app_config import conectar_db, oracledb

class Equipo():
    def __init__(self, tipo: str, marca: str, modelo: str, serie: str):
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.serie = serie

    def mostrar_datos(self):
        return f"Equipo\n Tipo: {self.tipo} | Marca: {self.marca} | Modelo: {self.modelo} | Serie: {self.serie}"
    
def validar_tabla_equipo():
    consulta_sql = """
        create table if not exists equipos (
            id NUMBER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1) PRIMARY KEY,
            tipo varchar2(50) not null,
            marca varchar2(50) not null,
            modelo varchar2(80) not null,
            serie varchar2(100) not null,
            constraint uq_equipo_serie unique (serie)
        )
    """
    conn = None
    cursor = None

    try:
        conn = conectar_db()

        if conn:
            cursor = conn.cursor()
            cursor.execute(consulta_sql)
            print("[INFO] Tabla equipos creada correctamente")
    except Exception as e:
        print(f"[ERROR] Creación de tabla equipos | {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def insertar_datos_equipo(equipo: Equipo):
    consulta_insert = "insert into equipos (tipo, marca, modelo, serie) values (:1, :2, :3, :4)"
    conn = None
    cursor = None

    try:
        conn = conectar_db()

        if conn:
            cursor = conn.cursor()
            cursor.execute(
                consulta_insert,
                (equipo.tipo, equipo.marca, equipo.modelo, equipo.serie)
            )
            conn.commit()
            print("[INFO] Equipo insertado correctamente")
    except oracledb.IntegrityError as e:
        if conn:
            conn.rollback()

        error = e.args[0]

        if error.code == 1:
            print("[WARNING] El equipo ya está registrado")
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

