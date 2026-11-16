from .cliente import registrar_usuario, inicio_sesion

def menu_principal(validador, usuario, sesion):
    
    print("\n Seleccione una opcion")
    opcion=str(input(
        "\n 1. Iniciar sesión"+
        "\n 2. Registrar usuario"+
        "\n 3. Terminar programa"+
        "\n\n Opcion:"
    ))
    
            
    if opcion not in ("1","2","3"):
        print("\n Opcion no valida, intente nuevamente")
    else:
        if opcion == "1":
            if usuario:
                sesion = inicio_sesion(usuario)
            else:
                print("Usuario no registrado, intente nuevamente")
    
        if opcion == "2":
            print("\n")
            print("==========" * 6)
            print("\n")
            print("Comienza registro usuario...")
    
            usuario=registrar_usuario()
    
        if opcion == "3":
            print("\n Que le vaya bien!")
            validador=False