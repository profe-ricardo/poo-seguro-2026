from config.app_config import conectar_db, oracledb
from model.cliente import Cliente
from model.equipo import Equipo

def validar_tabla_ordenes():
    consulta_sql = """
        create table if not exists ordenes_servicio (
            numero number PRIMARY KEY,
            descripcion varchar2(100),
            estado varchar2(20),
            diagnostico varchar2(100),
            cliente_id number,
            equipo_id number,
            FOREIGN KEY(cliente_id) REFERENCES clientes(id),
            FOREIGN KEY(equipo_id) REFERENCES equipos(id)
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
            print("[INFO] Tabla ordenes_servicio validada correctamente")
    except Exception as e:
        print(f"[ERROR] Durante creación de tabla ordenes_servicio | {e}")
    finally:
        if cursor:
            cursor.close()
            
        if conn:
            conn.close()

def insertar_datos_orden(orden: OrdenServicio):
    consulta_select_cliente = """
        select id from clientes
        where (
            clientes.nombre = :1
            and clientes.telefono = :2
            and clientes.correo = :3
        );
    """

    consulta_select_equipo = """
        select id from equipos
        where (
            equipos.tipo = :1
            and equipos.marca = :2
            and equipos.modelo = :3
            and equipos.serie = :4
        );
    """

    consulta_insert = """
        insert into ordenes_servicio (
            numero,
            descripcion,
            estado,
            diagnostico,
            cliente_id,
            equipo_id
        ) 
        values (:1, :2, :3, :4, :5, :6);
    """
    conn = None
    cursor = None

    try:
        conn = conectar_db()

        if conn:
            cursor = conn.cursor()

            cursor.execute(consulta_select_cliente, (orden.cliente.nombre, orden.cliente.telefono, orden.cliente.correo))
            cliente_id = str(cursor.fetchall()[0][0])

            cursor.execute(consulta_select_equipo,(orden.equipo.tipo, orden.equipo.marca, orden.equipo.modelo, orden.equipo.serie))
            equipo_id = str(cursor.fetchall()[0][0])

            cursor.execute(consulta_insert, (orden.numero, orden.descripcion, orden.estado, orden.diagnostico, cliente_id, equipo_id))
            conn.commit()

            print("[INFO] Orden registrada correctamente")
    except oracledb.IntegrityError as e:
        if conn:
            conn.rollback() # Si algo falla, nos aseguramos de que nada cambie en la bd

        error = e.args[0]

        if error.code == 1:
            print("[WARNING] Esta orden ya fue registrado") # El error ORA-00001 indica prohibición de datos duplicados (constraint uq_cliente)
        else:
            print(f"[ERROR] Error de integridad | {e}")
    except Exception as e:
        if conn:
            conn.rollback() # Si algo falla, nos aseguramos de que nada cambie en la bd

        print(f"[ERROR] Orden no se logro registrar | {e}")
    finally:
        if cursor:
            cursor.close()

        if conn:
            conn.close()

class OrdenServicio_Repositorio():
    def __init__(self):
        pass

    def bd_registrar_diagnostico(orden: OrdenServicio, diagnostico: str):
        consulta_update = """
            update ordenes_servicio set diagnostico = :1
            where numero = :2;
        """
        conn = None
        cursor = None
    
        try:
            conn = conectar_db()
    
            if conn:
                cursor = conn.cursor()
                cursor.execute(consulta_update, (diagnostico, orden.numero)) # Se entrega los datos parametrizados
                conn.commit()
    
                print("[INFO] Diagnostico registrado correctamente")
        except oracledb.IntegrityError as e:
            if conn:
                conn.rollback() # Si algo falla, nos aseguramos de que nada cambie en la bd
    
            error = e.args[0]
    
            if error.code == 1:
                print("[WARNING] Ni idea como llegaría a este error") # El error ORA-00001 indica prohibición de datos duplicados (constraint uq_cliente)
            else:
                print(f"[ERROR] Error de integridad | {e}")
        except Exception as e:
            if conn:
                conn.rollback() # Si algo falla, nos aseguramos de que nada cambie en la bd
    
            print(f"[ERROR] Diagnostico no se pudo registrar | {e}")
        finally:
            if cursor:
                cursor.close()
    
            if conn:
                conn.close()

    def bd_actualizar_estado(orden: OrdenServicio, estado: str):
        consulta_update = """
            update ordenes_servicio set estado = :1
            where numero = :2;
        """
        conn = None
        cursor = None
    
        try:
            conn = conectar_db()
    
            if conn:
                cursor = conn.cursor()
                cursor.execute(consulta_update, (estado, orden.numero)) # Se entrega los datos parametrizados
                conn.commit()
    
                print("[INFO] Estado actualizado correctamente")
        except oracledb.IntegrityError as e:
            if conn:
                conn.rollback() # Si algo falla, nos aseguramos de que nada cambie en la bd
    
            error = e.args[0]
    
            if error.code == 1:
                print("[WARNING] Ni idea como llegaría a este error") # El error ORA-00001 indica prohibición de datos duplicados
            else:
                print(f"[ERROR] Error de integridad | {e}")
        except Exception as e:
            if conn:
                conn.rollback() # Si algo falla, nos aseguramos de que nada cambie en la bd
    
            print(f"[ERROR] Estado no se pudo actualizar | {e}")
        finally:
            if cursor:
                cursor.close()
    
            if conn:
                conn.close()

class OrdenServicio(OrdenServicio_Repositorio):
    def __init__(self, numero: int, descripcion: str, estado: str, diagnostico: str, cliente: Cliente, equipo: Equipo):
        self.numero = numero
        self.descripcion = descripcion
        self.estado = estado or "recibida"
        self.diagnostico = diagnostico or ""
        self.cliente = cliente
        self.equipo = equipo

        validar_tabla_ordenes()
        insertar_datos_orden(self)

    def cambiar_estado(self, nuevo_estado: str):
        if isinstance(nuevo_estado, str):
            self.estado = nuevo_estado
            self.bd_actualizar_estado(self, nuevo_estado)
        else:
            print("Estado no corresponde a tipo String")

    def registrar_diagnostico(self, diagnostico: str):
        if isinstance(diagnostico, str):
            self.diagnostico = diagnostico
            self.bd_registrar_diagnostico(self, diagnostico)
        else:
            print("Diagnostico no corresponde a tipo String")

    def mostrar_resumen(self):
          return f"Orden N°{self.numero} | Cliente: {self.cliente.nombre} | Equipo: {self.equipo.tipo} {self.equipo.marca} | Estado: {self.estado}"