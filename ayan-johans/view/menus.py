from .registro_usuario import registrar_usuario, inicio_sesion

def menu_principal(validador, usuario, sesion):
    print("=====" * 6)
    print("\n Seleccione una opción:")

    opcion = str(input(
        "\n 1 : Iniciar sesión" +
        "\n 2 : Registrar usuario" +
        "\n 3 : Terminar programa" +
        "\n\n Opción : "
    ))

    if opcion not in ("1", "2", "3"):
        print(" Opción no válida, intente nuevamente.")
    else:
        if opcion == "1":
            if usuario:
                sesion = inicio_sesion(usuario)
            else:
                print("\n Usuario no registrado, intente nuevamente.")

        if opcion == "3":
            print(" Que le vaya bien.")
            validador = False
            sesion = False

        if opcion == "2":
            usuario = registrar_usuario()

    return validador, usuario, sesion

def menu_usuario(sesion):
    """"""