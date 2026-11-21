from model.cliente import Cliente, iniciar_sesion

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

def inicio_sesion():
    """ Valida inicio de sesión con usuario en memoria """
    usuario_correo = str(input("  Ingrese su correo     : "))
    usuario_clave  = str(input("  Ingrese su contraseña : "))

    return iniciar_sesion(usuario_correo, usuario_clave)