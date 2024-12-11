#EJERCICIO DE LISTAS 

#Modulo de copias profundas
import copy

#Crear una lista
empleados = [
    ["Pedro", ["Python", "SQL"]], 
    ["Manolo", ["Java", "C++", "JavaScript"]], 
    ["Alejandro", ["HTML", "CSS", "JavaScript"]]
]

#Mostrar lista original
print ("Lista original: ")
print (empleados)

#Copia Superficial y Copia Profunda
#Primera: Copia Superficial
copia_superficial = empleados.copy()

#Copia Profunda
copia_profunda = copy.deepcopy(empleados)

#Modificar habilidades de empleados
empleados[0][1].append("JavaScript")
empleados[1][1].append("Inteligencia Artificial")
empleados[2][1].append("Python")

#Mostrar la nueva lista
print ("\nLista después de modificar las habilidades de los empleados: ")
print ("Lista original:")
print (empleados)
print("\nCopia superficial: ")
print (copia_superficial)
print ("\nCopia profunda: ")
print (copia_profunda)
