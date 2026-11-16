class Equipo():
    def __init__(self, tipo:str , marca:str, modelo:str, serie:str, diagnostico:str):
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.serie = serie
        self.diagnostico = diagnostico
    def Actualizar_diagnostico(self, nuevo_diagnostico:str):