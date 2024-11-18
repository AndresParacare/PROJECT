import tkinter as tk #TKINTER PARA GENERAR BOTONES, VENTANA, ETC...
from tkinter.font import BOLD #IMPORTAR ESTILO DE FUENTE
import utilities.generic as utl
class MasterPannel():
    def __init__(self):
        self.wndw = tk.Tk()
        self.wndw.title("Admin. de Estacion de servicio")
        w, h = self.wndw.winfo_screenmmwidth(), self.wndw.winfo_screenmmheight()
        self.wndw.geometry("%dx%d+0+0" % (w, h))
        self.wndw.config(bg = "#fcfcfc")
        self.wndw.resizable(width=0, height=0)
        logo =  utl.leer_img("./Imagenes/simple_blue_logo_for_administration_software-removebg.png", (200,200))

        lbl =  tk.Label(self.wndw, image = logo, bg = "#3a7ff6")
        lbl.place(x=0, y=0, relwidth  = 1, relheight = 1)
        self.wndw.mainloop()



