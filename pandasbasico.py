#EJERCICIO

import pandas as pd

#Crear una serie de pandas a partir de una lista de números
numeros = [10, 20, 30, 40, 50]
serie = pd.Series(numeros)
print ("Serie original:")
print (serie)

#Mostrar la serie
print ("\nMostrar la serie:")
print (serie)

#Agregar un nuevo elemento a la Serie
nuevo_valor = 60
serie = serie.append(pd.series([nuevo_valor]), ignore_index=True)
print ("\nSerie después de agregar un nuevo elemento:")
print (serie)

#Quitar un elemento de la Serie
indice_eliminar = 2 #elemento en el segundo indice (tercer elemento)
serie = serie.drop(indice_eliminar).reset_index(drop=True)
print ("\nSerie después de eliminar un elemento:")
print (serie)

#Realizar operaciones aritmeticas básicas
suma = serie + 5
resta = serie - 5
multiplicacion = serie * 2
division = serie / 2

#Mostrar los resultados de cada operación 
print ("\nResultado de la Suma (+5):")
print (suma)

print ("\nResultado de la resta (-5):")
print (resta)

print ("\nResultado de la multiplicación (*2):")
print (multiplicacion)

print ("\nResultado de la división (/2):")
print (division)