from model.cliente import Cliente
from model.equipo import Equipo
from model.orden_servicio import OrdenServicio

print("=" * 50)
print("  SISTEMA DE ÓRDENES DE SERVICIO")
print("=" * 50)

# ----- Cliente -----
print("\n[1] Datos del Cliente")
nombre = input("  Nombre: ").strip()
telefono = input("  Teléfono: ").strip()
correo = input("  Correo: ").strip()
cliente = Cliente(nombre, telefono, correo)

# ----- Equipo -----
print("\n[2] Datos del Equipo")
tipo = input("  Tipo (Teléfono, Notebook, etc.): ").strip()
marca = input("  Marca: ").strip()
modelo = input("  Modelo: ").strip()
serie = input("  Número de serie: ").strip()
equipo = Equipo(tipo, marca, modelo, serie)

# ----- Orden de Servicio -----
print("\n[3] Datos de la Orden")
numero = int(input("  Número de orden: "))
descripcion = input("  Descripción del problema: ").strip()

orden = OrdenServicio(
    numero=numero,
    descripcion=descripcion,
    cliente=cliente,
    equipo=equipo
)

print("\n" + "=" * 50)
print(orden.mostrar_resumen())
print("=" * 50)

# Ejemplos de uso (descomenta para probar)
# orden.cambiar_estado("En diagnóstico")
# orden.registrar_diagnostico("Pantalla dañada, se recomienda cambio")
# print("\n--- Después de actualizar ---")
# print(orden.mostrar_resumen())
