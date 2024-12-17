#EJERCICIO 2

import pandas as pd

#Crear dos series de pandas a partir de listas de datos
#Serie A: Temperaturas semanales (con grados Celsius)
temperaturas = pd.series[5, 3, 0, 7, 8, 12, 15]
temperaturas = pd.Series(temperaturas, index = [
    "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sabado", "Domingo"])

#Serie B: Precipitaciones semanales (en milímetros)
precipitaciones = [5, 3, 0, 0, 7, 10, 12]
precipitaciones = pd.Series(precipitaciones, indx = [
    "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sabado", "Domingo"])

#Mostrar las series originales
print ("Temperaturas semanales:")
print (temperaturas)

print ("\nPrecipitaciones semanales:")
print (precipitaciones)

#Realizar operaciones de slicing
slicing_temperaturas = temperaturas[1:5]
slicing_precipitaciones = precipitaciones[2:6]

print ("\nSlicing de Serie temperaturas (Martes a viernes):")
print (slicing_temperaturas)

print ("\nSlicing de serie precipitaciones (Miercoles a Sabado):")
print (slicing_precipitaciones)

#Combinar las series resultantes del slicing en una nueva serie
serie_combinada = slicing_temperaturas.add(slicing_precipitaciones, fill_value=0)

print ("\nSerie combinada (Suma de temperaturas y precipitaciones ):")
print (serie_combinada)

#Realizar las operaciones básicas en la serie combinada
print ("\nOperaciones básicas en la serie combinada:")
print (f"Suma total: {serie_combinada.sum()}")
print (f"Promedio: {serie_combinada.mean():.2f}")
print (f"Maximo valor: {serie_combinada,max()}")
print (f"Minimo valor: {serie_combinada.min()}")