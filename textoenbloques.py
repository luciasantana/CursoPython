#EJERCICIO: División de texto en bloques

#Simular un texto de 1000 líneas
texto_largo = ["Línea " + str(i +1) for i in range(1000)]

#Lista para almacenar los bloques de 25 líneas
bloques = []

#Iterar a través de todas las líneas del texto
for linea in texto_largo:
    #Agregar la línea actual al bloque
    bloque_actual.append(línea)

    #Si el bloque tiene 25 líneas, almacenar en la lista de bloques
    if len(bloque_actual) == 25:
        bloques.append(bloque_actual)
        bloque_actual = [] #Reiniciar el bloque acutal

#Si quedan líneas sin almacenar al final, agregar el último bloque
if bloque_actual:
    bloques.append(bloque_actual)

#Mostrar el resultado
print (f"Se dividió el texto en {len(bloques)} bloques.")
print ("Primer bloque: ")
