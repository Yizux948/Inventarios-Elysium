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
    df = pd.read_csv('data/inventory/clients.csv')
    # Obtenemos el registro equivalente al ID
    data_finded = df.iloc[id]
    print(data_finded)
    # FORMULARIO PARA CREAR NUEVO PRODUCTO
    def validate_new_client():
        value_cedula = cedula.get()
        value_nombre = nombre.get()
        value_apellido = apellido.get()
        value_direccion = direccion.get()
        value_telefono = telefono.get()
        value_correo = correo.get()
        
        # Validar cedula
        if not value_cedula.isdigit():
            tkinter.messagebox.showerror("Error", "La cédula del cliente solo puede definirse en números.")
            return
        if float(value_cedula) <= 0:
            tkinter.messagebox.showerror("Error", "El número del cédula debe ser mayor a 0.")
            return        
        # Validar nombre del producto
        if not value_nombre:
            tkinter.messagebox.showerror("Error", "El nombre del cliente no puede estar vacío.")
            return
        if len(value_nombre) > 20:
            tkinter.messagebox.showerror("Error", "El nombre del cliente no puede tener más de 20 caracteres.")
            return
        # Validar apellido
        if not value_apellido:
            tkinter.messagebox.showerror("Error", "El apellido del cliente no puede estar vacío.")
            return
        if len(value_apellido) > 20:
            tkinter.messagebox.showerror("Error", "El apellido del cliente no puede tener más de 20 caracteres.")
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
            'Cédula': int(value_cedula),
            'Nombre': str(value_nombre),
            'Apellido': str(value_apellido),
            'Teléfono': int(value_telefono) or "no tiene",
            'Correo': str(value_correo) or "no tiene",
            'Dirección': str(value_direccion) or "no tiene"
            }
        
        print(data["Cédula"])
        print(data["Nombre"])
        print(data["Apellido"])
        print(data["Teléfono"])
        print(data["Correo"])
        print(data["Dirección"])
        
        df.at[id, 'Cédula'] = data["Cédula"]
        df.at[id, 'Nombre'] = data["Nombre"]
        df.at[id, 'Apellido'] = data["Apellido"]
        df.at[id, 'Teléfono'] = data["Teléfono"]
        df.at[id, 'Correo'] = data["Correo"]
        df.at[id, 'Dirección'] = data["Dirección"]
        
        
        # GUARDAMOS LOS CAMBIOS
        df.to_csv('data/inventory/clients.csv', index=False)
        
        
    ctk.CTkButton(master=right_menu_frame, 
                  text="Lista de productos", 
                  font=("Helvetica", 15, "bold"),
                  width=200,
                  height=30,
                  command=lambda:chp.new_page(right_menu_frame, "Lista de Productos")
                  ).place(rely=0.03, relx=0.11, anchor=tk.N)
    
    client_form = ctk.CTkScrollableFrame(right_menu_frame, width=1110, height=420, corner_radius=10, 
                                                    orientation="vertical",
                                                    label_text="Nuevo Producto",
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
    client_form.place(rely=0.1, relx=0.5, anchor=tk.N)
    
    
    # CEDULA
    cedula = ctk.CTkEntry(master=client_form, placeholder_text="Cédula del cliente",
                    width=250,
                    font=("Helvetica", 15),
                 )
    cedula.insert(0, data_finded["Cédula"])
    cedula.grid(row=0, column=0, padx=12, pady=15)
        
    # NOMBRE
    nombre = ctk.CTkEntry(master=client_form, placeholder_text="Nombre del cliente",
                    width=250,
                    font=("Helvetica", 15),
                 )
    nombre.insert(0, data_finded["Nombre"])
    nombre.grid(row=0, column=1, padx=12, pady=15)

    # APELLIDO
    apellido = ctk.CTkEntry(master=client_form, placeholder_text="Apellidos del cliente",
                    width=250,
                    font=("Helvetica", 15),
                 )
    apellido.insert(0, data_finded["Apellido"])
    apellido.grid(row=0, column=2, padx=12, pady=15)
        
    # TELEFONO
    telefono = ctk.CTkEntry(master=client_form, placeholder_text="Teléfono del cliente",
                    width=250,
                    font=("Helvetica", 15),
                 )
    telefono.insert(0, data_finded["Teléfono"])
    telefono.grid(row=1, column=0, padx=12, pady=15)   
    
    # CORREO ELECTRÓNICO
    correo = ctk.CTkEntry(master=client_form, placeholder_text="Correo electrónico del cliente",
                    width=250,
                    font=("Helvetica", 15),
                 )
    correo.insert(0, data_finded["Correo"])
    correo.grid(row=1, column=1, padx=12, pady=15)       
    
    # DIRECCION 
    direccion = ctk.CTkEntry(master=client_form, placeholder_text="Dirección del cliente",
                    width=250,
                    font=("Helvetica", 15),
                 )
    direccion.insert(0, data_finded["Dirección"])
    direccion.grid(row=1, column=2, padx=12, pady=15)        
    
    submit = ctk.CTkButton(master=client_form, text="Registrar cliente", width=250, font=("Helvetica", 15), command=lambda:validate_new_client()).grid(row=7, column=0, padx=30, pady=35)
