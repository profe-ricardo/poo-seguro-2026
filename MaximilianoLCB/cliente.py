'''from config.app_config import conectar_db'''

class cliente():
    def __init__(self, nombre: str, telefono: str, correo: str):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

        '''consulta_sql = """""
          create table if not exists clientes (
             id serial generated always as identity (start with by 1) primary key,
             nombre varchar2(100),
             telefono varchar2(30),
             correo varchar2(100)
          )"""
        
        try:
           conn = conectar_db()

           if conn:
             cursor = conn.cursor
             cursor.execute(consulta_sql)
             print ("[INFO] Tabla clientes creada correctamente")
        except Exception as e:
           print (f"[ERROR] Tabla cliente creada")'''

    def mostrar_datos(self): 
        return f"Nombre: {self.nombre} | telefono: {self.telefono} | correo: {self.correo}"

    def actualizar_telefono(self, nuevo_telefono: str):
        if isinstance(nuevo_telefono, str):
         self.telefono = nuevo_telefono
        else: 
           print("Telefono no corresponde a str")

        