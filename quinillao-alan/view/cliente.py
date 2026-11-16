from model.cliente import Cliente

def registrar_usuario():
    """ Registra Usuario """

    print("Ingrese datos de la persona")
    nombre = str(input("- Nombre: "))
    telefono = str(input("- Telefono: "))
    correo = str(input("- Correo: "))
    clave = str(input("- Clave: "))

    usuario = Cliente(nombre, telefono, correo, clave)

    print("\n Usuario creado")
    
    return usuario

def inicio_sesion(s_correo: str, s_clave: str, usuario:Cliente):
    """ Valida inicio de sesion con usuario en memoria """

    if usuario:
        usuario_nombre = str(input(" Ingrese su usuario: "))
        usuario_clave = str(input(" Ingrese su contraseña: "))
    
        if (usuario.nombre == usuario_nombre and usuario.clave == usuario_clave):
            print("Inicio de sesion correcto")
        else:
            print("Credenciales incorrectas, intente nuevamente")