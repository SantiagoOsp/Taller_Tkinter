# Taller_Tkinter

Este repositorio almacenara el taller instructivo de Tkinter de programacion de computadores 2020-II

## Widgets:

Tkinter permite añadir diferentes widgets a sus interfaces, de los cuales se usaron :

- *Label* :

  ´´´python
  label = tk.Label(window, text='Calculadora', pady = 2, font=('Arial Bold', 13))
  label.grid(column=2, row=1, columnspan = 2, sticky = 'nsew')
  ´´´

- *Button* :

  ´´´python
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
  ´´´

- *Menu* :

  ´´´python
  menuBa2 = Menu(n_window)
  ...
  menuBa2.add_cascade(label = 'Archivo', menu = archivo_b)
  menuBa2.add_cascade(label = 'Edicion', menu = edicion_b)
  menuBa2.add_cascade(label = 'Ayuda', menu = ayuda_b)
  n_window.config(menu = menuBa2)
  ´´´

- *Notebooks* :

  ´´´python
  pestañas = ttk.Notebook(n_window)
  pest1 = Frame(pestañas)
  pest2 = Frame(pestañas)
  pestañas.add(pest1, text = 'Notebook 1')
  pestañas.pack(expand = 1,fill = 'both')
  pestañas.add(pest2, text = 'Notebook 2')
  pestañas.pack(expand = 2, fill = 'both')
  ´´´

- *Combobox* :

  ´´´python
  combo_operadores = ttk.Combobox(window)
  combo_operadores['values'] = ['+', '-', '*', '/', 'pow']
  combo_operadores.current(0)
  combo_operadores.grid(column = 3, row = 4, sticky = 'nsew')
  ´´´

> **Nota**
> La gran parte de los botones de menu o Notebook´s no tienen funcionalidad.
