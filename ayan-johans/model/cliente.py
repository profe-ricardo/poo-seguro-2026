from config.app_config import conectar_db

class Cliente:
#atributos
    def __init__(self, nombre: str, correo: str, telefono: str):
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    consulta_sql = """
        create table if not exists clientes(
            id int generated always as identify (start with 1 increment by 1) primary key, 
            nombre varchar2(100),
            telefono varchar2(30),
            correo varchar2(100)
        )
    """
    try:
        conn = conectar_db
        if conn:
            cursor = conn.cursor
            cursor.execute(consulta_sql)
            print("La tabla Clientes fue creada con exito")
    except Exception as e:
        print("Error al intentar crear la tabla Clientes")
    finally:
        cursor.close()
        conn.close()

#metodos
    def actualizar_telefono(self, nuevo_telefono: str):
        if isinstance(nuevo_telefono, str):
#isinstance: recibe un dato
            self.telefono = nuevo_telefono
        else:
            print("Telefono no corresponde al tipo requerido (str) :(")

    def mostrar_datos(self):
        return f'Cliente: {self.nombre} | Correo: {self.correo} | Telefono: {self.telefono}'
    