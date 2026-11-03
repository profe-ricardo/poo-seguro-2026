# print("Hola mundo")


"""
Reglas PEP8:
    clases -> inicial en mayuscula, palabra en minuscula
    funciones -> todo en minuscula y en camel_case 
    (el cual escribio como snake_case asyfduiasfduiafsdu, 
    camelCase es este)
"""

from model.cliente import Cliente
from model.equipo import Equipo
from model.orden_servicio import OrdenServicio


persona1 = Cliente ('Pepe', '676767676767', 'pepe@hola.xd')
datos = persona1.mostrar_datos()

print(datos)

persona1.actualizar_telefono(767676767676)
datos = persona1.mostrar_datos()

print(datos)

equipo_1 = Equipo('Telefono', 'Xiaomi', 'Redmi 14c', '67')
print(equipo_1.mostrar_datos())

orden_servicio_1 = OrdenServicio(1, "Equipo no prende", "Recepcionado", "", persona1, equipo_1)
print(orden_servicio_1.mostrar_resumen())