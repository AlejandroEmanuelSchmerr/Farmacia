import os
from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
conexion= None
def conectar():
    global conexion

    conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="farmacia"
        )
    return conexion
conectar()
cursor = conexion.cursor

cursor = conexion.cursor()
def ventana_agregar_remedio():
    ventana_agregar_remedio = Toplevel(ventana)
    ventana_agregar_remedio.title('Agregar Remedio')
    ventana_agregar_remedio.geometry('800x400')
    ventana_agregar_remedio.config(bg='royalblue2')
    
    id_remedio = Label(ventana_agregar_remedio, text='ID del remedio:')
    id_remedio.place(x=265,y=50)
    entry_id_agregar = Entry(ventana_agregar_remedio)
    entry_id_agregar.place(x=350,y=50)

    nombre_remedio = Label(ventana_agregar_remedio, text='Nombre del remedio')
    nombre_remedio.place(x=235,y=100)
    entry_nombre_agregar = Entry(ventana_agregar_remedio)
    entry_nombre_agregar.place(x=350, y=100)

    cantidad = Label(ventana_agregar_remedio, text='Cantidad:')
    cantidad.place(x=295,y=150)
    entry_cantidad_agregar = Entry(ventana_agregar_remedio)
    entry_cantidad_agregar.place(x=350,y=150)

    precio = Label(ventana_agregar_remedio, text='Precio:')
    precio.place(x=310,y=200)
    entry_precio_agregar = Entry(ventana_agregar_remedio)
    entry_precio_agregar.place(x=350,y=200)

    marca = Label(ventana_agregar_remedio, text='Marca o generico:')
    marca.place(x=250,y=250)
    marcas = ['De Marca', 'Generico' ] 
    combo_marca = ttk.Combobox(ventana_agregar_remedio, values=marcas)
    combo_marca.place(x=350, y=250)

    descripcion = Label(ventana_agregar_remedio, text='Descripcion:')
    descripcion.place(x=280, y=300)
    entry_descripcion_agregar = Entry(ventana_agregar_remedio)
    entry_descripcion_agregar.place(x=350,y=300)

    def agregar_remedios():
        id_remedio = int(entry_id_agregar.get())
        nombre = entry_nombre_agregar.get()
        cantidad = int(entry_cantidad_agregar.get())
        precio = float(entry_precio_agregar.get())
        marca = combo_marca.get()  
        descripcion = entry_descripcion_agregar.get()

        try:
            cursor.execute('INSERT INTO remedio (id_remedio, nombre_remedio, cantidad, precio, marca, descripcion) VALUES (%s, %s, %s, %s, %s, %s)',
                           (id_remedio, nombre, cantidad, precio, marca, descripcion))
            conexion.commit()
            messagebox.showinfo('Listo', 'Remedio agregado a la base de datos')
            ventana_agregar_remedio.destroy()
        except conectar.Error as err:
            messagebox.showerror('Error', f'Error: {err}')

    agrego_remedio = Button(ventana_agregar_remedio, text='Agregar remedio', command=agregar_remedios)
    agrego_remedio.place(x=350,y=350)

# Ventana para baja y modificacion de remedios
def ventana_baja_y_modificacion():
    ventana_modificar = Toplevel(ventana)
    ventana_modificar.title('Baja y Modificacion de Remedio')
    ventana_modificar.geometry('900x400')
    ventana_modificar.config(bg='firebrick2')

    treeview = ttk.Treeview(ventana_modificar, columns=('ID', 'Nombre', 'Cantidad', 'Precio', 'Marca', 'Descripción'))
    treeview.heading('#1', text='ID')
    treeview.heading('#2', text='Nombre')
    treeview.heading('#3', text='Cantidad')
    treeview.heading('#4', text='Precio')
    treeview.heading('#5', text='Marca')
    treeview.heading('#6', text='Descripcion')
    treeview.grid(row=0, column=0, columnspan=6)

    # Configure el ancho de las grillas
    treeview.column('#1', width=50)
    treeview.column('#2', width=150)
    treeview.column('#3', width=80) 
    treeview.column('#4', width=80)  
    treeview.column('#5', width=100)
    treeview.column('#6', width=200)

    def cargar_datos():
        treeview.delete(*treeview.get_children())  # Limpia grilla
        cursor.execute("SELECT * FROM remedio")
        resultados = cursor.fetchall()
        for resultado in resultados:
            treeview.insert('', 'end', values=resultado)

    cargar_datos()

    def modificar_remedio():
        item = treeview.selection()
        if item:
            item = treeview.item(item)
            id_modificar = item['values'][0]

            ventana_modificar_remedio = Toplevel(ventana_modificar)
            ventana_modificar_remedio.title('Modificar Datos Del Remedio')
            ventana_modificar_remedio.geometry('800x400')
            ventana_modificar_remedio.config(bg='orange')

            nombre_nuevo = Label(ventana_modificar_remedio, text='Nuevo nombre:')
            nombre_nuevo.place(x=262,y=50)
            entry_nombre_modificar = Entry(ventana_modificar_remedio)
            entry_nombre_modificar.place(x=350,y=50)

            cantidad_nueva = Label(ventana_modificar_remedio, text='Nueva cantidad:')
            cantidad_nueva.place(x=260,y=100)
            entry_cantidad_modificar = Entry(ventana_modificar_remedio)
            entry_cantidad_modificar.place(x=350,y=100)

            precio_nuevo = Label(ventana_modificar_remedio, text='Nuevo precio:')
            precio_nuevo.place(x=270,y=150)
            entry_precio_modificar = Entry(ventana_modificar_remedio)
            entry_precio_modificar.place(x=350,y=150)

            marca_nueva = Label(ventana_modificar_remedio, text='Nueva marca:')
            marca_nueva.place(x=272,y=200)
            marca_nuevas = ['De Marca', 'Generico']  
            combo_marca_modificar = ttk.Combobox(ventana_modificar_remedio, values=marca_nuevas)
            combo_marca_modificar.place(x=350,y=200)

            descripcion_nueva = Label(ventana_modificar_remedio, text='Nueva descripcion:')
            descripcion_nueva.place(x=245, y=250)
            entry_descripcion_modificar = Entry(ventana_modificar_remedio)
            entry_descripcion_modificar.place(x=350, y=250)

            def guardar_modificacion():
                nuevo_nombre = entry_nombre_modificar.get()
                nueva_cantidad = entry_cantidad_modificar.get()
                nuevo_precio = entry_precio_modificar.get()
                nueva_marca = combo_marca_modificar.get()  
                nueva_descripcion = entry_descripcion_modificar.get()

                try:
                    cursor.execute('UPDATE remedio SET nombre_remedio = %s, cantidad = %s, precio = %s, marca = %s, descripcion = %s WHERE id_remedio = %s',
                                   (nuevo_nombre, nueva_cantidad, nuevo_precio, nueva_marca, nueva_descripcion, id_modificar))
                    conexion.commit()
                    messagebox.showinfo('Listo', 'Remedio modificado')
                    ventana_modificar_remedio.destroy()
                    cargar_datos()  
                except conectar.Error as err:
                    messagebox.showerror('Error', f'Error: {err}')

            guardar_modificacion = Button(ventana_modificar_remedio, text='Guardar modificacion', command=guardar_modificacion)
            guardar_modificacion.place(x=350,y=350)

        else:
            messagebox.showerror('Incorrecto', 'Seleccione un remedio de la grilla')

    def eliminar_remedio():
        item = treeview.selection()
        if item:
            id_eliminar = treeview.item(item, 'values')[0]
            confirmar = messagebox.askokcancel('C', '¿Está seguro que quiere eliminar este remedio?')  # askokcancel es una función de messagebox
            if confirmar:
                try:
                    cursor.execute('DELETE FROM remedio WHERE id_remedio = %s', (id_eliminar,))
                    conexion.commit()
                    messagebox.showinfo('Listo', 'Remedio eliminado')
                    cargar_datos()  # Actualizar la grilla
                except conectar.Error as err:
                    messagebox.showerror('Error', f'Error: {err}')
        else:
            messagebox.showerror('Error', 'Incorrecto, seleccione un remedio de la grilla')

    def mostrar_datos_producto():
        id_buscar = int(entry_id_buscar.get())
        cursor.execute('SELECT * FROM remedio WHERE id_remedio = %s', (id_buscar,))
        resultado = cursor.fetchone()
        if resultado:
            messagebox.showinfo('Datos del Remedio', f'ID: {resultado[0]}\nNombre: {resultado[1]}\nCantidad: {resultado[2]}\nPrecio: {resultado[3]}\nMarca: {resultado[4]}\nDescripción: {resultado[5]}')
        else:
            messagebox.showinfo('Producto no encontrado', f'No se encontró ningún producto con el ID {id_buscar}')

    filtro = Label(ventana_modificar, text='ID del remedio para Buscar:')
    filtro.grid(row=1, column=0,columnspan=2)
    entry_id_buscar = Entry(ventana_modificar)
    entry_id_buscar.grid(row=1, column=0, columnspan=4)

    modificar = Button(ventana_modificar, text='Modificar Remedio', command=modificar_remedio)
    modificar.grid(row=2, column=0, columnspan=2)
    eliminar = Button(ventana_modificar, text='Eliminar Remedio', command=eliminar_remedio)
    eliminar.grid(row=3, column=0, columnspan=2)
    mostrar_datos = Button(ventana_modificar, text='Mostrar Datos del Remedio', command=mostrar_datos_producto)
    mostrar_datos.grid(row=4, column=0, columnspan=2)


ventana = Tk()
ventana.title('Ventana Principal Farmacia')
ventana.geometry('800x600')
ventana.config(bg='springgreen3')

foto = PhotoImage(file='images.png')
imagen_etiqueta = Label(ventana, image=foto)
imagen_etiqueta.place(x=300,y=200)


agregar = Button(ventana, text='Agregar Remedio', command=ventana_agregar_remedio)
agregar.place(x=250,y=500)
bym = Button(ventana, text='Baja y Modificación de Remedio', command=ventana_baja_y_modificacion)
bym.place(x=400,y=500)

ventana.mainloop()
