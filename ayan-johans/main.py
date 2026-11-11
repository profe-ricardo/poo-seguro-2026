"""
    Reglas PEP8:
    - Clases -> inicial en mayús. palabra en min
    - Funciones -> todo en min y snake_case
"""
# from model.cliente import Cliente
from model.equipo import Equipo
# from model.orden_servicio import OrdenServicio
# print("Cargando...")
# persona_1 = Cliente('Juan', '912345678', 'juan@nose.cl')
# datos = persona_1.mostrar_datos()
# print(datos)

# print("Cargando...")
# equipo_1 = Equipo('Notebook', 'Lenovo', 'IdeaPad 3', '123456789')
# print(equipo_1.mostrar_datos())

# 1. Prueba de creación e inserción en Oracle
equipo_1 = Equipo("Notebook", "Lenovo", "IdeaPad Slim 3", "SN-2026-001")
print(equipo_1.mostrar_datos())

# 2. Prueba de restricción UNIQUE (debería lanzar el [WARNING] de serie duplicada)
# equipo_repetido = Equipo("Notebook", "Lenovo", "IdeaPad Slim 3", "SN-2026-001")
# print(equipo_repetido.mostrar_datos())
