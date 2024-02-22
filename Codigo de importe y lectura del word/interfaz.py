import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from time import strftime
from Excel import *
import pandas as pd
from Conexion import *
from Almacen import *
from tkinter import filedialog
import shutil
import PyPDF2

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
    global Asigna
    Asigna = None
    global ref
    ref = None
    global inv
    inv = None

def Formulario():
        
    global frame1,frame2,tree,buscarCod,nombre_buscado,Cod1,reserva,sipro,cantidad,fren,Asigna,frame3,frame4,button
        
    try:
        
        ventana = tk.Tk()
        ventana.geometry("1200x800")
        ventana.title("REGISTRO DE ALMACEN")
        
        # Crear el widget Notebook
        notebook = ttk.Notebook(ventana)

        # Crear pestañas
        pestana1 = ttk.Frame(notebook)
        pestana2 = ttk.Frame(notebook)
        
        # Añadir las pestañas al notebook
        notebook.add(pestana1, text="ALMACEN")
        notebook.add(pestana2, text="CONTRATOS")    
        
        # Funcion que ejecutaran las opciones de la barra de tareas
        def mostrar_mensaje():
            print("Haz hecho clic en la opción del menú")
   
        # Crear un objeto Menú (Barra de tareas)
        barra_tareas = tk.Menu(ventana)

        # Crear menú desplegable "Archivo" (Barra de tareas)
        menu_archivo = tk.Menu(barra_tareas, tearoff=0)
        menu_archivo.add_command(label="Abrir", command=mostrar_mensaje)
        menu_archivo.add_command(label="Guardar", command=mostrar_mensaje)
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Salir", command=ventana.destroy)

        # Crear menú desplegable "Ayuda" (Barra de tareas)
        menu_ayuda = tk.Menu(barra_tareas, tearoff=0)
        menu_ayuda.add_command(label="Acerca de", command=mostrar_mensaje)

        # Agregar menús a la barra de tareas
        barra_tareas.add_cascade(label="Archivo", menu=menu_archivo)
        barra_tareas.add_cascade(label="Ayuda", menu=menu_ayuda)

        # Configurar la barra de tareas en la ventana 
        ventana.config(menu=barra_tareas)
        
        # Frame para contener los widgets de la pestaña 1
        frame1 = LabelFrame(pestana1,text="Inventario - Almacen",padx=10,pady=10)
        frame1.pack(side="left", anchor='n',padx=10, pady=10, fill='both', expand=True)
        frame2 = LabelFrame(pestana1,text="TABLA",padx=10,pady=10)
        frame2.pack(side=RIGHT, anchor='n', fill='both', expand=True,padx=10,pady=10)
        
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
        Asigna = ttk.Combobox(frame1, values=["Ingeniero 1","Ingeniero 2", "Ingeniero 3", "Almacen"],textvariable=AsignarMateriales,width=20)
        Asigna.grid(row=6,column=1,padx=5,pady=5)
        AsignarMateriales.set("Asigne mat. a una persona")
        
        Button(frame1, text="Agregar",width=15, command = agregarCantidad).grid(row=7,column=0)
        Button(frame1, text="Retirar",width=15, command = retirarLaCantidad).grid(row=7,column=1)
        
        #TABLA DE DATOS
        tree = ttk.Treeview(frame2,columns=("CODIGO MATERIAL","MATERIAL - DESCRIPCION","GRUPO","INGENIERO 1",
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
        
        tree.pack(padx=5,pady=10, fill='both')
        
        #Boton para refrescar la tabla de datos
        Button(frame2, text="Refrescar",width=15,command=actualizarTreeView,height=15).pack(padx=20,pady=20, fill='both',side=LEFT,ipadx=15,ipady=15)
        
        #Boton para hacer el inventario
        Button(frame2, text="Inventario", command=funcionInventario,width=15,height=15).pack(padx=20,pady=20, fill='both',side=RIGHT,ipadx=15,ipady=15)
        
        # Posicionamiento del notebook
        notebook.pack(padx=10, pady=10, fill='both', expand=True)
        
        #______________________________________________________________________________________________
        
        # Frame para contener los widgets de la pestaña 2
        frame3 = LabelFrame(pestana2,text="Contrato",padx=10,pady=10)
        frame3.pack(side="left", anchor='n',padx=10, pady=10, fill='both', expand=True)
        
        frame4 = LabelFrame(pestana2,text="TABLA",padx=10,pady=10)
        frame4.pack(side=RIGHT, anchor='n', fill='both', expand=True,padx=10,pady=10)
        
        # Widgets pestaña 2
        LabelFrame(frame3,text= "Agregar materiales").grid(row=2,columnspan=2)
        Label(frame3, text="Codigo De Material", width=15, font=("arial",12),padx=5,pady=5).grid(row=2,column=0)
        Label(frame3, text="SIPRO", width=15, font=("arial",12),padx=5,pady=5).grid(row=3,column=0)
        Label(frame3, text="RESERVA", width=15, font=("arial",12),padx=5,pady=5).grid(row=4,column=0)
        Label(frame3, text="Cantidad a ingresar", width=15, font=("arial",12),padx=5,pady=5).grid(row=5,column=0)
        Label(frame3, text="Asignar Material", width=15, font=("arial",12),padx=5,pady=5).grid(row=6,column=0)
        
        Cod1 = StringVar()
        sipro = StringVar()
        reserva = StringVar()
        cantidad = StringVar()
        
        Entry(frame3,width=15,textvariable=Cod1).grid(row=2,column=1,padx=10,pady=10)
        Entry(frame3,width=15,textvariable=sipro).grid(row=3,column=1,padx=10,pady=10)
        Entry(frame3,width=15,textvariable=reserva).grid(row=4,column=1,padx=10,pady=10)
        Entry(frame3,width=15,textvariable=cantidad).grid(row=5,column=1,padx=10,pady=10)
        
        button = tk.Button(frame4, text='Importar archivo', command=lambda: importar_archivo_y_guardar('C:/Users/diosc/OneDrive/Escritorio/A.CRDA'))
        button.pack()
        
        ventana.mainloop()
        
    except ValueError as error:
        print("Error al mostrar la interfaz, error: {}".format(error))

def importar_archivo_y_guardar(ruta_destino):
    file_path = filedialog.askopenfilename(filetypes=[('Archivos PDF', '*.pdf'), ('Archivos de texto', '*.txt')])
    if file_path:
        shutil.copy(file_path, ruta_destino)
        print(f'Archivo copiado desde {file_path} a {ruta_destino}')

def buscar_nombre():
        global nombre_producto, nombre_buscado,buscarCod,tree,dato,Cod1,reserva,sipro,cantidad
        
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
    
    global nombre_producto, nombre_buscado,buscarCod,tree,Cod1,reserva,sipro,cantidad,Asigna,asigna,reser,canti,codMat,sipro1
    
    tree.delete(*tree.get_children())
    registro = Alma.mostrar_productos()
    i = -1
    for dato in registro:
        i= i+1                       
        tree.insert('',i, text = registro[i][1:2], values=registro[i][0:9])

def actualizarTreeView():
    
    global tree,datos,Cod1,reserva,sipro,cantidad,asigna,reser,codMat,sipro1
    
    try:
        
        tree.delete(*tree.get_children())
        datos = Alma.mostrar_productos()
            
        for row in Alma.mostrar_productos():
                tree.insert("","end", values=row)
    
    except ValueError as error:
        print("Error al actualizar tabla {}".format(error))

def agregarCantidad():
        
        global tree,Cod1,reserva,sipro,cantidad,Asigna,fren,reser,codMat,sipro1,canti,f1,f2,f3,f4
        
        try:
            if Cod1 is None or reserva is None or Asigna is None or cantidad is None or sipro is None:
                print("Los widgets no estan inicializados")
                return
            
            codMat = Cod1.get()
            reser = reserva.get()
            sipro1 = sipro.get()
            canti = cantidad.get()
            fren = Asigna.get()
            fren = str(fren)
            
            Alma.ingresarCantidad(fren,canti,codMat)
            
            messagebox.showinfo("Informacion", "Los datos fueron guardados")

            actualizarTreeView()
            
            
            #Limpiamos los campos
            
            
        except ValueError as error:
            print("Error al ingresar los datos {}".format(error))

def retirarLaCantidad():
        
        global tree,Cod1,reserva,sipro,cantidad,Asigna,fren,reser,codMat,sipro1,canti,f1,f2,f3,f4
        
        try:
            if Cod1 is None or reserva is None or Asigna is None or cantidad is None or sipro is None:
                print("Los widgets no estan inicializados")
                return
            
            codMat = Cod1.get()
            reser = reserva.get()
            sipro1 = sipro.get()
            canti = cantidad.get()
            fren = Asigna.get()
            fren = str(fren)
            
            nutr = Alma.RetirarCantidad(fren,canti,codMat)
            if nutr == 1:
                messagebox.showinfo("Informacion", "Los elementos fueron retirados")
            else:
                messagebox.showinfo("Informacion", "La cantidad a retirar supera el stock")

            actualizarTreeView()
            
        except ValueError as error:
            print("Error al ingresar los datos {}".format(error))

def funcionInventario():
    global nombre_producto, nombre_buscado,buscarCod,tree,Cod1,reserva,sipro,cantidad,Asigna,asigna,reser,canti,codMat,sipro1
    
    tree.delete(*tree.get_children())
    registro = Alma.Inventario()
    i = -1
    for dato in registro:
        i= i+1                       
        tree.insert('',i, text = registro[i][1:2], values=registro[i][0:9])


    
Formulario()