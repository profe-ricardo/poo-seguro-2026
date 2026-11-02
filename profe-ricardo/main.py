"""
    Reglas PEP8:
    - clases -> inicial en mayúscula, palabra en minúscula
    - funciones -> todo en minúscula y en camel_case
"""

from model.cliente import Cliente

persona_1 = Cliente('Pedro', '912345678', 'pedro@hola.com')

print(persona_1.mostrar_datos())