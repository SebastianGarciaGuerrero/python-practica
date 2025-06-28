cantidadClientes = int(input("¿Cuántos clientes son? "))

for cliente in range(1, cantidadClientes + 1):
    print(f"\nCliente #{cliente}")
    cantidadLlantas = int(input("Ingrese la cantidad de llantas que desea comprar: "))

    # Determinar el precio unitario según la cantidad
    if cantidadLlantas < 5:
        precioUnitario = 35000
    elif 5 <= cantidadLlantas <= 10:
        precioUnitario = 40000
    else:
        precioUnitario = 45000

    # Calcular el total
    total = cantidadLlantas * precioUnitario

    # Mostrar el resultado con toda la información
    print(f"Cliente #{cliente} compró {cantidadLlantas} llanta(s).")
    print(f"Precio por llanta: ${precioUnitario:,}")
    print(f"Total a pagar: ${total:,}")
