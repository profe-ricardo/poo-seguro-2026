from config.app_config import conectar_db, oracledb

def validar_tabla_equipo():
    consulta_sql = """
        create table if not exists equipos (
            id NUMBER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1) PRIMARY KEY,
            tipo varchar2(100),
            marca varchar2(100),
            modelo varchar2(100),
            serie varchar2(100),
            constraint uq_equipo unique (serie)
        );
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

def insertar_datos_equipo(tipo: str, marca: str, modelo: str, serie: str):
    consulta_insert = "insert into equipos (tipo, marca, modelo, serie) values (:1, :2, :3, :4)"
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
            print("[WARNING] El equipo ya está registrado (número de serie duplicado)")
        else:
            print(f"[ERROR] Error de integridad en equipo | {e}")
    except Exception as e:
        if conn:
            conn.rollback()
        print(f"[ERROR] Equipo no registrado | {e}")