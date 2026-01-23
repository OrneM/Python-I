"""nombres = ["Ana", "Luis", "Carla"]

#insertar entre ana y luis a paula

nombres.insert(1, "Paula")
nombres.append("Jorge") #agrega al final



i = 0
while i < len(nombres):
    print(nombres[i])
    i += 1
"""
"""
for i in range(1,10):   
    print(i)
"""
"""
numeros = [1, -3, -4, 7, 8, 2]

positivos = []
negativos = []

for numero in numeros:
    if numero > 0:
        positivos.append(numero)
    else:
        negativos.append(numero)

print("Números positivos:", positivos)
print("Números negativos:", negativos)
"""

"""i = 1
while i <= 5:
    print(i)
    i += 1
"""
"""
for i in range(1, 51):
    print(i)
    """
inicio= int(input("Ingrese un numero inicial de rango:"))
fin= int(input("Ingrese un numero final de rango:"))

multiplos_de_3_y_5= []


for i in range(inicio, fin+1):
    if i % 3 == 0 and i % 5 == 0:
        multiplos_de_3_y_5.append(i)

print("Múltiplos de 3 y 5 entre", inicio, "y", fin, ":", multiplos_de_3_y_5)