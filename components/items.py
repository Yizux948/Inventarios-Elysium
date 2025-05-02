import customtkinter as ctk
import tkinter as tk
import matplotlib.pyplot as plt
# pantallas
import inventory.content.welcome as wp
import inventory.content.new_product as pp
import inventory.content.product_list as pls
# scripts
import components.change_page as chp

    
def button_left_menu_dash(ctk, left_menu_frame, tk, y, t, screen):
    button_top_menu = ctk.CTkButton(master=left_menu_frame, text=t, width=150, height=35, corner_radius=0, anchor="w", font=('arial', 12, 'bold'), command=lambda:chp.new_page(screen, t))
    button_top_menu.place(relx=0.5, rely=y, anchor=tk.N)
    
def button_close_session(ctk, left_menu_frame, tk, y, t, screen, root, dash):
    button_top_menu = ctk.CTkButton(master=left_menu_frame, text=t, width=150, height=35, corner_radius=0, anchor="w", font=('arial', 12, 'bold'), command=lambda:chp.close_session(root, dash))
    button_top_menu.place(relx=0.5, rely=y, anchor=tk.N)
    
        
def imageTag():
    pass

def imageButton():
    pass

def contador_card(right_menu_frame, title, batch, ry, rx):
    frame_contador = ctk.CTkFrame(master=right_menu_frame, width=150, height=120, corner_radius=7)
    frame_contador.place(rely=ry, relx=rx, anchor=tk.N)
    
    ventas_hoy = ctk.CTkLabel(
        master=frame_contador, 
        text=title, 
        font=('arial', 18, 'bold')
        )
    ventas_hoy.place(rely=0, relx=0.5, anchor=tk.N)
    separador = ctk.CTkLabel(
        master=frame_contador,
        text="____________",
        font=('arial', 18, 'bold')
        )
    separador.place(rely=0.2, relx=0.5, anchor=tk.N)
    cantidad_hoy = ctk.CTkLabel(
        master=frame_contador, 
        text=" "+batch, 
        font=('arial', 18, 'bold')
        )
    cantidad_hoy.place(rely=1, relx=0, anchor=tk.SW)