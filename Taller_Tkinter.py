import tkinter as tk
from tkinter import ttk

def init_window():

    #     Creamos la ventana y le damos nombre
    window = tk.Tk()
    window.title('MY FIRST INTERFACE WITH TKINTER')
    window.geometry('400x250')

    #     Ponemos texto dentro de la ventana
    label = tk.Label(window, text='Calculadora', font=('Arial Bold', 13))
    label.grid(column=0, row=0)

    #     Cuadros de texto donde se ingresa el valor
    entrada1 = tk.Entry(window, width = 10)
    entrada2 = tk.Entry(window, width = 10)
    entrada1.grid(column=1, row=1)
    entrada2.grid(column=1, row=2)

    #     Texto que indica el valor que vamos a ingresar y opcion deseada
    label_entrada1 = tk.Label(window,text = 'Ingrese el primer valor: ',font = ('Arial Bold',9))
    label_entrada1.grid(column = 0, row = 1)

    label_entrada2 = tk.Label(window, text = 'Ingrese el segundo valor: ', font = ('Arial Bold',9))
    label_entrada2.grid(column = 0, row = 2)

    label_operador = tk.Label(window, text = 'Escoja su operacion deseada ', font = ('Arial Bold',9))
    label_operador.grid(column = 0, row = 3)

    #     Caja de operaciones
    combo_operadores = ttk.Combobox(window)
    combo_operadores['values'] = ['+', '-', '*', '/', 'pow']
    combo_operadores.current(0)
    combo_operadores.grid(column = 1, row = 3)

    label_resultado = tk.Label(window, text = 'Resultado: ', font = ('Arial Bold', 15))
    label_resultado.grid(column = 0, row = 5)

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

    boton_calcular.grid(column = 1, row = 4)

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