import tkinter as tk
from tkinter import END, messagebox
import threading
import time


root = tk.Tk()
root.title("Calculadora")
root.config(width=300, height=500)

txtDisplay = tk.Entry(root, font=("Arial", 16), justify="right")
txtDisplay.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="we")
txtDisplay.insert(0, "0")

aux = 0
signo = ""
historial = []


# --- DEMONIO: autoguardado ---
def autoguardado():
    ultimo_guardado = 0  # índice de la última operación guardada
    while True:
        if len(historial) > ultimo_guardado:
            nuevas = historial[ultimo_guardado:]
            with open(r"C:\Users\PC\OneDrive\Documentos\historial.txt", "a") as f:
                for op in nuevas:
                    f.write(op + "\n")
                    # Actualizar el índice
            ultimo_guardado = len(historial)
        time.sleep(5)  # guarda cada 5 segundos


def operador(x):
    global signo, aux
    signo = x
    aux = float(txtDisplay.get())
    txtDisplay.delete(0, END)


def operacion():
    resultado = 0
    global signo, aux
    try:
        if signo == "+":
            resultado = aux + float(txtDisplay.get())
        elif signo == "-":
            resultado = aux - float(txtDisplay.get())

        # guardar operación en historial
        operacion_str = f"{aux} {signo} {txtDisplay.get()} = {resultado}"
        historial.append(operacion_str)

        txtDisplay.delete(0, END)
        txtDisplay.insert(0, str(resultado))
    except Exception:
        messagebox.showerror("Error", "Operación inválida")


def limpiar_cero(event):
    if txtDisplay.get() == "0":
        txtDisplay.delete(0, tk.END)


txtDisplay.bind("<FocusIn>", limpiar_cero)


def insertar_numero(valor):
    actual = txtDisplay.get()
    if actual == "0":
        txtDisplay.delete(0, tk.END)
    txtDisplay.insert(tk.END, valor)


def eliminar():
    actual = txtDisplay.get()
    if len(actual) > 1:
        txtDisplay.delete(0, tk.END)
        txtDisplay.insert(0, actual[:-1])
    else:
        txtDisplay.delete(0, tk.END)
        txtDisplay.insert(0, "0")


sistemas = ["Hex", "Dec", "Oct", "Bin"]
for i, sistema in enumerate(sistemas):
    tk.Button(root, text=sistema, width=5).grid(row=1, column=i)

botones = [
    ["A", "n!", "%", "CE", "←"],
    ["B", "log", "√", "x^y", "÷"],
    ["C", "7", "8", "9", "*"],
    ["D", "4", "5", "6", "-"],
    ["E", "1", "2", "3", "+"],
    ["F", "±", "0", ".", "="]
]

for fila, fila_botones in enumerate(botones, start=2):
    for col, texto in enumerate(fila_botones):
        if texto.isdigit() or texto == ".":
            btn = tk.Button(root, text=texto, width=5, command=lambda t=texto: insertar_numero(t))
        elif texto in ["+", "-"]:
            btn = tk.Button(root, text=texto, width=5, command=lambda t=texto: operador(t))
        elif texto == "=":
            btn = tk.Button(root, text=texto, width=5, command=operacion)
        elif texto == "←":
            btn = tk.Button(root, text=texto, width=5, command=eliminar)
        else:
            btn = tk.Button(root, text=texto, width=5)  # Otros botones sin funcionalidad aún
        btn.grid(row=fila, column=col, padx=2, pady=2)


# --- Lanzar el demonio ---
hilo = threading.Thread(target=autoguardado, daemon=True)
hilo.start()

root.mainloop()
