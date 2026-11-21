from config.app_config import conectar_db, oracledb

def validar_tabla_cliente():
    consulta_sql = """
        CREATE TABLE IF NOT EXISTS clientes (
            id NUMBER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1) PRIMARY KEY,
            nombre VARCHAR2(100) NOT NULL,
            telefono VARCHAR2(30) NOT NULL,
            correo VARCHAR2(100) NOT NULL,
            CONSTRAINT uq_cliente UNIQUE (nombre, telefono, correo)
        )
    """
    conn = cursor = None
    try:
        conn = conectar_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute(consulta_sql)
            print("[INFO] Tabla clientes OK")
    except Exception as e:
        print(f"[ERROR] Creación tabla clientes | {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


class Cliente:
    def __init__(self, nombre: str, telefono: str, correo: str, id: int = None):
        self.id = id
        self.nombre = nombre.strip()
        self.telefono = telefono.strip()
        self.correo = correo.strip().lower()

        if self.id is None:
            validar_tabla_cliente()
            self._insertar()

    def _insertar(self):
        sql = """
            INSERT INTO clientes (nombre, telefono, correo) 
            VALUES (:1, :2, :3) 
            RETURNING id INTO :4
        """
        conn = cursor = None
        try:
            conn = conectar_db()
            if conn:
                cursor = conn.cursor()
                id_var = cursor.var(oracledb.NUMBER)
                cursor.execute(sql, (self.nombre, self.telefono, self.correo, id_var))
                conn.commit()
                self.id = int(id_var.getvalue()[0])
                print(f"[INFO] Cliente insertado (ID: {self.id})")
        except oracledb.IntegrityError as e:
            if conn: conn.rollback()
            if e.args[0].code == 1:
                print("[WARNING] Cliente ya existe")
            else:
                print(f"[ERROR] Integridad | {e}")
        except Exception as e:
            if conn: conn.rollback()
            print(f"[ERROR] Insertar cliente | {e}")
        finally:
            if cursor: cursor.close()
            if conn: conn.close()

    def actualizar_telefono(self, nuevo_telefono: str):
        if not isinstance(nuevo_telefono, str) or not nuevo_telefono.strip():
            print("[ERROR] Teléfono inválido")
            return

        sql = "UPDATE clientes SET telefono = :1 WHERE id = :2"
        conn = cursor = None
        try:
            conn = conectar_db()
            if conn:
                cursor = conn.cursor()
                cursor.execute(sql, (nuevo_telefono.strip(), self.id))
                conn.commit()
                self.telefono = nuevo_telefono.strip()
                print("[INFO] Teléfono actualizado correctamente")
        except Exception as e:
            if conn: conn.rollback()
            print(f"[ERROR] Actualizar teléfono | {e}")
        finally:
            if cursor: cursor.close()
            if conn: conn.close()

    def mostrar_datos(self):
        return (f"Cliente\n"
                f"  ID: {self.id}\n"
                f"  Nombre: {self.nombre}\n"
                f"  Teléfono: {self.telefono}\n"
                f"  Correo: {self.correo}")
