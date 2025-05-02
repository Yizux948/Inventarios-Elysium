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


    

def new_product_form(right_menu_frame):
    # FORMULARIO PARA CREAR NUEVO PRODUCTO
    def validate_new_product():
        value_nombre = nombre.get()
        value_descripcion = descripcion.get()
        value_precio = precio.get()
        value_cantidad = cantidad.get()
        value_medida = medidas_entry.get()
        value_proveedor = proveedores_entry.get()
        value_compra = compra.get()
        # Validar nombre del producto
        if not value_nombre:
            tkinter.messagebox.showerror("Error", "El nombre del producto no puede estar vacío.")
            return
        if len(value_nombre) > 50:
            tkinter.messagebox.showerror("Error", "El nombre del producto no puede tener más de 50 caracteres.")
            return
        # Validar descripcion
        if len(value_descripcion) > 50:
            tkinter.messagebox.showerror("Error", "La descripción del producto no puede tener más de 50 caracteres.")
            return
        # Validar precio
        if not value_precio:
            tkinter.messagebox.showerror("Error", "El precio del producto no puede estar vacío.")
            return        
        if not value_precio.isdigit():
            tkinter.messagebox.showerror("Error", "El precio del producto solo puede definirse en números.")
            return
        if float(value_precio) <= 0:
            tkinter.messagebox.showerror("Error", "El precio del producto no puede ser menor o igual a 0.")
            return            
        # Validar cantidad
        if not value_cantidad:
            tkinter.messagebox.showerror("Error", "El precio del producto no puede estar vacío.")
            return        
        if not value_cantidad.isdigit():
            tkinter.messagebox.showerror("Error", "El precio del producto solo puede definirse en números.")
            return
        if float(value_cantidad) <= 0:
            tkinter.messagebox.showerror("Error", "El precio del producto no puede ser menor o igual a 0.")
            return    
        # Validar medida
        if value_medida == "Tipo de Medida del producto":
            tkinter.messagebox.showerror("Error", "Debes seleccionar una unidad de medición válida.")
            return
        # Validar proveedor
        if value_proveedor == "Proveedor":
            tkinter.messagebox.showerror("Error", "Debes seleccionar un proveedor válido.")
            return
        # Validar precio de compra
        if not value_compra:
            tkinter.messagebox.showerror("Error", "El precio de compra del producto no puede estar vacío.")
            return        
        if not value_compra.isdigit():
            tkinter.messagebox.showerror("Error", "El precio de compra del producto solo puede definirse en números.")
            return
        # Agregar producto
        # print(value_nombre)
        # print(value_descripcion)
        # print(value_precio)
        # print(value_cantidad)
        # print(value_medida)
        # print(value_proveedor)
        data = {
            'Nombre': [str(value_nombre)],
            'Descripción': [str(value_descripcion) or "no tiene"],
            'Precio': [str(value_precio)],
            'PrecioCompra': [str(value_compra)],
            'Cantidad': [str(value_cantidad)],
            'Medida': [str(value_medida)],
            'Proveedor': [str(value_proveedor)]
            }
        df = pd.DataFrame(data)
        filename = "data/inventory/products.csv"
        # Verificar si el archivo ya existe
        if not os.path.isfile(filename):
            # Si el archivo no existe, escribir el DataFrame con el encabezado
            df.to_csv(filename, mode='w', index=False, header=True)
        else:
            # Si el archivo existe, anexar el DataFrame sin el encabezado
            df.to_csv(filename, mode='a', index=False, header=False)   
        
        
    ctk.CTkButton(master=right_menu_frame, 
                  text="Lista de productos", 
                  font=("Helvetica", 15, "bold"),
                  width=200,
                  height=30,
                  command=lambda:chp.new_page(right_menu_frame, "Lista de Productos")
                  ).place(rely=0.03, relx=0.11, anchor=tk.N)
    
    product_form = ctk.CTkScrollableFrame(right_menu_frame, width=1110, height=420, corner_radius=10, 
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
    product_form.place(rely=0.1, relx=0.5, anchor=tk.N)
    
    # NOMBRE DEL PRODUCTO
    nombre = ctk.CTkEntry(master=product_form, placeholder_text="Nombre del producto",
                    width=250,
                    font=("Helvetica", 15),
                 )
    nombre.grid(row=0, column=0, padx=12, pady=15)
    
    # DESCRIPCION DEL PRODUCTO
    descripcion = ctk.CTkEntry(master=product_form, placeholder_text="Descripción del producto",
                    width=250,
                    font=("Helvetica", 15),
                 )
    descripcion.grid(row=0, column=1, padx=12, pady=15)

    # PRECIO DEL PRODUCTO
    precio = ctk.CTkEntry(master=product_form, placeholder_text="Precio del producto",
                    width=250,
                    font=("Helvetica", 15),
                 )
    precio.grid(row=0, column=2, padx=12, pady=15)

    # CANTIDAD
    cantidad = ctk.CTkEntry(master=product_form, placeholder_text="Cantidad del producto",
                    width=250,
                    font=("Helvetica", 15),
                 )
    cantidad.grid(row=1, column=0, padx=12, pady=15)    
        
    # MEDIDA DEL PRODUCTO
    medidas = ["Tipo de Medida del producto", "Unidades", "Kilogramos", "Gramos", "Miligramos", "Litros", "Mililitros", "Toneladas", "Onzas", "Libras", "Galones", "Metros cúbicos", "Pulgadas cúbicas"]
    
    medidas_entry = ctk.CTkOptionMenu(master=product_form, values=medidas, width=250, font=("Helvetica", 15),)
    medidas_entry.grid(row=1, column=1, padx=0, pady=15) 
    
    # PROVEEDOR
    df = pd.read_csv('data/inventory/suppliers.csv')
    proveedores = ["Proveedor"]
    for proveedor in df.values.tolist():
        proveedores.append(proveedor[0])
    proveedores_entry = ctk.CTkOptionMenu(master=product_form, values=proveedores, width=250, font=("Helvetica", 15),)
    proveedores_entry.grid(row=2, column=0, padx=0, pady=15)
    
    # CANTIDAD
    compra = ctk.CTkEntry(master=product_form, placeholder_text="Precio de compra del producto",
                    width=250,
                    font=("Helvetica", 15),
                 )
    compra.grid(row=1, column=2, padx=12, pady=15)        
    
    submit = ctk.CTkButton(master=product_form, text="Registrar producto", width=250, font=("Helvetica", 15), command=lambda:validate_new_product()).grid(row=7, column=0, padx=30, pady=35)
    # fg_color="red", hover_color="green"