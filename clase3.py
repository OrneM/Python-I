"""
Escribir un programa que permita ingresar dos números enteros a y b que representan los catetos de un 
   triángulo rectángulo e imprima la hipotenusa h de dicho triángulo.
      
   h^2=a^2+b^2

   Ej: 

   a=3
   b=4
   h=5
   
   
a = int(input("Ingrese el valor del cateto a: "))
b = int(input("Ingrese el valor del cateto b: "))

h = (a**2 + b**2)**0.5

print("La hipotenusa h es:", h)

"""

"""
a = int(input("Ingrese un numero: "))
b = int(input("Ingrese otro numero: "))

if (a == b):
    print("Los numeros son iguales")
    print("La suma es:", a + b)
else:
    print("Los numeros son diferentes")
    print("El producto es:", a * b)
    """
"""
nombre = input("Ingrese nombre del alumno: ")

if nombre == "":
    print("Error: El nombre no puede estar vacío.")
else:
    print("El nombre se ingreso correctamente.")
"""

"""
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))  
nota3 = float(input("Ingrese la tercera nota: "))

promedio = (nota1 + nota2 + nota3) / 3
print("El promedio es:", promedio)

if promedio >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

"""

"""
1) Escribir un programa que permita ingresar un número entero e imprima si dicho número 
   es par o impar.
   """

"""
numero = int(input("Ingrese un número entero: "))
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")
"""
"""
edad = int(input("Ingrese su edad: "))
sueldo = float(input("Ingrese su sueldo mensual: "))
if edad >= 30 and edad <= 50  and sueldo > 100000:
    print("prestamo aprobado")
    if edad >= 30 and edad <= 50  and sueldo < 100000:
        print("prestamo a revisar")
else:
    print("prestamo denegado")  
"""
sueldo=int(input("Sueldo: "))
if sueldo<50000:
    print("Bajo.")
else:
    if sueldo<=100000:
        print("Medio.")
    else:
        if sueldo<=200000:
            print("Bueno.")
        else:
            print("Excelente.")