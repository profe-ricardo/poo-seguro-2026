"""
    Reglas PEP8:
    - clases -> inicial en mayúscula, palabra en minúscula
    - funciones -> todo en minúscula y en snake_case
"""

from model.cliente import Cliente
from model.equipo import Equipo
from model.orden_servicio import OrdenServicio

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
                if usuario: 
                    usuario_nombre = str(input(" Ingrese su usuario    : " ))
                    usuario_clave  = str(input(" Ingrese su contraseña : " ))
                    
                    if (usuario.nombre == usuario_nombre and usuario.clave == usuario_clave):
                        print("\n Inicio de sesion correcto ")
                    else:
                        print("\n Credenciales Incorrectas, intentelo nuevamente ")
                else:            
                    print(" Inicio de sesión no habilitado.")

            if opcion == "2":
                print(" Que le vaya bien.")
                validador = False

            if opcion == "3":
                print(" Comienza registro de usuario")
                registrar_usuario()

if __name__ == "__main__":
    main()


#print("---")
#persona_1 = Cliente('Pedro', '912345678', 'pedro@hola.com')
#print(persona_1.mostrar_datos())
# persona_1.actualizar_telefono(987654321)

#equipo_1 = Equipo('Telefono', 'Xiaomi', 'Redmi 14c', '123456')
#print(equipo_1.mostrar_datos())

#orden_servicio_1 = OrdenServicio(1, "Equipo no prende", "Recepcionado", "", persona_1, equipo_1)
#print(orden_servicio_1.mostrar_resumen())