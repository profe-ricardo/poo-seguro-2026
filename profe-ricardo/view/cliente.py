from model.cliente import Cliente

def registrar_usuario():
    """ Registra usuario """
    print("\n Ingrese datos de la persona")
    nombre   = str(input(" - Nombre   : "))
    telefono = str(input(" - Teléfono : "))
    correo   = str(input(" - Correo   : "))
    clave    = str(input(" - Clave    : "))

    usuario = Cliente(nombre, telefono, correo, clave)

    print("\n Usuario creado")
    return usuario