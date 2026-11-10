from .cliente import Cliente
from .equipo import Equipo

class OrdenServicio ():
    def __init__(self, numero:int, descripcion: str, estado:str, diagnostico:str, cliente: Cliente, equipo: Equipo): 
        self.descripcion = descripcion
        self.estado = estado or "Recibido"
        self.diagnstico = diagnostico or ""
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