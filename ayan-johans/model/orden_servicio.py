# Guardar orden de servicio en DB
# Registrar cambio de estado en DB
# Registrar diagnostico en DB
from config.app_config import conectar_db, oracledb
from model.cliente import Cliente
from model.equipo import Equipo

class OrdenServicio:
    def __init__(self, numero: int, descripcion: str, estado: str, diagnostico: str, cliente: Cliente, equipo: Equipo):
        self.numero = numero
        self.descripcion = descripcion
        self.estado = estado or 'recibida'
        self.diagnostico = diagnostico or ''
        self.cliente = cliente
        self.equipo = equipo

        validar_tabla_orden()
        insertar_datos_orden(self.numero, self.descripcion, self.estado, self.diagnostico, self.cliente.nombre, self.equipo.serie)

    def cambiar_estado(self, nuevo_estado: str):
        if isinstance(nuevo_estado, str):
            bd_cambiar_estado(self.numero, nuevo_estado)
            self.estado = nuevo_estado
        else:
            print("Tipo de dato no valido")

    def registrar_diagnostico(self, diagnostico):
        if isinstance(diagnostico, str):
            bd_registrar_diagnostico(self.numero, diagnostico)
            self.diagnostico = diagnostico
        else:
            print("Tipo de dato no valido")

    def mostrar_resumen(self):
        return f'Orden N° {self.numero} | Cliente: {self.cliente.nombre} | Equipo: {self.equipo.tipo} {self.equipo.marca} | Estado: {self.estado}'

def validar_tabla_orden():
    consulta_sql = """
        create table if not exists ordenes_servicio (
            id number generated always as identity (start with 1 increment by 1) primary key,
            numero number unique,
            descripcion varchar2(250),
            estado varchar2(50),
            diagnostico varchar2(250),
            cliente_nombre varchar2(100),
            equipo_serie varchar2(100)
        )
    """

    conn = None
    cursor = None

    try:
        conn = conectar_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute(consulta_sql)
            print("[INFO] Tabla 'ordenes_servicio' creada correctamente")
    except Exception as e:
        print(f"[ERROR] Creacion de tabla 'ordenes_servicio' fallida | {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def insertar_datos_orden(numero: int, descripcion: str, estado: str, diagnostico: str, cliente_nombre: str, equipo_serie: str):
    consulta_insert = """
        insert into ordenes_servicio (numero, descripcion, estado, diagnostico, cliente_nombre, equipo_serie) values (:1, :2, :3, :4, :5, :6)
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
            print("[ADVERTENCIA] El numero de orden ya está registrado")
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

def bd_cambiar_estado(numero_orden: int, nuevo_estado: str):
    consulta_update = """
        update ordenes_servicio set estado = :1 where numero = :2
    """

    conn = None
    cursor = None

    try:
        conn = conectar_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute(consulta_update, (nuevo_estado, numero_orden))
            conn.commit()
            print(f"[INFO] Estado de la orden N° {numero_orden} actualizado a '{nuevo_estado}'")
    except Exception as e:
        if conn:
            conn.rollback()
        print(f"[ERROR] No se pudo actualizar el estado | {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def bd_registrar_diagnostico(numero_orden: int, nuevo_diagnostico: str):
    consulta_update = """
        update ordenes_servicio set diagnostico = :1 where numero = :2
        """
    conn = None
    cursor = None

    try:
        conn = conectar_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute(consulta_update, (nuevo_diagnostico, numero_orden))
            conn.commit()
            print(f"[INFO] Diagnostico de la orden N° {numero_orden} registrado en la base de datos")
    except Exception as e:
        if conn:
            conn.rollback()
        print(f"[ERROR] No se pudo registrar el diagnostico | {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
