
def calcular_precio(producto, precio_base, impuesto):
    precio_total = precio_base * (1 + impuesto)
    print (f"El precio a pagar por {producto} es: ${precio_total:.2f}")
# Datos del producto y precio base
nombre_producto = "Computadora"
precio_producto = 800 # Precio base en dólares
impuesto_producto = 0.15 # Impuesto del 15%
# Llamada a la función con los argumentos respectivos
calcular_precio(nombre_producto, precio_producto, impuesto_producto)