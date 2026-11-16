"""
    Reglas PEP8:
    - clases -> inicial en mayúscula, palabra en minúscula
    - funciones -> todo en minúscula y en snake_case
"""

from view.cliente import registrar_usuario

def main():
    validador = True
    usuario = None

    while validador:
        print("=====" * 6)
        print("\n Seleccione una opción:")

        opcion = str(input(
            "\n 1 : Iniciar sesión" +
            "\n 2 : Terminar programa" +
            "\n 3 : Registrar usuario" +
            "\n\n Opción : "
        ))

        if opcion not in ("1", "2", "3"):
            print(" Opción no válida, intente nuevamente.")
        else:
            if opcion == "1":
                if usuario:
                    usuario_nombre = str(input("  Ingrese su usuario    : "))
                    usuario_clave  = str(input("  Ingrese su contraseña : "))

                    if (usuario.nombre == usuario_nombre and usuario.clave == usuario_clave):
                        print("\n Inicio de sesión correcto.")
                    else:
                        print("\n Credenciales incorrectas, intente nuevamente.")
                else:
                    print("\n Usuario no registrado, intente nuevamente.")

            if opcion == "2":
                print(" Que le vaya bien.")
                validador = False

            if opcion == "3":
                usuario = registrar_usuario()

if __name__ == "__main__":
    main()
