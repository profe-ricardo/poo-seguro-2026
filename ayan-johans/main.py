"""
    Reglas PEP8:
    - Clases -> inicial en mayús. palabra en min
    - Funciones -> todo en min y snake_case
"""
from model.cliente import Cliente
from model.equipo import Equipo
from model.orden_servicio import OrdenServicio

persona_1 = Cliente('Juan', '912345678', 'juan@nose.cl')
datos = persona_1.mostrar_datos()
print(datos)

persona_1.actualizar_telefono(987654321)
print(persona_1.mostrar_datos())

equipo_1 = Equipo('Celular', 'Xiaomi', 'Redmi 14C', '123456')
print(equipo_1.mostrar_datos())

orden_servicio1 = OrdenServicio(1, "Equipo no prende", "Recepcionado", "", persona_1, equipo_1)
print(orden_servicio1.mostrar_resumen())