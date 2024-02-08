import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from time import strftime
import pandas as pd

from Conexion import *

from Almacen import *

class FormularioAlmacen():
    
    global frame1
    frame1 = None
    global buscarCod
    buscarCod = None
    global nombre_buscado
    nombre_buscado = None
    global nombre_producto
    nombre_producto = None
    global Cod1
    Cod1 = None
    global reserva
    reserva = None
    global sipro
    sipro = None
    global cantidad
    cantidad = None

def Formulario():
        
    global frame1,tree,buscarCod,buscarMat,nombre_buscado,refrescar,Cod1,reserva,sipro,cantidad
        
    try:
        ventana = Tk()
        ventana.geometry("1200x800")
        ventana.title("REGISTRO DE ALMACEN")
            
        frame1 = LabelFrame(ventana,text="Inventario - Almacen",padx=10,pady=10)
        frame1.pack(side="left", anchor='n',padx=10, pady=10, fill='both', expand=True)
        frame1.config(width=5,height=5)
        frame3 = LabelFrame(ventana,text="TABLA",padx=10,pady=10)
        frame3.pack(side=RIGHT, anchor='n', fill='both', expand=True)
        frame3.config(width=5, height=10)
        
        #METODO BUSCAR
        buscarCod = StringVar()
        Label(frame1, text="Codigo De Material", width=15, font=("arial",12),padx=5,pady=5).grid(row=0,column=0)
        Entry(frame1,width=15,textvariable=buscarCod).grid(row=0,column=1,padx=10,pady=10)
        Button(frame1, text="BUSCAR",width=15,command=buscar_nombre).grid(row=1,columnspan=2,padx=5,pady=5)
        
        #METODO AGREGAR
        LabelFrame(frame1,text= "Agregar materiales").grid(row=2,columnspan=2)
        Label(frame1, text="Codigo De Material", width=15, font=("arial",12),padx=5,pady=5).grid(row=2,column=0)
        Label(frame1, text="SIPRO", width=15, font=("arial",12),padx=5,pady=5).grid(row=3,column=0)
        Label(frame1, text="RESERVA", width=15, font=("arial",12),padx=5,pady=5).grid(row=4,column=0)
        Label(frame1, text="Cantidad a ingresar", width=15, font=("arial",12),padx=5,pady=5).grid(row=5,column=0)
        Label(frame1, text="Asignar Material", width=15, font=("arial",12),padx=5,pady=5).grid(row=6,column=0)
        
        Cod1 = StringVar()
        sipro = StringVar()
        reserva = StringVar()
        cantidad = StringVar()
        
        Entry(frame1,width=15,textvariable=Cod1).grid(row=2,column=1,padx=10,pady=10)
        Entry(frame1,width=15,textvariable=sipro).grid(row=3,column=1,padx=10,pady=10)
        Entry(frame1,width=15,textvariable=reserva).grid(row=4,column=1,padx=10,pady=10)
        Entry(frame1,width=15,textvariable=cantidad).grid(row=5,column=1,padx=10,pady=10)
        
        
        #Combobox para asignar material a un ing o almacen
        AsignarMateriales = tk.StringVar()
        Asigna = ttk.Combobox(frame1, values=["Ingeniero 1","Ingeniero 2", "Ingeniero 3", "Almacen"],textvariable=AsignarMateriales,width=28)
        Asigna.grid(row=6,column=1,padx=5,pady=5)
        AsignarMateriales.set("Asigne mat. a una persona")
        
        Button(frame1, text="Agregar",width=15, command = agregarCantidad).grid(row=7,columnspan=2)
        
        #TABLA DE DATOS
        tree = ttk.Treeview(frame3,columns=("CODIGO MATERIAL","MATERIAL - DESCRIPCION","GRUPO","INGENIERO 1",
                                                    "INGENIERO 2","INGENIERO 3","ALMACEN","TOTAL","UNIDADES DE MEDIDA"),show='headings',height=10)
        
        tree.column("# 1",anchor=CENTER, width=100)
        tree.column("# 2", width=270)
        tree.column("# 3",anchor=CENTER, width=50)
        tree.column("# 4",anchor=CENTER, width=50)
        tree.column("# 5",anchor=CENTER, width=50)
        tree.column("# 6",anchor=CENTER, width=50)
        tree.column("# 7",anchor=CENTER, width=70)
        tree.column("# 8",anchor=CENTER, width=50)
        tree.column("# 9",anchor=CENTER, width=100)
            
        tree.heading("# 1",text="COD MATERIAL")
        tree.heading("# 2",text="MATERIAL - DESCRIPCION")
        tree.heading("# 3",text="GRUPO")
        tree.heading("# 4",text="ING 1")
        tree.heading("# 5",text="ING 2")
        tree.heading("# 6",text="ING 3")
        tree.heading("# 7",text="ALMACEN")
        tree.heading("# 8",text="TOTAL")
        tree.heading("# 9",text="UN-MEDIDA")
        
        for row in Alma.mostrar_productos():
            tree.insert("","end",values=row)
        
        tree.grid(row=1,rowspan=50,column=0, sticky=tk.NE)
        
        #Boton para refrescar la tabla de datos
        Button(frame3, text="Refrescar",width=15,command=actualizarTreeView).grid(row=0,column=0)
        
        ventana.mainloop()
        
    except ValueError as error:
        print("Error al mostrar la interfaz, error: {}".format(error))


def buscar_nombre():
        global nombre_producto, nombre_buscado,buscarCod,tree,dato,refrescar,Cod1,reserva,sipro,cantidad
        try:
            if not buscarCod.get():
                nombre_producto = " "
                nombre_producto = str(nombre_producto)
            else:  
                nombre_producto = buscarCod.get()
                nombre_producto = str(nombre_producto)
            nombre_buscado = Alma.busca_producto(nombre_producto)

            tree.delete(*tree.get_children())
            i = -1
            
            for dato in nombre_buscado:
                i= i+1                       
                tree.insert('',i, text = nombre_buscado[i][1:1], values=nombre_buscado[i][0:9])
                
            if nombre_buscado == []:
                messagebox.showinfo("Informacion", "El codigo de material ingresado no es correcto")
                
        except ValueError as error:
            print("Error al buscarCod, error: {}".format(error))

def mostrar_todo():
    global nombre_producto, nombre_buscado,buscarCod,tree,refrescar,Cod1,reserva,sipro,cantidad,Asigna,asigna,reser,canti,codMat,sipro1
    
    tree.delete(*tree.get_children())
    registro = Alma.mostrar_productos()
    i = -1
    for dato in registro:
        i= i+1                       
        tree.insert('',i, text = registro[i][1:2], values=registro[i][0:9])

def actualizarTreeView():
    global tree,datos,refrescar,Cod1,reserva,sipro,cantidad,asigna,reser,codMat,sipro1
    
    try:
        tree.delete(*tree.get_children())
        datos = Alma.mostrar_productos()
            
        for row in Alma.mostrar_productos():
                tree.insert("","end", values=row)
    
    except ValueError as error:
        print("Error al actualizar tabla {}".format(error))

def agregarCantidad():
        
        global tree,refrescar,Cod1,reserva,sipro,cantidad,Asigna,asigna,reser,codMat,sipro1,canti
        
        try:
            if Cod1 is None or reserva is None or Asigna is None or cantidad is None or sipro is None:
                print("Los widgets no estan inicializados")
                return
            
            codMat = Cod1.get()
            reser = reserva.get()
            sipro1 = sipro.get()
            canti = cantidad.get()
            asigna = asigna.get()
            
                #Llamamos la clase y la funcion de clientes para asignar los valores de cada variable a la tabla
            Alma.ingresarCantidad(canti,codMat)
            messagebox.showinfo("Informacion", "Los datos fueron guardados")

            actualizarTreeView()
            
                #Limpiamos los campos
            cantidad.delete(0,END)
            Cod1.delete(0,END)
            
        except ValueError as error:
            print("Error al ingresar los datos {}".format(error))


def modificarRegistros():
        
        global tree,refrescar,Cod1,reserva,sipro,cantidad,Asigna
        
        try:
            
                #verificar si los widgets (Editext) estan inicializados (contienen la informacion a registrar)
            if textBoxId is None or textBoxNombres is None or textBoxApellidos is None or combo is None:
                print("Los widgets no estan inicializados")
                return
            
            idUsuario = textBoxId.get()
            nombres = textBoxNombres.get()
            apellidos = textBoxApellidos.get()
            sexo = combo.get()
            
                #Llamamos la clase y la funcion de clientes para asignar los valores de cada variable a la tabla
            CClientes.modificarClientes(idUsuario,nombres,apellidos,sexo)
            
                #Por medio del messagebox emitimos un cuadro de notificacion respecto al estado de los datos
                #(titulo del cuadro de dialogo - texto informativo)
            messagebox.showinfo("Informacion", "Los datos fueron actualizados")
            
            actualizarTreeView()
            
                #Limpiamos los campos
            textBoxId.delete(0,END)
            textBoxNombres.delete(0,END)
            textBoxApellidos.delete(0,END)
        except ValueError as error:
            print("Error al ingresar los datos {}".format(error))

      
Formulario()