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
    
    global nombre_material
    nombre_material = None
    
    global buscarMat 
    buscarMat = None

def Formulario():
        
    global frame1,tree,buscarCod,buscarMat,nombre_buscado,nombre_material
        
    try:
        ventana = Tk()
        ventana.geometry("1200x800")
        ventana.title("REGISTRO DE ALMACEN")
            
        frame1 = Frame(ventana,padx=10,pady=10)
        frame1.pack(side=LEFT,anchor='nw',padx=10,pady=10,fill='both',expand=True)
        frame1.config(width=20,height=40)
        
        buscarCod = StringVar()
        buscarMat = StringVar()
        
        
        Label(frame1, text="Codigo De Material", width=15, font=("arial",12),padx=5,pady=5).grid(row=0,column=0)
        Label(frame1, text="Descripcion Del Material",width=20, font=("arial",12),padx=5,pady=5).grid(row=1,column=0)
        Entry(frame1,width=15,textvariable=buscarCod).grid(row=0,column=1,padx=10,pady=10)
        Entry(frame1,width=15,textvariable=buscarMat).grid(row=1,column=1,padx=10,pady=10)
        Button(frame1, text="BUSCAR",width=15,command=buscar_nombre).grid(row=2,columnspan=2,padx=5,pady=5)
        
        tree = ttk.Treeview(frame1,columns=("CODIGO MATERIAL","MATERIAL - DESCRIPCION","GRUPO","INGENIERO 1",
                                                    "INGENIERO 2","INGENIERO 3","ALMACEN","TOTAL","UNIDADES DE MEDIDA"),show='headings',height=20)
        
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
        
        tree.grid(row=0,rowspan=50,column=3, sticky=tk.NE)
        
        ventana.mainloop()
        
    except ValueError as error:
        print("Error al mostrar la interfaz, error: {}".format(error))


def buscar_nombre():
        global nombre_producto, nombre_buscado,buscarCod,tree,dato,nombre_material
        try:
            
            if not buscarCod.get():
                
                nombre_producto = " "
                nombre_producto = str(nombre_producto)
            else:  
                nombre_producto = buscarCod.get()
                nombre_producto = str(nombre_producto)
            
            if not buscarMat.get():
    
                nombre_material = " "
                nombre_material = str(nombre_material)
            else:
    
                nombre_material = buscarMat.get()
                nombre_material = str(nombre_material)
                
            nombre_buscado = Alma.busca_producto(nombre_producto,nombre_material)

            
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
    global nombre_producto, nombre_buscado,buscarCod,tree
    
    tree.delete(*tree.get_children())
    registro = Alma.mostrar_productos()
    i = -1
    for dato in registro:
        i= i+1                       
        tree.insert('',i, text = registro[i][1:2], values=registro[i][0:9])


            
Formulario()