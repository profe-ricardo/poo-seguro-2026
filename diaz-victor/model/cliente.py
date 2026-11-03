

class Client():
    def __init__(self, nombre:str, telefono:str,  correo:str):
        self.nombre = nombre 
        self.telefono = telefono
        self.correo =  correo

    def actualizar_telefono(self, nuevo_telefono:str):
        if isinstance(nuevo_telefono, str):
            self.telefono = nuevo_telefono
        else: (
            print("no es str")
        )
        
    def Mostrar_Datos(self): #muestra los 3 self
        return f"Nombre: {self.nombre} | Telefono: {self.telefono} | Correo: {self.correo}" #como self ordena datos




"""   def actualizar_telefono(self, TelefonoNuevo:str): # permite guardar int(str)
        self.telefono = TelefonoNuevo
"""