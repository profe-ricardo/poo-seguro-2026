from config.app_config import conectar_db, oracledb
from .cliente import Cliente
from .equipo import Equipo

class OrdenServicio():
    def __init__(self, numero: int, descripcion: str, estado: str, diagnostico: str, cliente: Cliente, equipo: Equipo):
        self.numero = numero
        self.descripcion = descripcion
        self.estado = estado or "Recibido"
        self.diagnostico = diagnostico or ""
        self.cliente = cliente
        self.equipo = equipo

    def cambiar_estado(self, nuevo_estado: str):
        if isinstance(nuevo_estado, str):
            self.nuevo_estado = nuevo_estado
        else:
            print("Nuevo estado no corresponde a tipo str")

    def registrar_diagnostico(self, diagnostico: str):
        if isinstance(diagnostico, str):
            self.diagnostico = diagnostico
        else:
            print("Diagnostico no corresponde a tipo str")

    def mostrar_resumen(self):
        return f"Orden de Servicio\n Numero: {self.numero} | Cliente: {self.cliente.nombre} | Equipo: {self.equipo.tipo} {self.equipo.marca}"

def validar_tabla_orden_servicio():
    consulta_sql = """
        create table if not exists ordenes_servicio (
            id NUMBER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1) PRIMARY KEY,
            numero number not null,
            descripcion varchar2(250) not null,
            estado varchar2(50) not null,
            diagnostico varchar2(500),
            cliente_correo varchar2(100) not null,
            equipo_serie varchar2(100) not null,
            constraint uq_orden_numero unique (numero)
        )
    """
    conn = None
    cursor = None

    try:
        conn = conectar_db()

        if conn:
            cursor = conn.cursor()
            cursor.execute(consulta_sql)
            print("[INFO] Tabla ordenes_servicio creada correctamente")
    except Exception as e:
        print(f"[ERROR] Creación de tabla ordenes_servicio | {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def insertar_orden_servicio(orden: OrdenServicio):
    consulta_insert = """
        insert into ordenes_servicio (numero, descripcion, estado, diagnostico, cliente_correo, equipo_serie)
        values (:1, :2, :3, :4, :5, :6)
    """
    conn = None
    cursor = None

    try:
        conn = conectar_db()

        if conn:
            cursor = conn.cursor()
            cursor.execute(
                consulta_insert,
                (orden.numero,orden.descripcion,orden.estado,orden.diagnostico,orden.cliente.correo,orden.equipo.serie))
            conn.commit()
            print("[INFO] Orden de servicio guardada correctamente")
    except oracledb.IntegrityError as e:
        if conn:
            conn.rollback()

        error = e.args

        if error.code == 1:
            print("[WARNING] El número de orden de servicio ya existe")
        else:
            print(f"[ERROR] Error de integridad | {e}")
    except Exception as e:
        if conn:
            conn.rollback()
        print(f"[ERROR] Orden de servicio no registrada | {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def actualizar_estado_orden(numero_orden: int, nuevo_estado: str):
    consulta_update = "update ordenes_servicio set estado = :1 where numero = :2"
    conn = None
    cursor = None

    try:
        conn = conectar_db()

        if conn:
            cursor = conn.cursor()
            cursor.execute(consulta_update, (nuevo_estado, numero_orden))
            conn.commit()

            if cursor.rowcount > 0:
                print("[INFO] Estado de la orden actualizado correctamente")
            else:
                print("[WARNING] No se encontró una orden con ese número")
    except Exception as e:
        if conn:
            conn.rollback()
        print(f"[ERROR] No se pudo actualizar el estado | {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def actualizar_diagnostico_orden(numero_orden: int, diagnostico: str):
    consulta_update = "update ordenes_servicio set diagnostico = :1 where numero = :2"
    conn = None
    cursor = None

    try:
        conn = conectar_db()

        if conn:
            cursor = conn.cursor()
            cursor.execute(consulta_update, (diagnostico, numero_orden))
            conn.commit()

            if cursor.rowcount > 0:
                print("[INFO] Diagnóstico registrado correctamente")
            else:
                print("[WARNING] No se encontró una orden con ese número")
    except Exception as e:
        if conn:
            conn.rollback()
        print(f"[ERROR] No se pudo registrar el diagnóstico | {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()