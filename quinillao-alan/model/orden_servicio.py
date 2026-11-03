from .cliente import Cliente
from .equipo import Equipo

class OrdenServicio:
    def __init__(self, numero:int, descripcion:str, estado:str, diagnostico:str, cliente:Cliente, equipo:Equipo):
        self.numero = numero
        self.descripcion = descripcion
        self.estado = estado or "Recibido"
        self.diagnostico = diagnostico or ""
        self.cliente = cliente
        self.equipo = equipo

    def cambiar_estado(self, nuevo_estado:str):
        if isinstance(nuevo_estado, str):
            self.telefono=nuevo_estado
        else:
            print("Nuevo estado no corresponde a tipo str")

    def registrar_diagnostico (self, diagnostico:str):
        if isinstance(diagnostico, str):
            self.telefono=diagnostico
        else:
            print("Nuevo estado no corresponde a tipo str")

    def mostrar_resumen(self):
        return f"Orden N° {self.numero} | Cliente: {self.cliente.nombre} | Equipo: {self.equipo.tipo} {self.equipo.marca}"