from config.app_config import conectar_db

class Cliente():
    def __init__(self, nombre: str, telefono: str, correo: str):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

        consulta_sql = """
            create table if not exists clientes (
                id NUMBER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1) PRIMARY KEY,
                nombre varchar2(100),
                telefono varchar2(30),
                correo varchar2(100)
            );
        """

        try:
            conn = conectar_db()

            if conn:
                cursor = conn.cursor()
                cursor.execute(consulta_sql)
                print("[INFO] Tabla clientes creada correctamente")
        except Exception as e:
            print(f"[ERROR] Creación de tabla clientes | {e}")
        finally:
            cursor.close()
            conn.close()

    def mostrar_datos(self):
        return f"Persona\n Nombre: {self.nombre} | Telefono: {self.telefono} | Correo: {self.correo}"

    def actualizar_telefono(self, nuevo_telefono: str):
        if isinstance(nuevo_telefono, str):
            self.telefono = nuevo_telefono
        else:
            print("Telefono no corresponde a tipo str")