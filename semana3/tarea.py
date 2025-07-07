while True:
    try:

        cantidad_frutas = int(input("Ingrese la cantidad de frutas y verduras existentes: "))
        frutas_vendidas = int(input("Ingrese la cantidad de frutas y verduras vendidas durante el día: "))

        if cantidad_frutas < 0 or frutas_vendidas < 0:
            raise ValueError("Los valores ingresados no pueden ser negativos. Por favor, vuelva a ingresar un valor.")

        if frutas_vendidas > cantidad_frutas:
            raise ValueError("La cantidad de frutas y verduras vendidas no puede exceder la cantidad existente en inventario.")
        resultado = cantidad_frutas - frutas_vendidas
        break

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

print(f"La cantidad de frutas y verduras restantes disponibles es de {resultado}")
print("Gracias por usar el programa.")