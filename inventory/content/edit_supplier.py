import sys
sys.path.append("../../components")
import components.color_palette as cp
import components.items as itm
import tkinter as tk
import tkinter.messagebox
import customtkinter as ctk
import pandas as pd
import os
# scripts
import components.change_page as chp


    

def edit(right_menu_frame, id):
    # OBTENEMOS LOS DATOS DEL REGISTRO
    # LEEMOS EL CSV
    df = pd.read_csv('data/inventory/suppliers.csv')
    # Obtenemos el registro equivalente al ID
    data_finded = df.iloc[id]
    print(data_finded)
    # FORMULARIO PARA CREAR NUEVO REGISTRO
    def validate_new_client():
        value_nombre = nombre.get()
        value_direccion = direccion.get()
        value_telefono = telefono.get()
        value_correo = correo.get()
        # Validar nombre
        if not value_nombre:
            tkinter.messagebox.showerror("Error", "El nombre del cliente no puede estar vacío.")
            return
        if len(value_nombre) > 20:
            tkinter.messagebox.showerror("Error", "El nombre del cliente no puede tener más de 20 caracteres.")
            return
        # Validar direccion
        if len(value_direccion) > 50:
            tkinter.messagebox.showerror("Error", "la dirección del cliente no puede tener más de 50 caracteres.")
            return    
        # Validar telefono
        if not value_telefono.isdigit():
            tkinter.messagebox.showerror("Error", "El número de teléfono solo puede definirse en números.")
            return
        if float(value_telefono) <= 0:
            tkinter.messagebox.showerror("Error", "El número del teléfono debe contener 11 dígitos.")
            return
        # Validar correo     
           
        data = {
            'Nombre': str(value_nombre),
            'Dirección': str(value_direccion) or "no tiene",
            'Teléfono': int(value_telefono) or "no tiene",
            'Correo': str(value_correo) or "no tiene",
            }
        
        df.at[id, 'Nombre'] = data["Nombre"]
        df.at[id, 'Dirección'] = data["Dirección"]
        df.at[id, 'Teléfono'] = data["Teléfono"]
        df.at[id, 'Correo'] = data["Correo"]
        
        # GUARDAMOS LOS CAMBIOS
        df.to_csv('data/inventory/suppliers.csv', index=False)
        
        
    ctk.CTkButton(master=right_menu_frame, 
                  text="Lista de proveedores", 
                  font=("Helvetica", 15, "bold"),
                  width=200,
                  height=30,
                  command=lambda:chp.new_page(right_menu_frame, "Lista de Proveedores")
                  ).place(rely=0.03, relx=0.11, anchor=tk.N)
    
    form = ctk.CTkScrollableFrame(right_menu_frame, width=1110, height=420, corner_radius=10, 
                                                    orientation="vertical",
                                                    label_text="Nuevo Proveedor",
                                                    # label_fg_color="blue",
                                                    label_text_color="white",
                                                    label_font=("Helvetica", 18),
                                                    label_anchor = "center", # "w",  # n, ne, e, se, s, sw, w, nw, center
                                                    # border_width=3,
                                                    # border_color="green",
                                                    # fg_color="red",
                                                    # scrollbar_fg_color="yellow",
                                                    # scrollbar_button_color="pink",
                                                    # scrollbar_button_hover_color = "blue", 
                                                    )
    form.place(rely=0.1, relx=0.5, anchor=tk.N)
    
    
    
    # NOMBRE DEL PROVEEDOR
    nombre = ctk.CTkEntry(master=form, placeholder_text="Nombre del proveedor",
                    width=250,
                    font=("Helvetica", 15),
                 )
    nombre.insert(0, data_finded["Nombre"])
    nombre.grid(row=0, column=0, padx=12, pady=15)
    # DIRECCION DEL PROVEEDOR
    direccion = ctk.CTkEntry(master=form, placeholder_text="Dirección del proveedor",
                    width=250,
                    font=("Helvetica", 15),
                 )
    direccion.insert(0, data_finded["Dirección"])
    direccion.grid(row=0, column=1, padx=12, pady=15)
    # TELEFONO DEL PROVEEDOR
    telefono = ctk.CTkEntry(master=form, placeholder_text="Teléfono del proveedor",
                    width=250,
                    font=("Helvetica", 15),
                 )
    telefono.insert(0, data_finded["Teléfono"])
    telefono.grid(row=1, column=0, padx=12, pady=15)
    # CORREO DEL PROVEEDOR
    correo = ctk.CTkEntry(master=form, placeholder_text="Correo Electrónico del proveedor",
                    width=250,
                    font=("Helvetica", 15),
                 )
    correo.insert(0, data_finded["Correo"])
    correo.grid(row=1, column=1, padx=12, pady=15)    
    
    submit = ctk.CTkButton(master=form, text="Registrar proveedor", width=250, font=("Helvetica", 15), command=lambda:validate_new_client()).grid(row=7, column=0, padx=30, pady=35)
