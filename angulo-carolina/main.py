'''print ("Hola mundo")'''

'''class Cliente:
  def __init__(self, nombre, correo, telefono):
    self.nombre = nombre
    self.correo = correo
    self.telefono = telefono
    
  def actualizar_telefono(self, nuevo_telefono):
    self.telefono = nuevo_telefono
  
  def mostrar_datos(self):
   return f'Cliente: {self.nombre} | Correo: {self.correo} | Teléfono: {self.telefono}'''

class OrdenServicio:
   def __init__(self, numero, descripcion, cliente):
     self.numero = numero
     self.descripcion = descripcion
     self.estado = 'recibida'
     self.diagnostico = ''
     self.cliente = cliente
 
   def cambiar_estado(self, nuevo_estado):
     self.estado = nuevo_estado
 
   def mostrar_resumen(self):
     return (f'Orden N° {self.numero} | '
             f'Cliente: {self.cliente.nombre} | '
             f'Estado: {self.estado}')