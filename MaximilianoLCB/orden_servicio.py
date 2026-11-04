from .cliente import cliente
from .equipo import equipo

class OrdenServicio ():
    def __init__(self, numero:int, descripcion: str, estado:str, diagnostico:str, cliente: cliente, equipo: equipo): 
        self.descripcion = descripcion
        self.estado = estado 
        self.diagnstico = diagnostico
        self.cliente = cliente
        self.equipo = equipo

    def Cambiar_estado(self, nuevo_estado: str):
            if isinstance(nuevo_estado, str):
             self.nuevo_estado = nuevo_estado
            else: 
               print("Nuevo estado no corresponde a str")

    def Registrar_diagnostico(self, diagnostico: str):
            if isinstance(diagnostico, str):
             self.diagnostico = diagnostico
            else: 
               print("Diagnostico no corresponde a str")

    def mostrar_resumen(self):
        return f"orden de servicio\n numero: {self.numero} | cliente: {self.cliente.nombre} | equipo: {self.equipo.tipo} {self.equipo.marca}"