import math

# Función para calcular el descuento en compras de licencias
def calcular_descuento_licencias():
    precio_base = 50  # Precio fijo por licencia

    try:
        cantidad = int(input("Ingrese la cantidad de licencias que desea comprar: "))

        if cantidad >= 5:
            descuento = 0.30
        elif cantidad >= 3:
            descuento = 0.20
        else:
            descuento = 0.0

        total_sin_descuento = cantidad * precio_base
        monto_descuento = total_sin_descuento * descuento
        total_final = total_sin_descuento - monto_descuento

        print(f"\nCantidad de licencias: {cantidad}")
        print(f"Descuento aplicado: {int(descuento * 100)}%")
        print(f"Total a pagar: ${total_final:.2f}")

    except ValueError:
        print("Por favor, ingrese un número entero válido.")

# Función para calcular el volumen de una esfera
def calcular_volumen_esfera():
    try:
        radio = float(input("Ingrese el radio de la esfera: "))
        pi = 3.1416
        volumen = (4/3) * pi * (radio ** 3)
        print(f"\nEl volumen de la esfera es: {volumen:.2f}")
    except ValueError:
        print("Por favor, ingrese un valor numérico válido.")

# Menú principal
while True:
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Calcular descuento en compras de software")
    print("2. Calcular el volumen de una esfera")
    print("3. Salir")

    opcion = input("Seleccione una opción (1, 2 o 3): ")

    if opcion == '1':
        calcular_descuento_licencias()
    elif opcion == '2':
        calcular_volumen_esfera()
    elif opcion == '3':
        print("¡Gracias por usar el programa! Hasta luego.")
        break
    else:
        print("⚠️ Opción no válida. Por favor, seleccione 1, 2 o 3.")
