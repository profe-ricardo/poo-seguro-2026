class Equipo():
    def __init__(self, tipo:str,marca:str,modelo:str,serie:str):
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.serie = serie

    def mostrar_datos(self):
        return f"tipo: {self.tipo} | marca: {self.marca} | modelo: {self.modelo} | serie: {self.serie}"