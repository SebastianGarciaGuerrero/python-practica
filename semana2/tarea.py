# Precio base por cada licencia
precio_base = 50

# Solicitar cantidad de licencias
cantidad_licencias = int(input("Ingrese la cantidad de licencias que desea comprar: "))

# Determinar el porcentaje de descuento
if cantidad_licencias >= 5:
    descuento = 0.30  # 30% de descuento
elif cantidad_licencias >= 3:
    descuento = 0.20  # 20% de descuento
else:
    descuento = 0.0   # Sin descuento

# Calcular el total a pagar
precio_sin_descuento = cantidad_licencias * precio_base
monto_descuento = precio_sin_descuento * descuento
precio_final = precio_sin_descuento - monto_descuento

# Mostrar resultados
print(f"\nResumen de compra:")
print(f"Cantidad de licencias: {cantidad_licencias}")
print(f"Descuento aplicado: {int(descuento * 100)}%")
print(f"Total a pagar: ${precio_final:.2f}")
