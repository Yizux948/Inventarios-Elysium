# libs
import tkinter
from tkinter.messagebox import *
import customtkinter as ctk
from PIL import Image, ImageTk
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

# scripts
import inventory.index as index

ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

app = ctk.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x440")
app.title("Elysium")
# app.resizable(0,0)


def test():
    print("hola")
    
    
def submit(root):

    # obtenemos los valores introducidos por el usuario
    user_value = str(user.get())
    password_value = str(password.get())
    
    # abrimos el json con los usuarios
    datos = pd.read_json('data/users.json')
    actual_user = datos[datos['user'] == user_value]
    
    # verificamos si el usuario ingresado existe
    if(not actual_user.empty):
        
        # obtenemos el usuario y contrasena correspondientes a dicha cuenta
        finded_user = str(actual_user.user.values[0])
        finded_password = str(actual_user.password.values[0])
        # comparamos la contrasena
        if(finded_password == password_value):
            # showerror('Error', 'Usuario encontrado')
            # root.destroy()
            hoy = date.today()
            limite = date(2024, 7, 3)
            
            if hoy > limite:
                showwarning('Licencia Expirada', 'Adquiere una licencia para continuar utilizando el sistema') 
                return   
            
            root.withdraw()
            index.index(app, finded_user)
        else:
            showerror('Contraseña inválida', 'Verifica tus datos y vuelve a intentarlo')
    # si el usuario no existe se lo hacemos saber al usuario
    else:
        showerror('Usuario no encontrado', 'Verifica tus datos y vuelve a intentarlo')


    
background = ctk.CTkImage(
    light_image=Image.open('./assets/images/pattern.png'),
	dark_image=Image.open('./assets/images/pattern.png'),
    size=(1366,768)) # WidthxHeight ,size=(180,250)

my_label = ctk.CTkLabel(master=app, text="", image=background)
my_label.pack()




# creando el frame del formulario
frame = ctk.CTkFrame(master=app, width=320, height=360, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

# creando el titulo de la aplicacion en el inicio de sesión
elysium = ctk.CTkLabel(master=frame, text="Inventarios Elysium DEMO", font=('arial', 15, 'bold'))
elysium.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

# creando el logo en el inicio de sesión
login_logo = ctk.CTkImage(
    light_image=Image.open('./assets/images/user_icon.png'),
	dark_image=Image.open('./assets/images/user_icon.png'),
    size=(90,90)) # WidthxHeight

logo = ctk.CTkLabel(master=frame, text="", image=login_logo, fg_color='#fff', corner_radius=15)
logo.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)


# creando los inputs
user = ctk.CTkEntry(
    master=frame, 
    placeholder_text="Usuario", 
    placeholder_text_color="white", 
    font=('arial', 13))
user.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

password = ctk.CTkEntry(
    master=frame, 
    placeholder_text="Constraseña", 
    placeholder_text_color="white", 
    font=('arial', 13))
password.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

submit_button = ctk.CTkButton(
    master=frame,
    text="Ingresar",
    font=('arial', 13, "bold"),
    command=lambda:submit(app)
)

submit_button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)




# index.index(app, "Jesus")



def on_closing():
    plt.close('all')
    app.quit()
    app.destroy()
app.protocol("WM_DELETE_WINDOW", on_closing)

app.mainloop()