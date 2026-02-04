matriz = [
    [3.3, 6.1, 4.0],
    [4.9, 5.7, 6.4],
]
fila = int(input("Fila: "))-1
columna = int(input("Columna: "))-1

if fila >= 0 and fila < len(matriz):
    if columna >= 0 and columna < len(matriz[fila]):
        print("El valor es:", matriz[fila][columna])
    else:
        print("Columna incorrecta")
else:
    print("Fila incorrecta")

