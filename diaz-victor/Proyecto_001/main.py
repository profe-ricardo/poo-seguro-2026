from view.cliente import Client #busca el archivo.py clase Client
from model.equipo import Equipo
from model.OrdenServicio import OrdenServicio

#validadar datos cliente
#insertar datos cliente
def ValidarDatosCliente():
    nombre = input("ingresar nombre")
    telefono = input("ingresar telefono")
    correo = input ("ingresar correo")
    if not nombre or not telefono or not correo:
        print("Error: Todos los campos son obligatorios.")
        return None

    return Client(nombre, telefono, correo)

def InsertarDatosCliente():
    cliente = ValidarDatosCliente()
    if cliente:
        print("Datos Ingresados")
        print(cliente.Mostrar_Datos())
    else:
        print("No se puede inresar")