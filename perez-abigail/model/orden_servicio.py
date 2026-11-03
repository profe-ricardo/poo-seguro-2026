from model.cliente import Cliente
from model.equipo import Equipo

class OrdenServicio():
    def __init__(self, numero: int, descripcion: str, estado: str, diagnostico: str, cliente: Cliente, equipo: Equipo):
        self.numero = numero
        self.descripcion = descripcion
        self.estado = estado or "recibida"
        self.diagnostico = diagnostico or ""
        self.cliente = cliente
        self.equipo = equipo

    def cambiar_estado(self, nuevo_estado: str):
        if isinstance(nuevo_estado, str):
            self.estado = nuevo_estado
        else:
            print("Estado no corresponde a tipo String")

    def registrar_diagnostico(self, diagnostico: str):
        if isinstance(diagnostico, str):
            self.diagnostico = diagnostico
        else:
            print("Diagnostico no corresponde a tipo String")

    def mostrar_resumen(self):
          return f"Orden N°{self.numero} | Cliente: {self.cliente.nombre} | Equipo: {self.equipo.tipo} {self.equipo.marca} | Estado: {self.estado}"