import tkinter as tk
from tkinter.messagebox import *
import customtkinter as ctk
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from PIL import Image, ImageTk

# pantallas
import inventory.content.welcome as wp
import inventory.content.new_product as pp
import inventory.content.product_list as pls
import components.change_page as chp
# scripts
import components.color_palette as cp
import components.items as tItems

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()
        
def change_frame(old_frame, new_frame):
    clear_frame(old_frame)
        
def index(app, user):
    
    # Obtenemos las dimensiones de la pantalla
    W = app.winfo_screenwidth()
    H = app.winfo_screenheight()
    # crear una nueva ventana
    dash = ctk.CTkToplevel(app)
    dash.title("inventarios Elysium DEMO")
    

    
    # dash.geometry(f"{W}x{H}")
    dash.wm_state('zoomed')
    # cerra la ventana del inicio de sesion
    app.deiconify
    
    # crear un boton para cerrar la ventana
    # elysium2 = ctk.CTkButton(
    #     master=ventana_secundaria, 
    #     text="Inventarios Elysium", 
    #     font=('arial', 15, 'bold'), 
    #     command=app.deiconify
    # )    
    # elysium2.pack()
    
    # definir las dimensiones del dashboard
    left_menu_width = float((W * 13)/100)
    right_menu_width = float((W * 88)/100)
    top_menu_height = float((H * 10)/100)
    # top_menu_width = float(left_menu_width + right_menu_width)
    bottom_menu_height = float((H * 90)/100)
    
    top_menu_frame_left = tk.Frame(master=dash, width=W+14, height=top_menu_height, bg=cp.COLORS["primary"])
    top_menu_frame_left.grid(row=0, column=0, columnspan=2)
    
    top_menu_frame_right = tk.Frame(master=dash, width=right_menu_width, height=top_menu_height, bg=cp.COLORS["primary"])
    # top_menu_frame_right.grid(row=0, column=1)
    
    left_menu_frame = tk.Frame(master=dash, width=left_menu_width, height=bottom_menu_height, bg=cp.COLORS["dark"])
    left_menu_frame.grid(row=1, column=0)
    
    right_menu_frame = tk.Frame(master=dash, width=right_menu_width, height=bottom_menu_height, bg=cp.COLORS["light"])
    right_menu_frame.grid(row=1, column=1)
    
    # definir el contenido dentro de los frames del dashboard
    # nota: para definir los widgets he de utilizar los componentes de items
    tItems.button_left_menu_dash(ctk, left_menu_frame, tk, 0.06,"     Dashboard", 
                                 right_menu_frame)
    
    tItems.button_left_menu_dash(ctk, left_menu_frame, tk, 0.12,"     Productos",
                                 right_menu_frame)
    
    tItems.button_left_menu_dash(ctk, left_menu_frame, tk, 0.18,"     Ventas",
                                 right_menu_frame)

    tItems.button_left_menu_dash(ctk, left_menu_frame, tk, 0.24,"     Clientes",
                                 right_menu_frame)

    tItems.button_left_menu_dash(ctk, left_menu_frame, tk, 0.30,"     Reportes",
                                 right_menu_frame)
    
    tItems.button_left_menu_dash(ctk, left_menu_frame, tk, 0.36,"     Provedores",
                                 right_menu_frame)
    
    tItems.button_left_menu_dash(ctk, left_menu_frame, tk, 0.42,"     Mi cuenta",
                                 right_menu_frame)
    
    tItems.button_close_session(ctk, left_menu_frame, tk, 0.48,"     Cerrar Sesión",
                                 right_menu_frame, app, dash)
                                    # inicio de sesion, dashboard
    
    ElysiumLabel = tk.Label(master=top_menu_frame_left, text="ELYSIUM DEMO", font=('arial', 18, 'bold'), bg=cp.COLORS["primary"], fg=cp.COLORS["light"])
    ElysiumLabel.place(relx=0.01, rely=0.4, anchor=tk.W)
    
    ElysiumLabel = tk.Label(master=top_menu_frame_left, text=f"Usuario: {user}", font=('arial', 11), bg=cp.COLORS["primary"], fg=cp.COLORS["light"])
    ElysiumLabel.place(relx=0.01, rely=0.7, anchor=tk.W)
        
    # logo de la app
    # login_logo = ctk.CTkImage(
    # light_image=Image.open('./assets/images/logo.png'),
	# dark_image=Image.open('./assets/images/logo.png'),
    # size=(50,50)) # WidthxHeight
    # logo = ctk.CTkLabel(master=top_menu_frame_left, text="", image=login_logo, fg_color='#fff', corner_radius=15)
    # logo.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
    wp.welcome_page(right_menu_frame)