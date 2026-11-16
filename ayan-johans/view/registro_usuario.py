from model.cliente import Cliente

def registrar_usuario():
    """Registrar Usuario"""
    print("Ingrese datos del cliente: ")
    nombre = input("- Nombre: ")
    telefono = input("- Telefono: ")
    correo = input("- Correo: ")
    clave = input("- Clave: ")

    usuario = Cliente(nombre, telefono, correo, clave)
    print("\n Usuario creado!")
    return usuario

def inicio_sesion(usuario: Cliente):
    """Valida inicio de sesión con usuario"""
    usuario_correo = input(" Ingrese su correo: ")
    usuario_clave = input(" Ingrese su contraseña: ")
    
    if (usuario.correo) == usuario_correo and (usuario.clave) == usuario_clave:
        print(" Inicio de sesión valido. Bienvenido!")
    else:
        print(" Credenciales incorrectas. Intente nuevamente")