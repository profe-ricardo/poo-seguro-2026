# # print("Hola mundo")
# """
# Reglas PEP8:
#     clases -> inicial en mayuscula, palabra en minuscula
#     funciones -> todo en minuscula y en camel_case 
#     (el cual escribio como snake_case asyfduiasfduiafsdu, 
#     camelCase es este)
# """
# from model.cliente import Cliente
# # from model.equipo import Equipo
# # from model.orden_servicio import OrdenServicio



from view.menus import menu_principal

def main():

    validador= True
    usuario=None
    sesion=None

    while validador and not sesion:
        validador, usuario, sesion = menu_principal(validador, usuario, sesion)

    while sesion:
        print("\n Sesion iniciada con usuario {usuario.nombre}")

        opcion = str(input("\n ¿desea cerrar sesion? (SI|NO) "))

        if opcion == "SI":
            print(" bai bai ")
            sesion=None


# persona1 = Cliente ('Pepe', '676767676767', 'pepe@hola.xd')
# # datos = persona1.mostrar_datos()
# # print(datos)

# # from model.cliente import Cliente
# from model.equipo import Equipo
# # from model.orden_servicio import OrdenServicio
# # print("Cargando...")
# # persona_1 = Cliente('Juan', '912345678', 'juan@nose.cl')
# # datos = persona_1.mostrar_datos()
# # print(datos)

# # print("Cargando...")
# # equipo_1 = Equipo('Notebook', 'Lenovo', 'IdeaPad 3', '123456789')
# # print(equipo_1.mostrar_datos())

if __name__ == "__main__":
    main()