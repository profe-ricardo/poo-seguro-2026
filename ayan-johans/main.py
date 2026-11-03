print("HelloWorld")

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

#Implementación de la clase Cliente 
# class Cliente:
# #atributos
#     def __init__(self, nombre, correo, telefono):
#         self.nombre = nombre
#         self.correo = correo
#         self.telefono = telefono

# #metodos
#     def actualizar_telefono(self, nuevo_telefono):
#         self.telefono = nuevo_telefono

#     def mostrar_datos(self):
#         return(f'Cliente: {self.nombre} | Correo: {self.correo} | Telefono: {self.telefono}')

# #Implementación de OrdneServicio con referencia al cliente (primera versión)
# class OrdenServicio:
#     def __init__(self, numero, descripcion, cliente):
#         self.numero = numero
#         self.descripcion = descripcion
#         self.estado = 'recibida'
#         self.diagnostico = ''
#         self.cliente = cliente

#     def cambiar_estado(self, nuevo_estado):
#         self.estado = nuevo_estado

#     def mostrar_resumen(self):
#         return(f'Orden N° {self.numero} |'
#                f'Cliente: {self.cliente.nombre} |'
#                f'Estado: {self.estado}')

# #Clase Equipo y versión ampliada de OrdenServicio (version ampliada)
# class Equipo:
#     def __init__(self, tipo, marca, modelo, serie):
#         self.tipo = tipo
#         self.marca = marca
#         self.modelo = modelo
#         self.serie = serie

#     def mostrar_datos(self):
#         return(f'Equipo: {self.tipo} | Marca: {self.marca} | Modelo: {self.modelo}')

#     class OrdenServicio:
#         def __init__(self, numero, descripcion, cliente, equipo):
#             self.numero = numero
#             self.descripcion = descripcion
#             self.estado = 'recibida'
#             self.diagnostico = ''
#             self.cliente = cliente
#             self.equipo = equipo

#         def cambiar_estado(self, nuevo_estado):
#             self.estado = nuevo_estado

#         def registrar_diagnostico(self, diagnostico):
#             self.diagnostico = diagnostico

#         def mostrar_resumen(self):
#             return(f'Orden N° {self.numero} | '
#                    f'Cliente: {self.cliente.nombre} | '
#                    f'Equipo: {self.equipo.tipo} {self.equipo.marca} | '
#                    f'Estado: {self.estado}')