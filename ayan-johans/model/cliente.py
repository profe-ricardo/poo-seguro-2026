class Cliente:
#atributos
    def __init__(self, nombre: str, correo: str, telefono: str):
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

#metodos
    def actualizar_telefono(self, nuevo_telefono: str):
        if isinstance(nuevo_telefono, str):
#isinstance: recibe un dato
            self.telefono = nuevo_telefono
        else:
            print("Telefono no corresponde al tipo requerido (str) :(")

    def mostrar_datos(self):
        return f'Cliente: {self.nombre} | Correo: {self.correo} | Telefono: {self.telefono}'