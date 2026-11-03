from model.OrdenServicio import cliente
from equipo import Equipo

class OrdenServicio():
    def __init__(self, numero:str, descripcion:str, estado:str, diagnostico:str, equipo:str): # guarda todos los datos iniciales
        self.numero = numero 
        self.descripcion = descripcion
        self.estado = estado 
        self.diagnostico = diagnostico
        self.cliente = cliente
        self.equipo = equipo
        self.ID = ""    #se puede guardar dato en blanco para guardar 

    def Cambiar_Estado(self, nuevo_estado): #se guarda asi mismo y nuevo estado
        if isinstance(nuevo_estado,str):
            self.telefono = nuevo_estado
        else:
            print("Nuevo estado no es str")

    def registrar_diagnostico(self, actualizar_diagnostico: str): #guarda un nuevo diagnostico al inicial
        if isinstance(actualizar_diagnostico, str):
            self.diagnostico = actualizar_diagnostico
            print("")
        else:
            print('Diagnostico no es str')

        return f" Numero: {self.numero} | Cliente: {self.cliente.nombre} | Equipo{self.equipo.tipo}" #retorna los datos 
"""
    def Resumen_resumen (self):
        return f ""
"""