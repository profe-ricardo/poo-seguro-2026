class Equipo():
    def __init__(self, tipo: str, marca: str, modelo: str, serie: str):
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.serie = serie

    def mostrar_datos(self):
        return f"Tipo: {self.tipo} | Marca: {self.marca} | Modelo: {self.modelo} | Serie: {self.serie}"