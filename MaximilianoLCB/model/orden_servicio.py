from config.app_config import conectar_db, oracledb
from .cliente import Cliente
from .equipo import Equipo

def validar_tablas_orden():
    consultas = [
        """
        create table ordenes_servicio (
            id NUMBER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1) PRIMARY KEY,
            numero NUMBER not null,
            descripcion varchar2(500),
            estado varchar2(30) not null,
            diagnostico varchar2(1000),
            cliente_id NUMBER not null,
            equipo_id NUMBER not null,
            constraint uq_orden_numero unique (numero),
            constraint fk_orden_cliente foreign key (cliente_id) references clientes(id),
            constraint fk_orden_equipo foreign key (equipo_id) references equipos(id)
        )
        """
        """
        create table historial_estados (
            id NUMBER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1) PRIMARY KEY,
            orden_id NUMBER not null,
            estado varchar2(30) not null,
            fecha timestamp default systimestamp,
            constraint fk_historial_orden foreign key (orden_id) references ordenes_servicio(id)
        )
        """
    ]
    conn = None
    cursor = None

    try:
        conn = conectar_db()

        if conn:
            cursor = conn.cursor()

            for consulta in consultas:
                try:
                    cursor.execute(consulta)
                except oracledb.DatabaseError as e:
                    if e.args[0].code != 955:  # ORA-00955: ya existe
                        raise
    except Exception as e:
        print(f"[ERROR] Creación de tablas de orden | {e}")
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

        validar_tablas_orden()
        self.guardar()

    # 1.- Guardar orden de servicio en bd
    def guardar(self):
        consulta_cliente = "select id from clientes where nombre = :1 and telefono = :2 and correo = :3"
        consulta_equipo = "select id from equipos where serie = :1"
        consulta_insert = """
            insert into ordenes_servicio (numero, descripcion, estado, diagnostico, cliente_id, equipo_id)
            values (:1, :2, :3, :4, :5, :6)
        """
        conn = None
        cursor = None

        try:
            conn = conectar_db()

            if conn:
                cursor = conn.cursor()

                cursor.execute(consulta_cliente, (self.cliente.nombre, self.cliente.telefono, self.cliente.correo))
                fila_cliente = cursor.fetchone()
                cursor.execute(consulta_equipo, (self.equipo.serie,))
                fila_equipo = cursor.fetchone()

                if not fila_cliente or not fila_equipo:
                    print("[ERROR] El cliente o el equipo no existen en la bd")
                    return

                cursor.execute(
                    consulta_insert,
                    (self.numero, self.descripcion, self.estado, self.diagnostico, fila_cliente[0], fila_equipo[0])
                )
                conn.commit()

                print("[INFO] Orden de servicio guardada correctamente")
        except oracledb.IntegrityError as e:
            if conn:
                conn.rollback()

            if e.args[0].code == 1:
                print("[WARNING] Ya existe una orden con ese número")
            else:
                print(f"[ERROR] Error de integridad | {e}")
        except Exception as e:
            if conn:
                conn.rollback()

            print(f"[ERROR] Orden no registrada | {e}")
        finally:
            if cursor:
                cursor.close()

            if conn:
                conn.close()

    # 2.- Registrar cambio estado en bd
    def cambiar_estado(self, nuevo_estado: str):
        if not isinstance(nuevo_estado, str):
            print("Nuevo estado no corresponde a tipo str")
            return

        consulta_update = "update ordenes_servicio set estado = :1 where numero = :2"
        consulta_historial = """
            insert into historial_estados (orden_id, estado)
            select id, :1 from ordenes_servicio where numero = :2
        """
        conn = None
        cursor = None

        try:
            conn = conectar_db()

            if conn:
                cursor = conn.cursor()
                cursor.execute(consulta_update, (nuevo_estado, self.numero))
                cursor.execute(consulta_historial, (nuevo_estado, self.numero))
                conn.commit()  # update + historial en la misma transacción

                self.estado = nuevo_estado
                print("[INFO] Estado actualizado correctamente")
        except Exception as e:
            if conn:
                conn.rollback()

            print(f"[ERROR] No se pudo cambiar el estado | {e}")
        finally:
            if cursor:
                cursor.close()

            if conn:
                conn.close()

    # 3.- Registrar diagnostico en bd
    def registrar_diagnostico(self, diagnostico: str):
        if not isinstance(diagnostico, str):
            print("Diagnóstico no corresponde a tipo str")
            return

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
                print("[INFO] Diagnóstico registrado correctamente")
        except Exception as e:
            if conn:
                conn.rollback()

            print(f"[ERROR] No se pudo registrar el diagnóstico | {e}")
        finally:
            if cursor:
                cursor.close()

            if conn:
                conn.close()