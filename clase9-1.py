import tkinter as tk

def sumar():
    n1 = int(caja1.get())
    n2 = int(caja2.get())
    suma = n1 + n2
    resultado.config(text="Resultado: " + str(suma))

def restar():
    n1 = int(caja1.get())
    n2 = int(caja2.get())
    resta = n1 - n2
    resultado2.config(text="Resultado: " + str(resta))
def salir():
    ventana.destroy()

ventana = tk.Tk()
ventana.config(width=300, height=200)
ventana.title("SUMAR")

caja1= tk.Entry() 
caja1.place(x=20, y=20, width=100, height=20)

caja2= tk.Entry() 
caja2.place(x=20, y=60, width=100, height=20)

boton = tk.Button(ventana, text="SUMAR", command = sumar)   
boton.place(x=20, y=100)

boton2 = tk.Button(ventana, text="RESTAR", command = restar)
boton2.place(x=100, y=100)

resultado = tk.Label(text="")
resultado.place(x=20, y=130)
resultado2 = tk.Label(text="")
resultado2.place(x=100, y=130)


salir_boton = tk.Button(ventana, text="SALIR", command=salir)
salir_boton.place(x=200, y=100)

ventana.mainloop()

