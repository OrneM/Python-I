

nombres = []

while True:
    opcion = int(input("Seleccione una opción (1, 2, o 3): "))
    if opcion == 1:
        nombre = input("Ingrese un nombre: ")
        nombres.append(nombre)
    elif opcion == 2:
        print("Nombres ingresados:")
        for nombre in nombres:
            print(nombre)
    elif opcion == 3:
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, intente de nuevo.") 



nombres=["Luis","Monica","Agustin","Luis"]
name=input("Nombre: ")

if (name in nombres):
    print("se encontró")
else:
    print("no se encontró")
    



