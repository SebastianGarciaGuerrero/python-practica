import math

try:
    numero = float(input("Ingrese un número para calcular su raíz cuadrada: "))

    if numero < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")

    resultado = math.sqrt(numero)

except ValueError as e:
    print(f"eRROR: {e}")
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Error inesperado: {e}")

else:
    print(f"La raiz cuadrada de {numero} es: {resultado:.2f}")

finally:
    print("Gracias por usar el programa.")