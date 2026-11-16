"""
    Reglas PEP8:
    - Clases -> inicial en mayús. palabra en min
    - Funciones -> todo en min y snake_case
"""

from view.menus import menu_principal
# from model.equipo import Equipo
# from model.orden_servicio import OrdenServicio

def main():
    validador = True
    usuario = None
    sesion = None

    while validador and not sesion:
        validador, usuario, sesion = menu_principal(validador, usuario, sesion)

    while sesion:
        print("\n Sesión iniciada con usuario {usuario.nombre}")
        opcion = input(" ¿Desea cerrar sesión?: (SI | NO) ")

        if opcion == "SI":
            print(" Que tenga un bonito día")
            sesion = None

if __name__ == "__main__":
    main()

# print("Cargando...")
# persona_1 = Cliente("Juan Perez", "juan@correo.cl", "123456789")
# print(persona_1.mostrar_datos())

# print("Cargando...")
# equipo_1 = Equipo('Notebook', 'Lenovo', 'IdeaPad 3', '123456789')
# print(equipo_1.mostrar_datos())

# persona_2 = Cliente("Maria Lopez", "maria@correo.cl", "987654321")
# equipo_2 = Equipo('Tablet', 'Samsung', 'Galaxy Tab S7', '987654321')

# orden_1 = OrdenServicio(1001, 'No enciende la pantalla', '', '', persona_2, equipo_2)
# print(orden_1.mostrar_resumen())

# orden_1.cambiar_estado('en revisión')