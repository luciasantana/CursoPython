#EJERCICIO DE PELÍCULAS

def menu():
    print ("\nGestión de Películas")
    print ("1. Añadir Película")
    print ("2. Eliminar Película")
    print ("3. Mostrar lista de películas")
    print ("4. Buscar Películas")
    print ("5. Salir")
    return input ("Selecciona un aopción: ")

#Lista vacía para almacenar películas
peliculas = []

while True:
    opcion = menu()

    if opcion == "1":
        #Añadir película
        pelicula = input("Ingresa el nombre de la pelicula que quiera añadir. ").strip()
        if pelicula in peliculas:
            print (f"La película '{pelicula}' ya está en la lista.")
        else:
            peliculas.append(pelicula)
            print (f"Película '{pelicula}' añadida a la lista.")
    
    elif opcion == "2":
        #Eliminar película
        pelicula = input ("Ingresa el nombre de la película que quiere elimina: ").strip()
        if pelicula in peliculas:
            peliculas.remove(pelicula)
            print (f"Película '{pelicula}' eliminada de la lista.")
        else:
            print (f"La película '{pelicula}' no está en la lista.")
    
    elif opcion == "3":
        #Mostrar lista de películas
        if peliculas:
            print ("\nLista de películas: ")
            for i, pelicula in enumerate(peliculas, start=1):
                print (f"{i}. {pelicula}")
        else:
            print ("La lista de películas está vacía.")
    
    elif opcion == "4":
        #Buscar película
        pelicula = input ("Ingresa el nombre de la películaque desea buscar: ").strip()
        if pelicula in peliculas:
            print (f"La película '{pelicula}' está en la lista.")
        else:
            print (f"La película '{pelicula}' no está en la lista.")
    
    elif opcion == "5":
        #Salir del programa
        print ("Saliendo del programa. ¡Hasta pronto!")
        break
    
    else:
        print ("Opción no válida. Por favor, seleccione una opción del menú.")