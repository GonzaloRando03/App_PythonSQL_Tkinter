import sqlite3

class ConnectDB:                                                                            #clase para conectarse a la base de datos
    def __init__(self):                                                                     #constructor
        self.database = "dbcoches/database/coches.db"                                                #ruta donde se alojará la db
        self.connection = sqlite3.connect(self.database)                                    #conectarnos a la db
        self.cursor = self.connection.cursor()                                              #cursor para ejecutar sql



    def close(self):                                                                        #función que crea un commit y cierra la conexión con la db
        self.connection.commit()
        self.connection.close()