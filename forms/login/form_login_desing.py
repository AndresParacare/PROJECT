import tkinter as tk
from  tkinter import ttk, messagebox
from tkinter.font import BOLD
import utilities.generic as utl
from forms.master.form_master import MasterPannel

class LoginDesign:

    def verificar():
        pass

    def userRegister():
        pass
    def __init__(self):
        self.wndw = tk.Tk()
        self.wndw.title("Inicio de sesion")
        self.wndw.geometry("800x500")
        self.wndw.config(bg="#fcfcfc")
        self.wndw.resizable(width=0,height=0)
        utl.centrar_wndw(self.wndw, 800,500)

        logo =  utl.leer_img("./Imagenes/simple_blue_logo_for_administration_software-removebg.png", (200,200))

        #FRAME LOGO (Panel que contiene el logo)
        frame_logo = tk.Frame(self.wndw, bd = 0, width= 300, relief = tk.SOLID, padx=10, pady=10, bg="#3a7ff6")
        frame_logo.pack(side = "left", expand=tk.NO,  fill=tk.BOTH)
        lbl = tk.Label(frame_logo, image= logo, bg="#3a7ff6")
        lbl.place(x=0,y=0,relwidth=1,relheight=1)

        #FRAME FORM (Frame que contiene el login)
        frame_form = tk.Frame(self.wndw, bd = 0, relief=tk.SOLID,  padx=10, pady=10, bg="#fcfcfc")
        frame_form.pack(side = "right", expand=tk.YES, fill=tk.BOTH)

        #FRAME FORM TOP(Tope del frame del logina, contiene el texto de Inicio de  sesion)
        frame_form_top = tk.Frame(frame_form,height=50, bd = 0, relief=tk.SOLID,bg="black")
        frame_form_top.pack(side = "top", expand=tk.NO, fill=tk.X)
        title = tk.Label(frame_form_top, text="Inicio de sesion", font=('Vogue',30), fg= "#666a88", bg= "#fcfcfc", pady=50)
        title.pack(expand=tk.YES, fill=tk.BOTH)

        #FRAME FORM FILL (Frame de relleno, informacion de usuario)
        frame_form_fill = tk.Frame(frame_form, bd = 0, relief=tk.SOLID, bg="#fcfcfc")
        frame_form_fill.pack(side = "top", expand=tk.YES, fill=tk.BOTH)

        tag_usr = tk.Label(frame_form_fill,text= "Usuario", font=('Vogue',14), fg="#666a88", bg="#fcfcfc", anchor="center")
        tag_usr.pack(fill=tk.X,  padx=40, pady=10)
        self.user = ttk.Entry(frame_form_fill, font = ('Vogue', 12))
        self.user.pack(fill=tk.X,  padx=40, pady=10)

        tag_password = tk.Label(frame_form_fill,text= "Contrasena", font=('Vogue',14), fg="#666a88", bg="#fcfcfc", anchor="center")
        tag_password.pack(fill=tk.X,  padx=40, pady=10)
        self.password = ttk.Entry(frame_form_fill, font = ('Vogue', 12))
        self.password.pack(fill=tk.X,  padx=40, pady=10)
        self.password.config(show="*")

        start = tk.Button(frame_form_fill,  text="Iniciar sesion", font=('Vogue',14, BOLD), fg="#3a7ff6", bd=0, bg="#fff", command=self.verify_data)
        start.pack(fill=tk.X,padx=20, pady=20)
        start.bind("<Return>", (lambda event : self.start(self.verify_data())))

        start = tk.Button(frame_form_fill, text= "Registrar usuario", font=("Times",15), bg= "#fcfcfc", bd= 0, fg= "#3a77f6", command= self.userRegister)
        start.pack(fill= tk.X, padx= 20, pady=20)
        start.bind("<Return>", lambda event: self.start(self.userRegister()))

        self.wndw.mainloop()
    