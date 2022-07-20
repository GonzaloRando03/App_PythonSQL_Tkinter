import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from model.queries import createTableCoche, delComprador, listComprador, saveComprador, createTableComprador, deleteTableCoche, Comprador, Coche, saveCoche, listCoche, editCoche, delCoche


def barraMenu(root):                                                                #creamos una función para las opciones de la barra de arriba
    barraMenu = tk.Menu(root)
    root.config(menu = barraMenu, width = 300, height = 300)

    menuInicio = tk.Menu(barraMenu, tearoff = 0)                                    #creamos el boton de inicio dentro de la barra con las opciones crear y eliminar registro y salir
    barraMenu.add_cascade(label = 'Inicio', menu = menuInicio)
    barraMenu.add_cascade(label = 'Consultas')                                      #los demás botones no son funcionales
    barraMenu.add_cascade(label = 'Configuración')
    barraMenu.add_cascade(label = 'Ayuda')

    menuInicio.add_command(label = 'Crear registro en DB', command = createTableCoche)
    menuInicio.add_command(label = 'Eliminar registro en DB', command = deleteTableCoche)
    menuInicio.add_command(label = 'Salir', command = root.destroy)



class FrameCoche(tk.Frame):                                                         #creamos una clase heredada de frame para definir nuestro frame
    def __init__(self, root = None):                                                #constructor de la clase
        super().__init__( root, width = 480, height = 320 )                         #creamos la herencia 
        self.root = root                                                            #guardamos el frame de root en la raiz de la clase gracias a la herencia
        self.pack()
        self.idCoche = None
        self.config(width = 480, height = 320, bg = '#1B1C23')                      #configuración de tamaño y colores del frame

        self.campos()

        self.disableObject()

        self.objectTable()

    menu = 'coche'

    def campos(self):                                                               #funcion para los campos
        if self.menu == 'coche':
            titulo = 'Base de datos: Coches'
        elif self.menu == 'comprador':
            titulo = 'Base de datos: Compradores'

        self.title = tk.Label(self, text = titulo)                                  #label marca
        self.title.config( 
            font = ( 'arial', 20, 'bold' ), 
            bg = '#1B1C23', 
            fg = 'white'
        )
        self.title.grid( 
            row = 0, 
            column = 0, 
            padx = 10, 
            pady = 10, 
            columnspan = 4
        ) 

        #Labels
        if self.menu == 'coche':
            label1 = 'Marca: '
        elif self.menu == 'comprador':
            label1 = 'DNI: '

        self.lFirst = tk.Label(self, text = label1)                                   #label marca
        self.lFirst.config( 
            font = ( 'arial', 12, 'bold' ), 
            bg = '#1B1C23', 
            fg = 'white'
        )
        self.lFirst.grid( row = 1, column = 0, padx = 10, pady = 10 )                 #posicionamiento de los campos y padding en los ejes


        if self.menu == 'coche':
            label2 = 'Modelo: '
        elif self.menu == 'comprador':
            label2 = 'Nombre: '

        self.lSecond = tk.Label(self, text = label2)                                   #label modelo
        self.lSecond.config( 
            font = ( 'arial', 12, 'bold' ), 
            bg = '#1B1C23', 
            fg = 'white'
        )
        self.lSecond.grid( row = 2, column = 0, padx = 10, pady = 10 )

        if self.menu == 'coche':
            label3 = 'Caballos: '
        elif self.menu == 'comprador':
            label3 = 'Fecha de nacimiento: '

        self.lThird = tk.Label(self, text = label3)                                     #label caballos
        self.lThird.config( 
            font = ( 'arial', 12, 'bold' ), 
            bg = '#1B1C23', 
            fg = 'white' 
        )
        self.lThird.grid( row = 3, column = 0, padx = 10, pady = 10 )

        if self.menu == 'comprador':
            self.lidCoche = tk.Label(self, text = 'ID Coche: ')                        #label idCoche
            self.lidCoche.config( 
                font = ( 'arial', 12, 'bold' ), 
                bg = '#1B1C23', 
                fg = 'white' 
            )
            self.lidCoche.grid( row = 4, column = 0, padx = 10, pady = 10 )

        #Inputs
        self.vFirst = tk.StringVar()
        self.iFirst = tk.Entry(self, textvariable = self.vFirst)                        #input text marca, texvariable guarda el valor del texto
        self.iFirst.config(
            width = 50, 
            font = ( 'arial', 12 ), 
            bg = '#2A2B36', 
            fg = 'white'
        )
        self.iFirst.grid( row = 1, column = 1, padx = 10, pady = 10, columnspan = 2 )

        self.vSecond = tk.StringVar()
        self.iSecond= tk.Entry(self, textvariable = self.vSecond)                                                #input text modelo
        self.iSecond.config( 
            width = 50, 
            font = ( 'arial', 12 ), 
            bg = '#2A2B36', 
            fg = 'white'
        )
        self.iSecond.grid( row = 2, column = 1, padx = 10, pady = 10, columnspan = 2 )

        self.vThird = tk.StringVar()
        self.iThird = tk.Entry(self, textvariable = self.vThird)                                             #input text caballos
        self.iThird.config( 
            width = 50, 
            font = ( 'arial', 12 ), 
            bg = '#2A2B36', 
            fg = 'white'
        )
        self.iThird.grid( row = 3, column = 1, padx = 10, pady = 10, columnspan = 2 )

        if self.menu == 'comprador':
            self.vidCoche = tk.StringVar()
            self.iidCoche = tk.Entry(self, textvariable = self.vidCoche)                                             #input text idCoche
            self.iidCoche.config( 
                width = 50, 
                font = ( 'arial', 12 ), 
                bg = '#2A2B36', 
                fg = 'white'
            )
            self.iidCoche.grid( row = 4, column = 1, padx = 10, pady = 10, columnspan = 2 )

        #Botones
        self.bNuevo = tk.Button( self, text = 'Nuevo', command = self.enableObject )                             #botón nuevo
        self.bNuevo.config( 
            width = 20, 
            fg = 'white', 
            font = ( 'arial', 12, 'bold' ), 
            bg = '#2A2B36', 
            cursor = 'hand2',                                                           #para que se cambie el raton al pasar por encima
            activebackground = '#3A3C44'
        )
        self.bNuevo.grid( row = 5, column = 0, padx = 10, pady = 10)

        self.bGuardar = tk.Button( self, text = 'Guardar', command = self.saveObject )                         #botón guardar
        self.bGuardar.config( 
            width = 20,
            font = ( 'arial', 12, 'bold' ),
            fg = 'white',  
            bg = '#2C8F4C',
            cursor = 'hand2',
            activebackground = '#34A659'
        )
        self.bGuardar.grid( row = 5, column = 1, padx = 10, pady = 10 )

        self.bCancelar = tk.Button( self, text = 'Cancelar', command = self.disableObject )                       #botón cancelar
        self.bCancelar.config( 
            width = 20,
            font = ( 'arial', 12, 'bold' ), 
            fg = 'white', 
            bg = '#8F2C2C',
            cursor = 'hand2',
            activebackground = '#AF3434'
        )
        self.bCancelar.grid( row = 5, column = 2, padx = 10, pady = 10 )

        

    def enableObject(self):                                                             #función para activar los campos
        self.iFirst.config(state = 'normal')
        self.iSecond.config(state = 'normal')
        self.iThird.config(state = 'normal')

        self.bGuardar.config(state = 'normal')
        self.bCancelar.config(state = 'normal')
        
        if self.menu == 'comprador':
            self.iidCoche.config(state = 'normal')



    def disableObject(self):                                                            #función para desactivar campos
        self.vFirst.set('')                                                             #pone los valores de los input vacios
        self.vSecond.set('')
        self.vThird.set('')

        if self.menu == 'comprador':
            self.vidCoche.set('')
        
        self.iFirst.config(
            state = 'disabled', 
            disabledbackground = 'grey'
        )
        self.iSecond.config(
            state = 'disabled', 
            disabledbackground = 'grey'
        )
        self.iThird.config(
            state = 'disabled', 
            disabledbackground = 'grey'
        )

        if self.menu == 'comprador':
            self.iidCoche.config(
                state = 'disable',
                disabledbackground = 'grey'
            )

        self.bGuardar.config(state = 'disabled')
        self.bCancelar.config(state = 'disabled')



    def saveObject(self):                                                               #función para guardar los datos
        if self.menu == 'coche':
            coche = Coche(
                self.vFirst.get(),
                self.vSecond.get(),
                self.vThird.get()
            )
            if self.idCoche == None:
                saveCoche(coche)
            else:
                editCoche(coche, self.idCoche)
        elif self.menu == 'comprador':
            comprador = Comprador(
                self.vFirst.get(),
                self.vSecond.get(),
                self.vThird.get(),
                self.vidCoche.get()
            )
            saveComprador(comprador)
        self.disableObject()
        self.objectTable()


    def objectTable(self):                                                              #función para crear la tabla donde van los objetos de la db
        if self.menu == 'coche':
            self.cochesArray = listCoche()

            self.table = ttk.Treeview(self,
                column = ('Marca', 'Modelo', 'Caballos')
            )
            self.table.grid(
                row = 6, 
                column = 0,
                padx = 10, 
                pady = 10, 
                columnspan = 4
            )
            self.table.heading('#0', text = 'ID')                                       #en la posición 0 pondra ID como título
            self.table.heading('#1', text = 'Marca')
            self.table.heading('#2', text = 'Modelo')
            self.table.heading('#3', text = 'Caballos')

            for c in self.cochesArray:                                                  #bucle para mostrar los objetos de la tabla
                self.table.insert('',0, 
                    text = c[0],                                                        #id que se encuentra en la posición 0
                    values = (c[1], c[2], c[3])                                         #el resto de campos
                )
        
        elif self.menu == 'comprador':
            self.CompradoresArray = listComprador()

            self.table = ttk.Treeview(self,
                column = ('dni','nombre', 'fechaNacimiento', 'idCoche')
            )
            self.table.grid(
                row = 6, 
                column = 0,
                padx = 10, 
                pady = 10, 
                columnspan = 4
            )
            self.table.heading('#0', text = 'ID')                                       #en la posición 0 pondra ID como título
            self.table.heading('#1', text = 'Nombre')
            self.table.heading('#2', text = 'Fecha Nacimiento')
            self.table.heading('#3', text = 'ID Coche')
        
            for c in self.CompradoresArray:                                             #bucle para mostrar los objetos de la tabla
                self.table.insert('',0, 
                    text = c[0],                                                        #id que se encuentra en la posición 0
                    values = (c[1], c[2], c[3])                                         #el resto de campos
                )

        self.scroll = tk.Scrollbar(                                                     #scrollbar de la tabla
            self, 
            orient = 'vertical', 
            command = self.table.yview,
        )
        self.scroll.config(bg= 'grey')
        self.scroll.grid(row = 6, column = 4, sticky = 'nse')
        self.table.configure(yscrollcommand = self.scroll.set )
       
        


        self.bEditar = tk.Button( self, text = 'Editar', command = self.editar)                       #botón editar
        self.bEditar.config( 
            width = 20, 
            fg = 'white', 
            font = ( 'arial', 12, 'bold' ), 
            bg = '#2A2B36', 
            cursor = 'hand2',                                                       
            activebackground = '#3A3C44'
        )
        self.bEditar.grid( row = 7, column = 0, padx = 10, pady = 10)

        self.bEliminar = tk.Button( self, text = 'Eliminar', command = self.eliminar)                    #botón eliminar
        self.bEliminar.config( 
            width = 20,
            font = ( 'arial', 12, 'bold' ), 
            fg = 'white', 
            bg = '#8F2C2C',
            cursor = 'hand2',
            activebackground = '#AF3434'
        )
        self.bEliminar.grid( row = 7, column = 1, padx = 10, pady = 10 )

        self.bClientes = tk.Button( self, text = 'Clientes/Coches', command = self.cambiar)                       #botón editar
        self.bClientes.config( 
            width = 20, 
            fg = 'white', 
            font = ( 'arial', 12, 'bold' ), 
            bg = '#2A2B36', 
            cursor = 'hand2',                                                       
            activebackground = '#3A3C44'
        )
        self.bClientes.grid( row = 7, column = 2, padx = 10, pady = 10)



    def editar(self):
        if self.menu == 'coche':
            try:
                self.idCoche = self.table.item(
                    self.table.selection()
                )['text']
                self.First = self.table.item(
                    self.table.selection()
                )['values'][0]                                                      #coge el primer valor
                self.Second = self.table.item(
                    self.table.selection()
                )['values'][1]                                                      #coge el segundo valor
                self.Third = self.table.item(
                    self.table.selection()
                )['values'][2]                                                      #coge el primer valor

                self.enableObject()

                self.iFirst.insert(0, self.First)                                   #metemos el valor de los campos en el input
                self.iSecond.insert(0, self.Second)
                self.iThird.insert(0, self.Third)

            except:
                title = 'Edición de objeto'
                text = 'Error al editar el objeto en la base de datos'
                messagebox.showerror(title, text)

        elif self.menu == 'comprador':
            try:
                self.First = self.table.item(
                    self.table.selection()
                )['text']
                self.Second = self.table.item(
                    self.table.selection()
                )['values'][0]                                                      #coge el primer valor
                self.Third = self.table.item(
                    self.table.selection()
                )['values'][1]                                                      #coge el segundo valor
                self.idCoche = self.table.item(
                    self.table.selection()
                )['values'][2]                                                      #coge el primer valor

                self.enableObject()

                self.idni.insert(0, self.First) 
                self.inombre.insert(0, self.Second)                                 #metemos el valor de los campos en el input
                self.ifechaNacimiento.insert(0, self.Third)
                self.iidCoche.insert(0, self.idCoche)

            except:
                title = 'Edición de objeto'
                text = 'Error al editar el objeto en la base de datos'
                messagebox.showerror(title, text)

    def eliminar(self):
        if self.menu == 'coche':
            try:
                self.idCoche = self.table.item(
                    self.table.selection()
                )['text']
                delCoche(self.idCoche)
                self.objectTable()

            except:
                title = 'Eliminación de objeto'
                text = 'Error al eliminar el objeto en la base de datos'
                messagebox.showerror(title, text)
        
        elif self.menu == 'comprador':
            try:
                self.First = self.table.item(
                    self.table.selection()
                )['text']
                delComprador(self.First)
                self.objectTable()

            except:
                title = 'Eliminación de objeto'
                text = 'Error al eliminar el objeto en la base de datos'
                messagebox.showerror(title, text)

    def cambiar(self):
        if self.menu == 'coche':
            self.menu = 'comprador'
        elif self.menu == 'comprador':
            self.menu = 'coche'

        self.root.destroy()

        root = tk.Tk()                                                          #clase que crea una interfaz
        root.title('Modelos de coche')                                          #titulo de la ventana
        root.iconbitmap('dbcoches/src/coche.ico')                               #icono del programa
        root.resizable(0,0)                                                     #para que no pueda cambiar de tamaño la ventana

        barraMenu(root)

        self.__init__(root = root)