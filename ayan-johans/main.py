"""
    Reglas PEP8:
    - Clases -> inicial en mayús. palabra en min
    - Funciones -> todo en min y snake_case
"""
from model.cliente import Cliente
from model.equipo import Equipo
from model.orden_servicio import OrdenServicio

# print("Cargando...")
# persona_1 = Cliente("Juan Perez", "juan@correo.cl", "123456789")
# print(persona_1.mostrar_datos())

# print("Cargando...")
# equipo_1 = Equipo('Notebook', 'Lenovo', 'IdeaPad 3', '123456789')
# print(equipo_1.mostrar_datos())

persona_2 = Cliente("Maria Lopez", "maria@correo.cl", "987654321")
equipo_2 = Equipo('Tablet', 'Samsung', 'Galaxy Tab S7', '987654321')

orden_1 = OrdenServicio(1001, 'No enciende la pantalla', '', '', persona_2, equipo_2)
print(orden_1.mostrar_resumen())

# orden_1.cambiar_estado('en revisión')