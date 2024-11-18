from PIL import ImageTk, Image

def leer_img (path, size):
    return ImageTk.PhotoImage(Image.open(path).resize(size, Image.LANCZOS) )

def centrar_wndw (wndw, app_width, app_height): #widht , height / ancho , largo

    screen_width = wndw.winfo_screenwidth()
    screen_height = wndw.winfo_screenheight()
    x = int(  (screen_width / 2) - (app_width / 2) )
    y = int(   (screen_height / 2) - (app_height / 2) )
    return wndw.geometry(f"{app_width}x{app_height}+{x}+{y}")


