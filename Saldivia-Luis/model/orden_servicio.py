from config.app_config import conectar_db, oracledb
from model.cliente import Cliente
from model.equipo import Equipo

def validar_tabla_orden_servicio():
    consulta_sql = """
        CREATE TABLE IF NOT EXISTS ordenes_servicio (
            id NUMBER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1) PRIMARY KEY,
            numero NUMBER NOT NULL,
            descripcion VARCHAR2(300) NOT NULL,
            estado VARCHAR2(50) DEFAULT 'Recepcionado' NOT NULL,
            diagnostico VARCHAR2(500),
            cliente_id NUMBER NOT NULL,
            equipo_id NUMBER NOT NULL,
            CONSTRAINT fk_orden_cliente FOREIGN KEY (cliente_id) REFERENCES clientes(id),
            CONSTRAINT fk_orden_equipo FOREIGN KEY (equipo_id) REFERENCES equipos(id),
            CONSTRAINT uq_numero_orden UNIQUE (numero)
        )
    """
    conn = cursor = None
    try:
        conn = conectar_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute(consulta_sql)
            print("[INFO] Tabla ordenes_servicio OK")
    except Exception as e:
        print(f"[ERROR] Creación tabla ordenes_servicio | {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


class OrdenServicio:
    def __init__(self, numero: int, descripcion: str, cliente: Cliente, equipo: Equipo,
                 estado: str = "Recepcionado", diagnostico: str = "", id: int = None):
        self.id = id
        self.numero = numero
        self.descripcion = descripcion.strip()
        self.estado = estado.strip()
        self.diagnostico = diagnostico.strip() if diagnostico else ""
        self.cliente = cliente
        self.equipo = equipo

        if self.id is None:
            validar_tabla_orden_servicio()
            self._insertar()

    def _insertar(self):
        sql = """
            INSERT INTO ordenes_servicio 
                (numero, descripcion, estado, diagnostico, cliente_id, equipo_id)
            VALUES (:1, :2, :3, :4, :5, :6)
            RETURNING id INTO :7
        """
        conn = cursor = None
        try:
            conn = conectar_db()
            if conn:
                cursor = conn.cursor()
                id_var = cursor.var(oracledb.NUMBER)
                cursor.execute(sql, (
                    self.numero,
                    self.descripcion,
                    self.estado,
                    self.diagnostico,
                    self.cliente.id,
                    self.equipo.id,
                    id_var
                ))
                conn.commit()
                self.id = int(id_var.getvalue()[0])
                print(f"[INFO] Orden de servicio creada (ID: {self.id})")
        except oracledb.IntegrityError as e:
            if conn: conn.rollback()
            print(f"[ERROR] Integridad al crear orden | {e}")
        except Exception as e:
            if conn: conn.rollback()
            print(f"[ERROR] Crear orden | {e}")
        finally:
            if cursor: cursor.close()
            if conn: conn.close()

    def cambiar_estado(self, nuevo_estado: str):
        if not isinstance(nuevo_estado, str) or not nuevo_estado.strip():
            print("[ERROR] Estado inválido")
            return

        sql = "UPDATE ordenes_servicio SET estado = :1 WHERE id = :2"
        conn = cursor = None
        try:
            conn = conectar_db()
            if conn:
                cursor = conn.cursor()
                cursor.execute(sql, (nuevo_estado.strip(), self.id))
                conn.commit()
                self.estado = nuevo_estado.strip()
                print(f"[INFO] Estado actualizado a: {self.estado}")
        except Exception as e:
            if conn: conn.rollback()
            print(f"[ERROR] Cambiar estado | {e}")
        finally:
            if cursor: cursor.close()
            if conn: conn.close()

    def registrar_diagnostico(self, diagnostico: str):
        if not isinstance(diagnostico, str):
            print("[ERROR] Diagnóstico inválido")
            return

        sql = "UPDATE ordenes_servicio SET diagnostico = :1 WHERE id = :2"
        conn = cursor = None
        try:
            conn = conectar_db()
            if conn:
                cursor = conn.cursor()
                cursor.execute(sql, (diagnostico.strip(), self.id))
                conn.commit()
                self.diagnostico = diagnostico.strip()
                print("[INFO] Diagnóstico registrado")
        except Exception as e:
            if conn: conn.rollback()
            print(f"[ERROR] Registrar diagnóstico | {e}")
        finally:
            if cursor: cursor.close()
            if conn: conn.close()

    def mostrar_resumen(self):
        return (f"Orden de Servicio #{self.numero}\n"
                f"  ID: {self.id}\n"
                f"  Estado: {self.estado}\n"
                f"  Descripción: {self.descripcion}\n"
                f"  Diagnóstico: {self.diagnostico or 'Sin diagnóstico'}\n"
                f"  Cliente: {self.cliente.nombre} (ID {self.cliente.id})\n"
                f"  Equipo: {self.equipo.tipo} {self.equipo.marca} {self.equipo.modelo} "
                f"(Serie: {self.equipo.serie})")
