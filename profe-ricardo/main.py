"""
    Reglas PEP8:
    - clases -> inicial en mayúscula, palabra en minúscula
    - funciones -> todo en minúscula y en snake_case
"""

from view.cliente import registrar_usuario

def main():
    validador = True

    while validador:
        print(" Seleccione una opción:")
        opcion = str(input(
            "\n 1 : Iniciar sesión" +
            "\n 2 : Terminar programa" +
            "\n 3 : Registrar usuario" +
            "\n\n Opción : "
        ))

        print("\n")
        print("=====" * 6)

        if opcion not in ("1", "2", "3"):
            print(" Opción no válida, intente nuevamente.")
        else:
            if opcion == "1":
                print(" Inicio de sesión no habilitado.")

            if opcion == "2":
                print(" Que le vaya bien.")
                validador = False

            if opcion == "3":
                print(" Comienza registro de usuario")
                registrar_usuario()

if __name__ == "__main__":
    main()
