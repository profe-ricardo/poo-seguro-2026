print ("hola mundo")

from .cliente import cliente
from .equipo import equipo
from .orden_servicio import orden_servicio

print("---")
persona_1 = cliente('Pedro', '912345678', 'pedro@hola.com')
print(persona_1.mostrar_datos())
# persona_1.actualizar_telefono(987654321)

equipo_1 = equipo('Telefono', 'Xiaomi', 'Redmi 14c', '123456')
print(equipo_1.mostrar_datos())

orden_servicio_1 = orden_servicio(1, "Equipo no prende", "Recepcionado", "", persona_1, equipo_1)
print(orden_servicio_1.mostrar_resumen()) 