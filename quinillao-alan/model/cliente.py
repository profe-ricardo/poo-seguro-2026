from config.app_config import conectar_db, oracledb

def validar_tabla_cliente():
    consulta_sql = """
        create table if not exists clientes (
            id NUMBER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1) PRIMARY KEY,
            nombre varchar2(100),
            telefono varchar2(30),
            correo varchar2(100),
            constraint uq_cliente unique (nombre, telefono, correo)
        );
    """
    conn = None
    cursor = None

    try:
        conn = conectar_db()

        if conn:
            cursor = conn.cursor()
            cursor.execute(consulta_sql)
            print("[INFO] Tabla clientes creada correctamente")
    except Exception as e:
        print(f"[ERROR] Creación de tabla clientes | {e}")
    finally:
        if cursor:
            cursor.close()
            
        if conn:
            conn.close()

def insertar_datos_cliente(nombre: str, telefono: str, correo: str):
    consulta_insert = "insert into clientes (nombre, telefono, correo) values (:1, :2, :3)"
    conn = None
    cursor = None

    try:
        conn = conectar_db()

        if conn:
            cursor = conn.cursor()
            cursor.execute(consulta_insert, (nombre, telefono, correo)) # Se entrega los datos parametrizados
            conn.commit()

            print("[INFO] Cliente insertado correctamente")
    except oracledb.IntegrityError as e:
        if conn:
            conn.rollback()

        error = e.args[0]

        if error.code == 1:
            print("[WARNING] El cliente ya registrado")
        else:
            print(f"[ERROR] Error de integridad | {e}")
    except Exception as e:
        if conn:
            conn.rollback()

        print(f"[ERROR] Cliente no registrado | {e}")
    finally:
        if cursor:
            cursor.close()

        if conn:
            conn.close()

def bd_actualizar_telefono(cliente: Cliente, nuevo_telefono:str):
    consulta_update = '''update clientes
                        set telefono = :1
                        where nombre = :2 and correo = :3 and telefono = :4
                    '''
    conn = None
    cursor = None

    try:
        conn = conectar_db()

        if conn:
            cursor = conn.cursor()
            cursor.execute(consulta_update, (cliente.nombre, cliente.correo, cliente.telefono)) # Se entrega los datos parametrizados
            conn.commit()

            print("[INFO] Telefono del cliente actualizado correctamente")
    except oracledb.IntegrityError as e:
        if conn:
            conn.rollback()

        error = e.args[0]

        if error.code == 1:
            print("[WARNING] Combinacion nombre-telefono-correo ya existe")
        else:
            print(f"[ERROR] Error de integridad | {e}")
    except Exception as e:
        if conn:
            conn.rollback()

        print(f"[ERROR] Cliente no registrado | {e}")
    finally:
        if cursor:
            cursor.close()

        if conn:
            conn.close()

class ClienteRepositorio:
    def __init__(self):
        pass

    def actualizar_telefono(self, nuevo_telefono:str):
        if isinstance(nuevo_telefono, str):
            bd_actualizar_telefono()
            self.telefono=nuevo_telefono
        else:
            print("Telefono no corresponde a tipo str")

class Cliente:
    def __init__(self, nombre:str,telefono:str, correo:str):
        self.nombre=nombre
        self.telefono=telefono
        self.correo=correo

        validar_tabla_cliente()
        insertar_datos_cliente(self.nombre, self.telefono, self.correo)

    def mostrar_datos(self):
        return f'Cliente: {self.nombre} | Correo: {self.correo} | Teléfono: {self.telefono}'




