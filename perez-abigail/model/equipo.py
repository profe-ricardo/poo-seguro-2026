from config.app_config import conectar_db, oracledb

def validar_tabla_equipo():
    consulta_sql = """
        create table if not exists equipos (
            id NUMBER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1) PRIMARY KEY,
            tipo varchar2(50),
            marca varchar2(50),
            modelo varchar2(100),
            serie varchar2(100),
            constraint uq_equipo unique (tipo, marca, modelo, serie)
        );
    """
    conn = None
    cursor = None

    try:
        print("Intentando validar tabla...")
        conn = conectar_db()

        if conn:
            cursor = conn.cursor()
            cursor.execute(consulta_sql)
            print("[INFO] Tabla equipos validada correctamente")
    except Exception as e:
        print(f"[ERROR] Creación de tabla  equipos | {e}")
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
            cursor.execute(consulta_insert, (equipo.tipo, equipo.marca, equipo.modelo, equipo.serie)) # Se entrega los datos parametrizados
            conn.commit()

            print("[INFO] Equipo registrado correctamente")
    except oracledb.IntegrityError as e:
        if conn:
            conn.rollback() # Si algo falla, nos aseguramos de que nada cambie en la bd

        error = e.args[0]

        if error.code == 1:
            print("[WARNING] Este equipo ya fue registrado") # El error ORA-00001 indica prohibición de datos duplicados (constraint uq_cliente)
        else:
            print(f"[ERROR] Error de integridad | {e}")
    except Exception as e:
        if conn:
            conn.rollback() # Si algo falla, nos aseguramos de que nada cambie en la bd

        print(f"[ERROR] Equipo no se logro registrar | {e}")
    finally:
        if cursor:
            cursor.close()

        if conn:
            conn.close()

class EquipoRepositorio():
    def __init__(self):
        pass

class Equipo(EquipoRepositorio):
    def __init__(self, tipo: str, marca: str, modelo: str, serie: str):
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.serie = serie

        validar_tabla_equipo()
        insertar_datos_equipo(self)

    def mostrar_datos(self):
        return f"Tipo: {self.tipo} | Marca: {self.marca} | Modelo: {self.modelo} | Serie: {self.serie}"