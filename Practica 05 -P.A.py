import tkinter as tk
from tkinter import messagebox
import re
import os

def es_entero_valido(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False

def es_entero_decimal_valido(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

def es_entero_de_10_digitos(valor):
    return es_entero_valido(valor) and len(valor) == 10

def es_texto_valido(valor):
    return re.match(r"^[a-zA-Z\s]+$", valor)

def validar_edad(event):
    valor = event.widget.get()
    if not es_entero_valido(valor):
        messagebox.showerror("Error", "Por favor, ingrese una edad válida")
        event.widget.delete(0, tk.END)

def validar_estatura(event):
    valor = event.widget.get()
    if not es_entero_decimal_valido(valor):
        messagebox.showerror("Error", "Por favor, ingrese una estatura válida")
        event.widget.delete(0, tk.END)

def validar_telefono(event):
    valor = event.widget.get()
    if len(valor) < 10:
        if not es_entero_de_10_digitos(valor):
            messagebox.showerror("Error", "Por favor, ingrese un número de teléfono válido")
            event.widget.delete(0, tk.END)
    elif not es_entero_de_10_digitos(valor):
        messagebox.showerror("Error", "Por favor, ingrese un número de teléfono válido")
        event.widget.delete(0, tk.END)

def validar_texto(event):
    valor = event.widget.get()
    if not es_texto_valido(valor):
        messagebox.showerror("Error", "Por favor, ingrese un valor válido (sólo letras y espacios)")
        event.widget.delete(0, tk.END)

def guardar_datos():
    nombres = entry1.get()
    apellidos = entry2.get()
    telefono = entry3.get()
    estatura = entry4.get()
    edad = entry5.get()

    genero = ""
    if var_genero.get() == 1:
        genero = "Hombre"
    elif var_genero.get() == 2:
        genero = "Mujer"

    if (es_entero_valido(edad) and es_entero_decimal_valido(estatura) and
        es_entero_de_10_digitos(telefono) and es_texto_valido(nombres) and
        es_texto_valido(apellidos)):

        datos = f"Nombre: {nombres}\nApellidos: {apellidos}\nTelefonos: {telefono}\nEstatura: {estatura}\nEdad: {edad}\nGenero: {genero}"

        ruta_archivo = "datos.txt"

        if not os.path.exists(ruta_archivo):
            with open(ruta_archivo, "w") as archivo:
                archivo.write(datos)
        else:
            with open(ruta_archivo, "a") as archivo:
                archivo.write("\n" + datos)

        messagebox.showinfo("Información", "Datos Guardados con éxito:\n\n" + datos)
    else:
        messagebox.showerror("Error", "Por favor, ingrese datos válidos en los campos.")

# Crear la ventana principal
root = tk.Tk()
root.title("Formulario")
root.geometry("400x400")

# Variables de control
var_genero = tk.IntVar()

# Etiquetas y Entradas de texto
label1 = tk.Label(root, text="Nombres:")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Apellidos:")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()

label3 = tk.Label(root, text="Teléfono:")
label3.pack()
entry3 = tk.Entry(root)
entry3.pack()

label4 = tk.Label(root, text="Estatura:")
label4.pack()
entry4 = tk.Entry(root)
entry4.pack()

label5 = tk.Label(root, text="Edad:")
label5.pack()
entry5 = tk.Entry(root)
entry5.pack()

label6 = tk.Label(root, text="Género:")
label6.pack()

# Radiobuttons para el género
radio1 = tk.Radiobutton(root, text="Hombre", variable=var_genero, value=1)
radio1.pack()
radio2 = tk.Radiobutton(root, text="Mujer", variable=var_genero, value=2)
radio2.pack()

# Botón para guardar datos
button = tk.Button(root, text="Guardar", command=guardar_datos)
button.pack()

# Asociar validadores a las entradas de texto
entry1.bind("<FocusOut>", validar_texto)
entry2.bind("<FocusOut>", validar_texto)
entry3.bind("<FocusOut>", validar_telefono)
entry4.bind("<FocusOut>", validar_estatura)
entry5.bind("<FocusOut>", validar_edad)

root.mainloop()
