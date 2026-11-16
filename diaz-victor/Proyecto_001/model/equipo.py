from Proyecto_001.view.cliente import Client
class Equipo():
    def __init__(self, tipo:str , marca:str, modelo:str, serie:str, diagnostico:str):
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.serie = serie
        self.diagnostico = diagnostico

    def mostrar_datos(self):
        return f"Equipo\n Tipo: {self.tipo} | Marca: {self.marca} | Modelo: {self.modelo} | Serie: {self.serie} | Diagnostico: {self.diagnostico}"

    def Actualizar_diagnostico(self, nuevo_diagnostico:str):
        if isinstance(nuevo_diagnostico, str):
            self.diagnostico = nuevo_diagnostico
        else:
            print("Diagnostico no es str")