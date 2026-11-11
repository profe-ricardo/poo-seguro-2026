"""
    Reglas PEP8:
    - clases -> inicial en mayúscula, palabra en minúscula
    - funciones -> todo en minúscula y en snake_case
"""

from model.cliente import Cliente
from model.equipo import Equipo
from model.orden_servicio import OrdenServicio

print("---")
print("Ingrese datos de la persona")
nombre = str(input(" - Nombre: "))
telefono = str(input(" - Teléfono: "))
correo = str(input(" - Correo: "))

persona_1 = Cliente(nombre, telefono, correo)
persona_1.actualizar_telefono('987')

print(persona_1.mostrar_datos())
persona_1.actualizar_telefono(987654321)

equipo_1 = Equipo('Telefono', 'Xiaomi', 'Redmi 14c', '123456')
print(equipo_1.mostrar_datos()) 

orden_servicio_1 = OrdenServicio(1, "Equipo no prende", "Recepcionado", "", persona_1, equipo_1)
orden_servicio_1.cambiar_estado("En revisión")
orden_servicio_1.registrar_diagnostico("Batería dañada")
print(orden_servicio_1.mostrar_resumen())