#EJEMPLO
#Ver si un número es par o impar

#Pedirle al usuario un número
numero = int(input("Ingresa un número entero:  "))

#Comprobar si el número es par o impar
if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")

#Operaciones adicionales
print(f"El cuadrado de {numero} es: {numero ** 2}")
print(f"El doble de {numero} es: {numero * 2}")
print(f"El número {numero} más 10 es: {numero + 10}")