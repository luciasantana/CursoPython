#EJERCICIO 1

import os

#Abrir archivo modo lectura
try:
    with open ("mi_archivo.txt", "r") as archivo:
        print ("El archivo ya existe. No se puede continuar.")
except FileNotFoundError:
    print ("El archivo no existe. Creando un nuevo archivo...")
    with open ("mi_archivo.txt", "w") as archivo:
        archivo.writelines([
            "Primera línea de texto\n",
            "Segunda línea de texto\n"
            "Tercera línea de texto\n"
            "Cuarta línea de texto\n"
            "Quinta línea de texto\n"
        ])
    print ("Archivo creado con contenido inicial.")

#Abrir archivo en modo lectura y leer las líneas
print ("\nLeyendo el contenido del archivo línea por línea:")
with open ("mi_archivo.txt", "r") as archivo:
    for linea in archivo:
        print (linea.strip()) #Elimina espacios en blanco y saltos de línea

#Usar tell() para obtener la posición del cursor después de leer cada línea
print ("\nMostrando posición del cursor con tell():")
with open("mi_archivo.txt", "r") as archivo:
    while linea := archivo.readline():
        print (f"Línea: {linea.strip()} - Posición del cursor: {archivo.tell()}")

#Sobreescribir el archivo
print ("\nSobreescribiendo el archivo con una nueva línea:")
with open("mi_archivo.txt", "w") as archivo:
    archivo.write("Esta es una nueva línea que sobreescribe todo el contenido anterior.\n")
print ("Archivo sobreescrito.")

#Añadir al archivo usando 'a+'
print ("\nAñadiendo una línea al final del archivo y leyendo todo el contenido:")
with open ("mi_archivo.txt", "a+") as archivo:
    archivo.write("Esta línea se añadió al final.\n")
    archivo.seek(0) #Volver al inicio del archivo
    contenido = archivo.read()
    print ("Contenido completo después de añadir una línea:")
    print (contenido)

#Cambiar el modo de apertura de 'a+' a 'a'
print ("|nIntentando con modo 'a':")
with open ("mi_archivo.txt", "a") as archivo:
    archivo.write("Otra línea añadida al final.\n")
    try: 
        archivo.seek(0)
        contenido = archivo.read() #Genera un error ya que 'a' no permite leer
    except UnsupportedOperation as e:
        print (f"Error al intentar leer en modo 'a': {e}")