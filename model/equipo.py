from config.app_config import conectar_db, oracledb

def validar_tabla_equipo():
    consulta_sql = """
        CREATE TABLE IF NOT EXISTS equipos (
            id NUMBER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1) PRIMARY KEY,
            tipo VARCHAR2(50) NOT NULL,
            marca VARCHAR2(50) NOT NULL,
            modelo VARCHAR2(80) NOT NULL,
            serie VARCHAR2(100) NOT NULL,
            CONSTRAINT uq_serie UNIQUE (serie)
        )
    """
    conn = cursor = None
    try:
        conn = conectar_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute(consulta_sql)
            print("[INFO] Tabla equipos OK")
    except Exception as e:
        print(f"[ERROR] Creación tabla equipos | {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


class Equipo:
    def __init__(self, tipo: str, marca: str, modelo: str, serie: str, id: int = None):
        self.id = id
        self.tipo = tipo.strip()
        self.marca = marca.strip()
        self.modelo = modelo.strip()
        self.serie = serie.strip().upper()

        if self.id is None:
            validar_tabla_equipo()
            self._insertar()

    def _insertar(self):
        sql = """
            INSERT INTO equipos (tipo, marca, modelo, serie) 
            VALUES (:1, :2, :3, :4) 
            RETURNING id INTO :5
        """
        conn = cursor = None
        try:
            conn = conectar_db()
            if conn:
                cursor = conn.cursor()
                id_var = cursor.var(oracledb.NUMBER)
                cursor.execute(sql, (self.tipo, self.marca, self.modelo, self.serie, id_var))
                conn.commit()
                self.id = int(id_var.getvalue()[0])
                print(f"[INFO] Equipo insertado (ID: {self.id})")
        except oracledb.IntegrityError as e:
            if conn: conn.rollback()
            if e.args[0].code == 1:
                print("[WARNING] Número de serie ya existe")
            else:
                print(f"[ERROR] Integridad | {e}")
        except Exception as e:
            if conn: conn.rollback()
            print(f"[ERROR] Insertar equipo | {e}")
        finally:
            if cursor: cursor.close()
            if conn: conn.close()

    def mostrar_datos(self):
        return (f"Equipo\n"
                f"  ID: {self.id}\n"
                f"  Tipo: {self.tipo}\n"
                f"  Marca: {self.marca}\n"
                f"  Modelo: {self.modelo}\n"
                f"  Serie: {self.serie}")
