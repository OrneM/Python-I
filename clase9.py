import tkinter as tk

def boton_click():
    print("¡Hola, ", caja.get(), "!")
    etiqueta2.config(text="¡Hola, " + caja.get() + "!") 

ventana = tk.Tk()
ventana.title("Primera aplicación de escritorio")
ventana.geometry("400x300")   # más directo que config width/height

boton = tk.Button(ventana, text="Saludar"    , command=boton_click)   
boton.place(x=150, y=130)

caja= tk.Entry() 
caja.place(x=150, y=100, width=100, height=20)


etiqueta = tk.Label(text="Ingrese su nombre: ", background="Blue", font=("Arial", 12))
etiqueta.place(x=150, y=70)

etiqueta2 = tk.Label()
etiqueta2.place(x=150, y=160)

ventana.mainloop()