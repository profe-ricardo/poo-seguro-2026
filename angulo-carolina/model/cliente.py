class Cliente:
  def __init__(self, nombre: str, correo: str, telefono: str):
    self.nombre = nombre
    self.correo = correo
    self.telefono = telefono

    consulta_sql = """
      create table if not exists clientes (
        id NUMBER GENERATED ALWAYS AS IDENTUTY (START WITH 1 ) 
        nombre varchar2(100)
        telefono varchar2(30)
        correo varchae2(100)
      )
    """

    try:
       conn = conectar_db()

       if conn:
          cursor = conn.cursor()
          cursor.execute(consulta_sql)
          print("[INFO] Tabla clientes creada correctamente")

    except: Exception as e:
        print("[ERROR] Creación de Tablas Clientes")
    finally:
        cursor.close()
        conn.close()
    
  def actualizar_telefono(self, nuevo_telefono: str):
        if isinstance(nuevo_telefono, str):
            self.telefono = nuevo_telefono
        else:
           print("Telefono no corresponde a tipo str")
  
  def mostrar_datos(self):
   return f'Cliente: {self.nombre} | Correo: {self.correo} | Teléfono: {self.telefono}



