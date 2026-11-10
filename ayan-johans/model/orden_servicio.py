# Guardar orden de servicio en DB
# Registrar cambio de estado en DB
# Registrar diagnostico en DB

from model.cliente import Cliente
from model.equipo import Equipo

class OrdenServicio:
    def __init__(self, numero: int, descripcion: str, estado: str, diagnostico: str, cliente: Cliente, equipo: Equipo):
        self.numero = numero
        self.descripcion = descripcion
        self.estado = estado or 'recibida'
        self.diagnostico = diagnostico or ''
        self.cliente = cliente
        self.equipo = equipo

    def cambiar_estado(self, nuevo_estado: str):
        if isinstance(nuevo_estado, str):
            self.estado = nuevo_estado
        else:
            print("Tipo de dato no valido")

    def registrar_diagnostico(self, diagnostico):
        if isinstance(diagnostico, str):
            self.estado = diagnostico
        else:
            print("Tipo de dato no valido")

    def mostrar_resumen(self):
        return f'Orden N° {self.numero} | Cliente: {self.cliente.nombre} | Equipo: {self.equipo.tipo} {self.equipo.marca} | Estado: {self.estado}'