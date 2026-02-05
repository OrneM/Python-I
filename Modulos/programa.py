import operaciones
import areas


def realizar_operaciones_basicas():
    while True:
        print("\nOperaciones básicas seleccionadas.")
        print("Seleccione la operación que desea realizar:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("Escriba 'cerrar' para volver al menú principal")

        opcion = input("Ingrese el número de la operación (o 'cerrar'): ").strip().lower()

        if opcion == "cerrar":
            return

        if opcion not in ("1", "2", "3", "4"):
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")
            continue

        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if opcion == "1":
            resultado = operaciones.sumar(num1, num2)
            print(f"El resultado de la suma es: {resultado}")

        elif opcion == "2":
            resultado = operaciones.restar(num1, num2)
            print(f"El resultado de la resta es: {resultado}")

        elif opcion == "3":
            resultado = operaciones.multiplicar(num1, num2)
            print(f"El resultado de la multiplicación es: {resultado}")

        elif opcion == "4":
            if num2 == 0:
                print("No se puede dividir por 0.")
            else:
                resultado = operaciones.dividir(num1, num2)
                print(f"El resultado de la división es: {resultado}")


def realizar_calculo_areas():
    while True:
        print("\nCálculo de áreas seleccionado.")
        print("Seleccione la figura para calcular su área:")
        print("1. Círculo")
        print("2. Cuadrado")
        print("3. Rectángulo")
        print("Escriba 'cerrar' para volver al menú principal")

        opcion = input("Ingrese el número de la figura (o 'cerrar'): ").strip().lower()

        if opcion == "cerrar":
            return

        if opcion == "1":
            radio = float(input("Ingrese el radio del círculo: "))
            resultado = areas.circulo(radio)
            print(f"El área del círculo es: {resultado}")

        elif opcion == "2":
            lado = float(input("Ingrese el lado del cuadrado: "))
            resultado = areas.cuadrado(lado)
            print(f"El área del cuadrado es: {resultado}")

        elif opcion == "3":
            base = float(input("Ingrese la base del rectángulo: "))
            altura = float(input("Ingrese la altura del rectángulo: "))
            resultado = areas.rectangulo(base, altura)
            print(f"El área del rectángulo es: {resultado}")

        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 3.")


print("Bienvenido al programa de operaciones matemáticas")

while True:
    print("\nSeleccione el tipo de operación que desea realizar:")
    print("1. Operaciones básicas")
    print("2. Cálculo de áreas")
    print("Escriba 'cerrar' para salir")

    tipo_operacion = input("Ingrese el número del tipo de operación (o 'cerrar'): ").strip().lower()

    if tipo_operacion == "cerrar":
        print("Programa cerrado. ¡Hasta la próxima! 👋")
        break
    elif tipo_operacion == "1":
        realizar_operaciones_basicas()
    elif tipo_operacion == "2":
        realizar_calculo_areas()
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 2.")
