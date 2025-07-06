def dividir(a,b):
    if b == 0:
        raise ValueError("No se puede dividir un número por 0.")

    return a/b

try:
    resultado = dividir(10, 0)
except ValueError as e:
    print(f"Error: {e}")