import bcrypt

from config.app_config import conectar_db, oracledb

def validar_tabla_cliente():
    """ Solo puede existir un único registro que tenga (nombre, telefono, correo), si se registra otro igual lanzará error. """
    consulta_sql = """
        create table if not exists clientes (
            id NUMBER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1) PRIMARY KEY,
            nombre varchar2(100) not null,
            telefono varchar2(30),
            correo varchar2(100) not null,
            clave varchar2(150) not null
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

def insertar_datos_cliente(cliente: Cliente):
    consulta_insert = "insert into clientes (nombre, telefono, correo, clave) values (:1, :2, :3, :4)"
    conn = None
    cursor = None

    try:
        clave_bytes = cliente.clave.encode('utf-8')         # Transformamos la clave de str a bytes
        salt = bcrypt.gensalt()                             # Se genera un salt aleatorio para cada clave
        clave_encriptada = bcrypt.hashpw(clave_bytes, salt) # Se encripta la clave
        clave_str = clave_encriptada.decode('utf-8')        # Transformamos a str

        conn = conectar_db()

        if conn:
            cursor = conn.cursor()
            cursor.execute(consulta_insert, (cliente.nombre, cliente.telefono, cliente.correo, clave_str)) # Se entrega los datos parametrizados
            conn.commit()

            print("[INFO] Cliente insertado correctamente")
    except oracledb.IntegrityError as e:
        if conn:
            conn.rollback() # Si algo falla, nos aseguramos de que nada cambie en la bd

        error = e.args[0]

        if error.code == 1:
            print("[WARNING] El cliente ya registrado") # El error ORA-00001 indica prohibición de datos duplicados (constraint uq_cliente)
        else:
            print(f"[ERROR] Error de integridad | {e}")
    except Exception as e:
        if conn:
            conn.rollback() # Si algo falla, nos aseguramos de que nada cambie en la bd

        print(f"[ERROR] Cliente no registrado | {e}")
    finally:
        if cursor:
            cursor.close()

        if conn:
            conn.close()

def iniciar_sesion(correo: str, clave: str):
    consulta = "select nombre, telefono, clave from clientes where correo = :1"
    conn = None
    cursor = None

    try:
        conn = conectar_db()

        if conn:
            cursor = conn.cursor()
            cursor.execute(consulta, (correo,))

            if cursor.fetchone():
                datos_usuario = cursor.fetchone()
                clave_bd = str(datos_usuario.get('clave'))

                # Se deben transformar ambas claves a bytes para validarlas
                clave_bd_bytes = clave_bd.encode('utf-8')
                clave_bytes = clave.encode('utf-8')

                if bcrypt.checkpw(clave_bytes, clave_bd_bytes):
                    print("Ingreso correcto")
                    return Cliente(str(datos_usuario.get('nombre')), str(datos_usuario.get('telefono')), correo, clave)
                else:
                    print(f"[ERROR] Credenciales incorrectas")
                    return False            
            else:
                print(f"[ERROR] Credenciales incorrectas | {e}")
                return False
            
    except Exception as e:
        print(f"[ERROR] Obtención de clave | {e}")
        return False
    finally:
        if cursor:
            cursor.close()
            
        if conn:
            conn.close()


class ClienteRepositorio():
    def __init__(self):
        pass

    def actualizar_telefono(self, nuevo_telefono: str):
        """ Actualiza telefono en bd """

        if isinstance(nuevo_telefono, str):
            consulta_update = """
                update clientes set telefono = :1
                where nombre = :2 and correo = :3 and telefono = :4
            """
            conn = None
            cursor = None

            try:
                conn = conectar_db()

                if conn:
                    cursor = conn.cursor()
                    cursor.execute(consulta_update, (nuevo_telefono, self.nombre, self.correo, self.telefono)) # Se entrega los datos parametrizados
                    conn.commit()

                    print("[INFO] Teléfono del cliente actualizado correctamente")
            except oracledb.IntegrityError as e:
                if conn:
                    conn.rollback() # Si algo falla, nos aseguramos de que nada cambie en la bd

                error = e.args[0]

                if error.code == 1:
                    print("[WARNING] Combinación nombre-telefono-correo ya existe") # El error ORA-00001 indica prohibición de datos duplicados (constraint uq_cliente)
                else:
                    print(f"[ERROR] Error de integridad | {e}")
            except Exception as e:
                if conn:
                    conn.rollback() # Si algo falla, nos aseguramos de que nada cambie en la bd

                print(f"[ERROR] No se pudo actualizar telefono | {e}")
            finally:
                if cursor:
                    cursor.close()

                if conn:
                    conn.close()
        else:
            print("Telefono no corresponde a tipo str")

class Cliente(ClienteRepositorio):
    def __init__(self, nombre: str, telefono: str, correo: str, clave: str):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.clave = clave

        validar_tabla_cliente() # Creamos la tabla / validamos que exista
        insertar_datos_cliente(self)

    def mostrar_datos(self):
        return f"Persona\n Nombre: {self.nombre} | Telefono: {self.telefono} | Correo: {self.correo}"
