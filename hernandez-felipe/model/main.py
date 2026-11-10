"""
    Reglas PEP8:
    - clases -> inicial en mayúscula, palabra en minúscula
    - funciones -> todo en minúscula y en snake_case
"""

from model.cliente import Cliente, cliente
# from model.equipo import Equipo
# from model.orden_servicio import OrdenServicio

print("---")
persona_1 = Cliente('Pedro', '912345678', 'pedro@hola.com')
persona_2 = actualizar_telefono(persona_1, '987654321')
# print(persona_1.mostrar_datos())
# persona_1.actualizar_telefono(987654321)

# equipo_1 = Equipo('Telefono', 'Xiaomi', 'Redmi 14c', '123456')
# print(equipo_1.mostrar_datos())

# orden_servicio_1 = OrdenServicio(1, "Equipo no prende", "Recepcionado", "", persona_1, equipo_1)
# print(orden_servicio_1.mostrar_resumen())