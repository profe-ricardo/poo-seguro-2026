from model.cliente import Cliente

def registrar_usuario():
    """ Registra usuario """
    print(" Ingrese datos de la persona")
    nombre = str(input(" - Nombre: "))
    telefono = str(input(" - Teléfono: "))
    correo = str(input(" - Correo: "))

    # persona_1 = Cliente(nombre, telefono, correo)