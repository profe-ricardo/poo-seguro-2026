from config.app_config import conectar_db, oracledb

def validar_tabla_cliente():
    consulta_sql ="""""" #aqui se hace la tabla de cliente
    conn = None 
    cursor = None

    try: #esta echo para que si hay un error no se caiga el programa

        conn = conectar_db() #se conecta a la base de datos
        if conn:
            cursor = conn.cursor() 
            cursor.execute(consulta_sql) 
            print("info: Tabla clientes")
    except Exception as e:
        print(f"error creacion de tabla cliente")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()



class Client():
    def __init__(self, nombre:str, telefono:str,  correo:str):
        self.nombre = nombre 
        self.telefono = telefono
        self.correo =  correo

        
    def actualizar_telefono(self, nuevo_telefono:str):
        if isinstance(nuevo_telefono, str):
            self.telefono = nuevo_telefono
        else:
            print("no es str")
        
        
    def Mostrar_Datos(self): #muestra los 3 self
        return f"Nombre: {self.nombre} | Telefono: {self.telefono} | Correo: {self.correo}" #como self ordena datos




"""   def actualizar_telefono(self, TelefonoNuevo:str): # permite guardar int(str)
        self.telefono = TelefonoNuevo
"""