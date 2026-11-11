# 1.- Guardar orden de servicio en bd
# 2.- Registrar cambio estado en bd
# 3.- Registrar diagnostico en bd

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


    from config.app_config import conectar_db, oracledb
from .cliente import Cliente
from .equipo import Equipo

def validar_tabla_orden():
    consulta_sql = """
        create table if not exists ordenes_servicio (
            numero NUMBER PRIMARY KEY,
            descripcion varchar2(255),
            estado varchar2(50),
            diagnostico varchar2(500),
            cliente_correo varchar2(100),
            equipo_serie varchar2(50)
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

def insertar_datos_orden(orden: OrdenServicio):
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
                (orden.numero, orden.descripcion, orden.estado, orden.diagnostico, orden.cliente.correo, orden.equipo.serie)
            )
            conn.commit()
            print("[INFO] Orden de servicio insertada correctamente")
    except oracledb.IntegrityError as e:
        if conn:
            conn.rollback()
        error = e.args[0]
        if error.code == 1:
            print("[WARNING] La orden con este número ya está registrada")
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

class OrdenServicioRepositorio():
    def __init__(self):
        pass

    def actualizar_estado_bd(self, nuevo_estado: str):
        consulta_update = "update ordenes_servicio set estado = :1 where numero = :2"
        conn = None
        cursor = None

        try:
            conn = conectar_db()
            if conn:
                cursor = conn.cursor()
                cursor.execute(consulta_update, (nuevo_estado, self.numero))
                conn.commit()
                print("[INFO] Estado de la orden actualizado en la BD")
        except Exception as e:
            if conn:
                conn.rollback()
            print(f"[ERROR] No se pudo actualizar estado en BD | {e}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def registrar_diagnostico_bd(self, diagnostico: str):
        consulta_update = "update ordenes_servicio set diagnostico = :1 where numero = :2"
        conn = None
        cursor = None

        try:
            conn = conectar_db()
            if conn:
                cursor = conn.cursor()
                cursor.execute(consulta_update, (diagnostico, self.numero))
                conn.commit()
                print("[INFO] Diagnóstico de la orden registrado en la BD")
        except Exception as e:
            if conn:
                conn.rollback()
            print(f"[ERROR] No se pudo registrar diagnóstico en BD | {e}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

class OrdenServicio(OrdenServicioRepositorio):
    def __init__(self, numero: int, descripcion: str, estado: str, diagnostico: str, cliente: Cliente, equipo: Equipo):
        self.numero = numero
        self.descripcion = descripcion
        self.estado = estado or "Recibido"
        self.diagnostico = diagnostico or ""
        self.cliente = cliente
        self.equipo = equipo

        validar_tabla_orden() # Creamos la tabla / validamos que exista
        insertar_datos_orden(self)

    def cambiar_estado(self, nuevo_estado: str):
        if isinstance(nuevo_estado, str):
            self.estado = nuevo_estado
            self.actualizar_estado_bd(nuevo_estado) # Actualiza directamente en BD
        else:
            print("Nuevo estado no corresponde a tipo str")

    def registrar_diagnostico(self, diagnostico: str):
        if isinstance(diagnostico, str):
            self.diagnostico = diagnostico
            self.registrar_diagnostico_bd(diagnostico) # Actualiza directamente en BD
        else:
            print("Diagnostico no corresponde a tipo str")

    def mostrar_resumen(self):
        return f"Orden de Servicio\n Numero: {self.numero} | Cliente: {self.cliente.nombre} | Equipo: {self.equipo.tipo} {self.equipo.marca}"