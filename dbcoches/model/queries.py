from sqlite3 import connect
from .connectDB import ConnectDB
from tkinter import messagebox

def createTableCoche():
    connect = ConnectDB()
    sql = '''
        CREATE TABLE coches(
            idCoche INTEGER,
            marca VARCHAR(30),
            modelo VARCHAR(50),
            caballos NUMBER(3,0),
            PRIMARY KEY(idCoche AUTOINCREMENT)
    )'''
    try:
        connect.cursor.execute(sql)
        connect.close()
        title = 'Crear registro'
        text = 'Registro creado con éxito'
        messagebox.showinfo(title, text)                                                    #con messgebox creamos una ventana emergente que muestra si todo ha ido bien o en su defecto los errores
    except:
        title = 'Crear registro'
        text = 'Ya hay un registro creado'
        messagebox.showwarning(title, text)

def deleteTableCoche():
    try:
        connect = ConnectDB()
        sql = 'DROP TABLE coches'
        connect.cursor.execute(sql)
        connect.close()
        title = 'Borrar registro'
        text = 'Registro borrado con éxito'
        messagebox.showinfo(title, text)
    except:
        title = 'Borrar registro'
        text = 'No hay un registro que borrar'
        messagebox.showwarning(title, text)



class Coche:
    def __init__(self, marca, modelo, caballos):                                            #clase para crear objetos tipo coche
        self.idCoche = None
        self.marca = marca
        self.modelo = modelo
        self.caballos = caballos

    def __str__(self):                                                                      #función que devuelve el coche formatado
        return f'Coche[{self.marca}, {self.modelo}, {self.caballos}]'



def saveCoche(Coche):
    connect = ConnectDB()
    sql = f'''INSERT INTO coches (marca, modelo, caballos)
        VALUES('{Coche.marca}', '{Coche.modelo}', {Coche.caballos})'''
    
    try:
        connect.cursor.execute(sql)
        connect.close()
    except:
        title = 'Conexión al registro'
        text = 'La tabla coches no esta creada en la base de datos'
        messagebox.showerror(title, text)



def listCoche():
    connect = ConnectDB()
    cochesArray = []
    sql = 'SELECT * FROM coches ORDER BY idCoche DESC'

    try:
        coches = connect.cursor.execute(sql)
        cochesArray = coches.fetchall()
        connect.close()
    except:
        title = 'Conexión al registro'
        text = 'Error al consultar datos en la base de datos'
        messagebox.showerror(title, text)

    return cochesArray


def editCoche(coche, idCoche):
    connect = ConnectDB()
    sql = f'''UPDATE coches
    SET marca = '{coche.marca}', modelo = '{coche.modelo}', 
    caballos = {coche.caballos}
    WHERE idCoche = {idCoche}'''
    try:
        connect.cursor.execute(sql)
        connect.close()
    except:
        title = 'Editar objeto'
        text = 'Error al editar objetos en la base de datos'
        messagebox.showerror(title, text)

def delCoche(idCoche):
    connect = ConnectDB()
    sql = f'''DELETE FROM coches
    WHERE idCoche = {idCoche}'''
    try:
        connect.cursor.execute(sql)
        connect.close()
    except:
        title = 'Eliminar objeto'
        text = 'Error al eliminar objetos en la base de datos'
        messagebox.showerror(title, text)






def createTableComprador():
    connect = ConnectDB()
    sql = '''
        CREATE TABLE comprador(
            dni VARCHAR(9) CONSTRAINT pkcomprador PRIMARY KEY,
            nombre VARCHAR(50),
            fechaNacimiento VARCHAR(50),
            idCoche NUMBER(5,0) CONSTRAINT idcoche REFERENCES Coches(idCoche)
        )'''
    try:
        connect.cursor.execute(sql)
        connect.close()
        title = 'Crear registro'
        text = 'Registro creado con éxito'
        messagebox.showinfo(title, text)                                                    #con messgebox creamos una ventana emergente que muestra si todo ha ido bien o en su defecto los errores
    except:
        title = 'Crear registro'
        text = 'Ya hay un registro creado'
        messagebox.showwarning(title, text)



def deleteTableComprador():
    try:
        connect = ConnectDB()
        sql = 'DROP TABLE comprador'
        connect.cursor.execute(sql)
        connect.close()
        title = 'Borrar registro'
        text = 'Registro borrado con éxito'
        messagebox.showinfo(title, text)
    except:
        title = 'Borrar registro'
        text = 'No hay un registro que borrar'
        messagebox.showwarning(title, text)


class Comprador:
    def __init__(self, dni, nombre, fechaNacimiento, idCoche):                                            #clase para crear objetos tipo coche
        self.dni = dni
        self.nombre = nombre
        self.fechaNacimiento = fechaNacimiento
        self.idCoche = idCoche

    def __str__(self):                                                                      #función que devuelve el coche formatado
        return f'Comprador[{self.dni}, {self.nombre}, {self.fechaNacimiento}, {self.idCoche}]'



def saveComprador(Comprador):
    connect = ConnectDB()
    sql = f'''INSERT INTO comprador (dni, nombre, fechaNacimiento, idCoche)
        VALUES('{Comprador.dni}', '{Comprador.nombre}', '{Comprador.fechaNacimiento}', {Comprador.idCoche} )'''
    print(sql)
    try:
        connect.cursor.execute(sql)
        connect.close()
    except:
        title = 'Conexión al registro'
        text = 'La tabla compradores no esta creada en la base de datos'
        messagebox.showerror(title, text)


def listComprador():
    connect = ConnectDB()
    compradoresArray = []
    sql = 'SELECT * FROM comprador ORDER BY dni DESC'

    try:
        comprador = connect.cursor.execute(sql)
        compradoresArray = comprador.fetchall()
        connect.close()
    except:
        title = 'Conexión al registro'
        text = 'Error al consultar datos en la base de datos'
        messagebox.showerror(title, text)

    return compradoresArray


def editComprador(comprador, dni):
    connect = ConnectDB()
    sql = f'''UPDATE comprador
    SET nombre = '{comprador.nombre}', 
    fechaNacimiento = '{comprador.fechaNacimiento}', idCoche = {comprador.idCoche}
    WHERE dni = "{dni}"'''
    try:
        connect.cursor.execute(sql)
        connect.close()
    except:
        title = 'Editar objeto'
        text = 'Error al editar objetos en la base de datos'
        messagebox.showerror(title, text)

def delComprador(dni):
    connect = ConnectDB()
    sql = f'''DELETE FROM comprador
    WHERE dni = "{dni}"'''
    print(dni)
    try:
        connect.cursor.execute(sql)
        connect.close()
    except:
        title = 'Eliminar objeto'
        text = 'Error al eliminar objetos en la base de datos'
        messagebox.showerror(title, text)
