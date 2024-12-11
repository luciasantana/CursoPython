#EJERCICIO DE TEMPERATURAS

#Lista de temperaturas en grados Celsius
temperaturas = [-200, -198, -196, -195, -193, -180, -150, -100]

#Temperatura crítica del nitrógeno
temperatura_critica = -196

#Usar una lista por compresión para filtrar temperaturas mayores o iguales a -196ºC
estado_gaseoso = [temp for temp in temperaturas if temp >= temperatura_critica]
print ("Temperaturas done el nitrógeno permanece en estado gaseoso: ", estado_gaseoso)

#Resultado: Temperaturas done el nitrógeno permanece en estado gaseoso:  [-196, -195, -193, -180, -150, -100]
