"""
    Reglas PEP8:
    - clases -> inicial en mayúscula, palabra en minúscula
    - funciones -> todo en minúscula y en snake_case
"""

from view.menus import menu_principal

def main():
    validador = True
    usuario = None
    sesion = None

    while validador and not sesion:
        validador, usuario, sesion = menu_principal(validador, usuario, sesion)

    while sesion:
        print(f"\n Sesión iniciada con usuario {usuario.nombre}")

        opcion = str(input("\n ¿Desea cerrar sesión? (Si | No) "))

        if opcion == "Si":
            print("\n Que tenga un buen día.")
            sesion = None

if __name__ == "__main__":
    main()