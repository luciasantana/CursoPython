#EJERCICIO 1

#Crear una tupla
mi_tupla = (1, 2, 3)

#Intentamos modificar su contenido usando try-except
try:
    mi_tupla[0] = 10 
except TypeError as e:
    print (f"Error: {e}")
#Resultado: Imprime un mensaje de error indicando que las tuplas no se pueden modificar

#EJERCICIO 2
#Crear una tupla mixta 
tupla_mixta = (1, "dos", [3, 4], {5: "cinco"}, (6, 7), 8.0, True, None, {9})

#Imprimir la tupla 
print ("Tupla mixta:", tupla_mixta)

#Intentar modificar el tercer elemento de la tupla
try:
    tupla_mixta[2][0] = 99
    print ("Tupla mixta modificada: ", tupla_mixta)
except TypeError as e:
    print (f"Error: {e}")
#Resultado: En este caso modifica el contenido de la lista dentro de la tupla, porquelas listas se pueden modificar

#EJERCICIO 3
#Imprimir los elementos y tipos de tupla con bucle
for elemento in tupla_mixta:
    print (f"{elemento} => {type(elemento)}")

#EJERCICIO 4
#Convertir la tupla mixta en una lista
lista_mixta = list(tupla_mixta)
print ("Lista mixta: ", lista_mixta)

#Modificar elementos de la lista
lista_mixta[1] = "DOS"
lista_mixta[3] = {10: "diez"}
lista_mixta[5] = 42

#Covertir de nuevo en tupla
tupla_modificada = tuple(lista_mixta)
print ("Tupla modificada: ", tupla_modificada)

#EJERCICIO 5
#Crear una tupla númerica
tupla_numerica = (10, 20, 30, 40)

#Operaciones
print ("Suma: ", sum(tupla_numerica))
print ("Máximo: ", max(tupla_numerica))
print ("Mínimo: ", min(tupla_numerica))

#Calcular el cuadrado de cada elemento 
cuadrados = tuple(x ** 2 for x in tupla_numerica)
print ("Cuadrados: ", cuadrados)

#Desempaquetar la tupla
a, b, c, d = tupla_numerica
print ("Valores desempaquetados: ", a, b, c, d)