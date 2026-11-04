from .cliente01 import Cliente
from .equipo01 import Equipo

class OrdenServicio():
    def __init__(self, numero: int, descripcion: str, estado: str, diagnostico: str, cliente: Cliente, equipo: Equipo):
        self.numero = numero
        self.descripcion = descripcion
        self.estado = estado or "Recibido"
        self.diagnostico = diagnostico or ""
        self.cliente = cliente
        self.equipo = equipo

    def cambiar_estado(self, nuevo_estado: str):
        if isinstance(nuevo_estado, str):
            self.nuevo_estado = nuevo_estado
        else:
            print("Nuevo estado no corresponde a tipo str")

    def registrar_diagnostico(self, diagnostico: str):
        if isinstance(diagnostico, str):
            self.diagnostico = diagnostico
        else:
            print("Diagnostico no corresponde a tipo str")

    def mostrar_resumen(self):
        return f"Orden de Servicio\n Numero: {self.numero} | Cliente: {self.cliente.nombre} | Equipo: {self.equipo.tipo} {self.equipo.marca}"