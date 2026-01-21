#Continua de las clase 3, ahora con elif
"""
sueldo=int(input("Sueldo: "))
if sueldo<50000:
        print("Bajo.")
elif sueldo<=100000:
        print("Medio.")
elif sueldo<=200000:
        print("Bueno.")
else:
        print("Excelente.")
""" 

""" 
for i in range(1, 6):
    print("Hola Mundo")
    """ 

"""
a=1

while a <=5:
    print("Hola Mundo")
    a +=1
    
"""
"""
i=0

while i<10:
	print (i)
	i+=1
    """
"""
nombre = input("Ingrese su nombre: ")

while nombre == "":
    print("Error: El nombre no puede estar vacío.")
    nombre = input("Ingrese su nombre: ")

print("El nombre se ingreso correctamente.") """

"""Escribir un programa que permita ingresar un número entero mayor a 0 e
   imprima todos los números enteros desde 1 hasta el número ingresado 
   inclusive.

   """

"""

numero = int(input("Ingrese un número entero mayor a 0: "))
while numero <= 0:
    print("Error: El número debe ser mayor a 0.")
    numero = int(input("Ingrese un número entero mayor a 0: "))

acumulador= 1

while acumulador<= numero:
    print(acumulador)
    acumulador += 1

"""

puntosCardinales = ["Norte", "Sur", "Este", "Oeste"]

i= 0

while i < len(puntosCardinales):
    print(puntosCardinales[i])
    i += 1  