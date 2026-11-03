from model.cliente import Client #busca el archivo.py clase Client
from model.equipo import Equipo
from model.OrdenServicio import OrdenServicio



persona_1 = Client('pedro', '9 1234 5678', 'pedro@gmail.com') #no se escribe desde la consola
print (persona_1.Mostrar_Datos())

equipo_1 = Equipo('telefono', 'xiaomi', 'redmi 14C', '56 9 1234 5678')
print (persona_1.mostrar_datos())

orden_1 = OrdenServicio('9 1234 5678', 'descripcion', 'mal estado', 'diagnostico', persona_1, equipo_1)
print (persona_1.Cambiar_Estado, persona_1.registrar_diagnostico())
