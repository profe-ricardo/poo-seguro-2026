# Clase Equipo y versión ampliada de OrdenServicio (version ampliada)

class Equipo:
    def __init__(self, tipo: str, marca: str, modelo: str, serie: str):
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.serie = serie

    def mostrar_datos(self):
        return f'Equipo: {self.tipo} | Marca: {self.marca} | Modelo: {self.modelo}'
