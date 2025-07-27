import io

with open ('MiArchivo.txt', "w") as archivo:
    archivo.write('hola, estoy agregando texot a un archivo\n')
    archivo.write("aqui agrego mas cositas")

with open ('MiArchivo.txt', "r") as archivo:
    contenido = archivo.read()
    print("contenido del archivo:")
    print(contenido)

with open ('MiArchivo.txt', 'a') as archivo:
    archivo.write("\nEsta es una nueva linea del documento.")

with open ('MiArchivo.txt', 'r') as archivo:
    contenido_actualizado = archivo.read()
    print("contenido actualidao del archivo: ")
    print(contenido_actualizado)