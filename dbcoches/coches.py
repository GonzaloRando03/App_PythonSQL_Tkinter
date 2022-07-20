import tkinter as tk
from client.gui_app import FrameCoche, barraMenu


def main():
    root = tk.Tk()                                                  #clase que crea una interfaz
    root.title('Modelos de coche')                                  #titulo de la ventana
    root.iconbitmap('dbcoches/src/coche.ico')                       #icono del programa
    root.resizable(0,0)                                             #para que no pueda cambiar de tamaño la ventana

    barraMenu(root)

    app = FrameCoche(root = root)

    app.mainloop()                                                 #hace que la interfaz se mantenga abierta

    


if __name__ == '__main__':
    main()
