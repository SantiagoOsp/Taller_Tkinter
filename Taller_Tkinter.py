#from tkinter.ttk import Notebook
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

def init_window():

    #     Creamos la ventana y le damos nombre
    window = Tk()
    window.title('MY FIRST INTERFACE WITH TKINTER')
    window.geometry('400x250')
    s = ttk.Style()
    s.theme_use('clam')
    #window.config(style = 'clam')

    #     Menus desplegables
    def abrir():
        ventAbrir = Tk()
        ventAbrir.geometry('450x200')
        ventAbrir.title('Aca no hay nada')
        Mensaje_Abrir = Label(ventAbrir,text = 'Lo siento   xD',font = ('Times NeW Roman',30))
        Mensaje_Abrir.grid(column=230,row=100)
        ventAbrir.mainloop()

    def Nuevo():
        ventNuevo = Tk()
        ventNuevo.geometry('450x200')
        ventNuevo.title('Nuevo')
        Mensaje_ventNuevo = Label(ventNuevo,text = 'Ingresa el texto deseado',font = ('Times NeW Roman',30))
        Mensaje_ventNuevo.grid(column=0,row=0)
        cuadrotxt_Nuevo = Entry(ventNuevo)
        cuadrotxt_Nuevo.grid(column = 0, row = 1)
        var_chk = BooleanVar()
        var_chk.set(False)
        cuad_ch = Checkbutton(ventNuevo, text = 'No eres un robot', var = var_chk)
        cuad_ch.grid(column = 0, row = 2)
        hecho = Button(ventNuevo, text = 'Listo!', bg = 'Cyan', command = ventNuevo.destroy)
        hecho.grid(column = 0, row = 3)
        ventNuevo.mainloop()

    def Informacion():
        messagebox.showinfo('Info Ventana','Esta ventana es de prueba para la libreria Tkinter')

    def Notebook_window():
        n_window = Tk()
        n_window.geometry('400x200')
        n_window.title("Notebooks")

        menuBa2 = Menu(n_window)

        archivo_b = Menu(menuBa2)
        archivo_b.add_command(label = 'Abrir', command = abrir)
        archivo_b.add_command(label = 'Nuevo', command = Nuevo)
        archivo_b.add_command(label = 'Guardar')
        archivo_b.add_command(label = 'Cerrar')
        archivo_b.add_separator()
        archivo_b.add_command(label = 'Salir', command = n_window.destroy)

        edicion_b = Menu(menuBa2)
        edicion_b.add_command(label = 'Copiar')
        edicion_b.add_command(label = 'Pegar')
        edicion_b.add_command(label = 'Cortar')
        edicion_b.add_separator()
        edicion_b.add_command(label = 'Deshacer')
        edicion_b.add_command(label = 'Rehacer')

        ayuda_b = Menu(menuBa2)
        ayuda_b.add_command(label = 'Info')
        ayuda_b.add_command(label = 'No se')

        menuBa2.add_cascade(label = 'Archivo', menu = archivo_b)
        menuBa2.add_cascade(label = 'Edicion', menu = edicion_b)
        menuBa2.add_cascade(label = 'Ayuda', menu = ayuda_b)
        n_window.config(menu = menuBa2)

        pestañas = ttk.Notebook(n_window)
        pest1 = Frame(pestañas)
        pest2 = Frame(pestañas)
        pestañas.add(pest1, text = 'Notebook 1')
        pestañas.pack(expand = 1,fill = 'both')
        pestañas.add(pest2, text = 'Notebook 2')
        pestañas.pack(expand = 2, fill = 'both')

        n_window.mainloop()

    menuBa = Menu(window)

    archivo_b = Menu(menuBa)
    archivo_b.add_command(label = 'Abrir', command = abrir)
    archivo_b.add_command(label = 'Nuevo', command = Nuevo)
    archivo_b.add_command(label = 'Guardar')
    archivo_b.add_command(label = 'Cerrar')
    archivo_b.add_separator()
    archivo_b.add_command(label = 'Salir', command = window.destroy)

    edicion_b = Menu(menuBa)
    edicion_b.add_command(label = 'Copiar')
    edicion_b.add_command(label = 'Pegar')
    edicion_b.add_command(label = 'Cortar')
    edicion_b.add_separator()
    edicion_b.add_command(label = 'Deshacer')
    edicion_b.add_command(label = 'Rehacer')

    notebooks = Menu(menuBa)
    notebooks.add_command(label = 'Abrir Notebooks',command = Notebook_window)

    ayuda_b = Menu(menuBa)
    ayuda_b.add_command(label = 'Info', command = Informacion)
    ayuda_b.add_command(label = 'No se')

    menuBa.add_cascade(label = 'Archivo', menu = archivo_b)
    menuBa.add_cascade(label = 'Edicion', menu = edicion_b)
    menuBa.add_cascade(label = 'Notebooks', menu = notebooks)
    menuBa.add_cascade(label = 'Ayuda', menu = ayuda_b)
    window.config(menu = menuBa)

    #     Modificar Botones
    #ttk.Style().configure("TButton", padding = 6 , )

    #     Ponemos texto dentro de la ventana
    label = tk.Label(window, text='Calculadora', pady = 2, font=('Arial Bold', 13))
    label.grid(column=2, row=1, columnspan = 2, sticky = 'nsew')
    #label.rowconfigure(1, weight = 1)

    #     Cuadros de texto donde se ingresa el valor
    entrada1 = Spinbox(window, from_=0,to=1000,state = 'normal')
    entrada1.grid(column=3, row=2)
    entrada2 = Spinbox(window, from_=0, to=1000, state = 'normal')
    entrada2.grid(column=3, row=3)

    #     Texto que indica el valor que vamos a ingresar y opcion deseada
    label_entrada1 = tk.Label(window,text = 'Ingrese el primer valor: ',font = ('Arial Bold',9))
    label_entrada1.grid(column = 2, row = 2, sticky = 'nsew'        )

    label_entrada2 = tk.Label(window, text = 'Ingrese el segundo valor: ', font = ('Arial Bold',9))
    label_entrada2.grid(column = 2, row = 3, sticky = 'nsew')

    label_operador = tk.Label(window, text = 'Escoja su operacion deseada ', font = ('Arial Bold',9))
    label_operador.grid(column = 2, row = 4, sticky = 'nsew')

    #     Caja de operaciones
    combo_operadores = ttk.Combobox(window)
    combo_operadores['values'] = ['+', '-', '*', '/', 'pow']
    combo_operadores.current(0)
    combo_operadores.grid(column = 3, row = 4, sticky = 'nsew')

    label_resultado = tk.Label(window, text = 'Resultado: ', font = ('Arial Bold', 15))
    label_resultado.grid(column = 2, row = 6)

    #      Boton calcular
    boton_calcular = tk.Button(window,
                            command = lambda: click_calcular (
                                label_resultado,
                                entrada1.get(),
                                entrada2.get(),
                                combo_operadores.get()),
                            text = 'Calcular',
                            bg = 'Cyan',
                            fg = 'Black')

    boton_calcular.grid(column = 3, row = 5)

    window.mainloop()

def calculadora(num1, num2, operador):
    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/':
        resultado = round(num1 + num2,2)
    else:
        resultado = num1 ** num2
    return resultado

def click_calcular(label, num1, num2, operador):
    #      Conversion de valores
    valor1 = float(num1)
    valor2 = float(num2)

    #      Calculo de resultado dependiendo valores y operacion
    res = calculadora(valor1,valor2,operador)

    #      Actualizacion del texto
    label.configure(text = 'Resultado:   ' + str(res))

def main():
    init_window()

main()