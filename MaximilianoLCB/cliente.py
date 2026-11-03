class cliente():
    def __init__(self, nombre: str, telefono: str, correo: str):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

    def mostrar_datos(self): 
        return f"Nombre: {self.nombre} | telefono: {self.telefono} | correo: {self.correo}"

    def actualizar_telefono(self, nuevo_telefono: str):
        if isinstance(nuevo_telefono, str):
         self.telefono = nuevo_telefono
        else: 
           print("Telefono no corresponde a str")