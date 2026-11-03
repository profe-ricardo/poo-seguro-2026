from model.cliente import Cliente
from model.equipo import Equipo
from model.orden_servicio import OrdenServicio

print("-------------------------------------------")
#Instancia de Cliente, puesta de sus datos a consola
persona_1 = Cliente("Pedro", "943218765", "pedro@email.net")
datos = persona_1.mostrar_datos()
print(datos)

print("-------------------------------------------")
#Prueba de validacion de tipo de dato
persona_1.actualizar_telefono(912345678)
datos = persona_1.mostrar_datos()
print(datos)

print("-------------------------------------------")
#Prueba de metodo actualizacion
persona_1.actualizar_telefono("912345678")
datos = persona_1.mostrar_datos()
print(datos)

print("-------------------------------------------")
#Instancia de Equipo, puesta de sus datos a consola
equipo_1 = Equipo("Telefono", "Xiaomi", "Redmi 13C", "2597")
print(equipo_1.mostrar_datos())

print("-------------------------------------------")
#Instancia de OrdenServicio, prueba de metodo print en datos
orden_1 = OrdenServicio(21, "Ta malo", None, None, persona_1, equipo_1)
print(orden_1.mostrar_resumen)