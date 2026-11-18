from model.cliente01 import Cliente

def registrar_usuario():
    """ Registrar Usuario """
    print ("\n Ingrese datos de la persona")
    nombre   = str(input(" - Nombre   : "))
    telefono = str(input(" - Telefono : "))
    correo   = str(input(" - Correo   : "))
    clave    = str(input(" - Clave    : "))
    
    usuario = Cliente(nombre,telefono,correo,clave)
    
    print("\n Usuario creado")
    return usuario 