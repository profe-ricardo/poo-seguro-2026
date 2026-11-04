print("Hola Mundo")


from model.cliente import Cliente

persona_1 = Cliente('Pedro', '91214323', 'pedro@gmail.com')
datos = persona_1.mostrar_datos()

print(datos)
