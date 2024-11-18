import tkinter as tk
from  tkinter import ttk, messagebox
from tkinter.font import BOLD
import utilities.generic as utl
from forms.master.form_master import MasterPannel
from forms.login.form_login_desing import LoginDesign

class FormLogin(LoginDesign): 

    def verify_data(self):
        user = self.user.get()
        password = self.password.get()
        if(user == 'root' and password == '1234'):
            self.wndw.destroy()
            MasterPannel()
        else:
             messagebox.showerror(message="Error! Usuario o  contraseña incorrectos", title="Error")

    
    def __init__(self):
        super().__init__()


