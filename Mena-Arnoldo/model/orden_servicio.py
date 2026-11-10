from config.app_config import conectar_db, oracledb
from cliente import Cliente
from equipo import Equipo

def validar_tabla_orden():
    consulta_sql = """
        create table if not exists ordenes_servicio (
            numero NUMBER PRIMARY KEY,
            descripcion VARCHAR2(255),
            estado VARCHAR2(50),
            diagnostico VARCHAR2(255),
            cliente_nombre VARCHAR2(100),
            equipo_serie VARCHAR2(100)
        );
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

def insertar_datos_orden(numero: int, descripcion: str, estado: str, diagnostico: str, cliente_nombre: str, equipo_serie: str):
    consulta_insert = """
        insert into ordenes_servicio (numero, descripcion, estado, diagnostico, cliente_nombre, equipo_serie)
        values (:1, :2, :3, :4, :5, :6)
    """
    conn = None
    cursor = None

    try:
        conn = conectar_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute(consulta_insert, (numero, descripcion, estado, diagnostico, cliente_nombre, equipo_serie))
            conn.commit()
            print("[INFO] Orden de servicio insertada correctamente")
    except oracledb.IntegrityError as e:
        if conn:
            conn.rollback()
        error = e.args[0]
        if error.code == 1:
            print("[WARNING] La orden de servicio ya está registrada (número duplicado)")
        else:
            print(f"[ERROR] Error de integridad en orden de servicio | {e}")
    except Exception as e:
        if conn:
            conn.rollback()
        print(f"[ERROR] Orden de servicio no registrada | {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

class OrdenServicio():
    def __init__(self, numero: int, descripcion: str, estado: str, diagnostico: str, cliente: Cliente, equipo: Equipo):
        self.numero = numero
        self.descripcion = descripcion
        self.estado = estado or "Recibido"
        self.diagnostico = diagnostico or ""
        self.cliente = cliente
        self.equipo = equipo

        # 1. Validar tabla y 2. Guardar en la base de datos
        validar_tabla_orden()
        insertar_datos_orden(
            self.numero,
            self.descripcion,
            self.estado,
            self.diagnostico,
            self.cliente.nombre,
            self.equipo.serie
        )

    def cambiar_estado(self, nuevo_estado: str):
        if isinstance(nuevo_estado, str):
            consulta_update = "update ordenes_servicio set estado = :1 where numero = :2"
            conn = None
            cursor = None

            try:
                conn = conectar_db()
                if conn:
                    cursor = conn.cursor()
                    cursor.execute(consulta_update, (nuevo_estado, self.numero))
                    conn.commit()
                    
                    self.estado = nuevo_estado
                    print(" Estado de la orden actualizado!")
            except Exception as e:
                if conn:
                    conn.rollback()
                print(f"[ERROR] No se pudo actualizar el estado | {e}")
            finally:
                if cursor:
                    cursor.close()
                if conn:
                    conn.close()
        else:
            print("Nuevo estado no corresponde a tipo str")

    def registrar_diagnostico(self, diagnostico: str):
        if isinstance(diagnostico, str):
            consulta_update = "update ordenes_servicio set diagnostico = :1 where numero = :2"
            conn = None
            cursor = None

            try:
                conn = conectar_db()
                if conn:
                    cursor = conn.cursor()
                    cursor.execute(consulta_update, (diagnostico, self.numero))
                    conn.commit()

                    self.diagnostico = diagnostico
                    print("[INFO] Diagnóstico actualizado en la base de datos")
            except Exception as e:
                if conn:
                    conn.rollback()
                print(f"[ERROR] No se pudo actualizar el diagnóstico | {e}")
            finally:
                if cursor:
                    cursor.close()
                if conn:
                    conn.close()
        else:
            print("Diagnostico no corresponde a tipo str")

    def mostrar_resumen(self):
        return f"Orden de Servicio\n Numero: {self.numero} | Cliente: {self.cliente.nombre} | Equipo: {self.equipo.tipo} {self.equipo.marca}"