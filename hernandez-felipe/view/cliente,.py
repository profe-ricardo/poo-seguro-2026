from model.cliente import Cliente

def registrar_cliente():
    """Registrar usuario """
    nombre = str(input("Ingrese su nombre: "))
    telefono = str(input("Ingrese su telefono: "))
    correo = str(input("Ingrese su correo: "))
    clave = str(input("Ingrese su clave: "))

    usuario = Cliente(nombre, telefono, correo, clave)