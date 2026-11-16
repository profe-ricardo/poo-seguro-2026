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

def inicio_sesion(usuario: Cliente):
    """ Valida inicio de sesión con usuario en memoria """
    usuario_correo = str(input("  Ingrese su correo     : "))
    usuario_clave  = str(input("  Ingrese su contraseña : "))

    if (usuario.correo == usuario_correo and usuario.clave == usuario_clave):
        print(f"\n Inicio de sesión correcto, bienvenid@ {usuario.nombre}.")
        return True
    else:
        print("\n Credenciales incorrectas, intente nuevamente.")
        return False