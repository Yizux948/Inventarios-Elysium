import sys
sys.path.append("../../components")

import components.items as itm
import tkinter as tk
from tkinter.messagebox import *
from tkinter import simpledialog
import customtkinter as ctk
import pandas as pd
import os
from datetime import datetime
import json
# scripts
import components.change_page as chp
import components.color_palette as cp

    

def details(right_menu_frame, data):   
    
    # OBTENEMOS LA DATA DEL JSON SOLICITADO
    # sale_details = pd.read_json(f'./data/sales/{data}').to_dict()
    with open(f'./data/sales/{data}', 'r', encoding='utf-8') as file:
        sale_details = json.load(file)

    # print(sale_details['cliente'][0])
    ctk.CTkButton(master=right_menu_frame, 
                  text="Lista de ventas",
                  font=("Helvetica", 15, "bold"),
                  width=200,
                  height=30,
                  command=lambda:chp.new_page(right_menu_frame, "Lista de Ventas")
                  ).place(rely=0.03, relx=0.11, anchor=tk.N)
    
    form = ctk.CTkScrollableFrame(right_menu_frame, width=1110, height=420, corner_radius=10, 
                                                    orientation="vertical",
                                                    label_text="Nueva Venta",
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
    
    ctk.CTkLabel(master=form, font=("Helvetica", 18, "bold"), text=f"Datos personales del cliente").grid(row=0, column=0, padx=120, pady=15)
            
    cedula = ctk.CTkLabel(master=form, font=("Helvetica", 16), text=f"Cédula: {sale_details['cliente'][0]['Cédula']}")
    cedula.grid(row=1, column=0, padx=120, pady=15)
    
    nombre = ctk.CTkLabel(master=form, font=("Helvetica", 16), text=f"Nombres Y Apellidos: {sale_details['cliente'][0]['Nombre']} {sale_details['cliente'][0]['Apellidos']}")
    # nombre.grid(row=1, column=1, padx=120, pady=15)

    ctk.CTkLabel(master=form, font=("Helvetica", 18, "bold"), text=f"Detalles de la venta").grid(row=2, column=0, padx=120, pady=15)
    
    monto_total = ctk.CTkLabel(master=form, font=("Helvetica", 16), text=f"Monto total de venta: {sale_details['total']}", anchor="nw")
    monto_total.grid(row=3, column=0, padx=120, pady=15)


    ctk.CTkLabel(master=form, font=("Helvetica", 18, "bold"), text=f"Productos vendidos").grid(row=2, column=0, padx=120, pady=15)



# =====================================================================    
    i = 0
    actual_row = 4
    data = [["Producto", "Precio Unitario", "Cantidad", "Medida"]]
    for producto_actual in sale_details['productos']:
        # sale_details['productos'][i]["Producto"]
        
        data.append([
            sale_details['productos'][i]["Producto"],
            sale_details['productos'][i]["Precio_unitario"],
            sale_details['productos'][i]["Cantidad"],
            sale_details['productos'][i]["Medida"],
            ])
        i += 1
        actual_row += 1
    

    print(data)
    
    # INICIO DE LA TABLA 

    # Fuentes personalizadas
    header_font = ("Helvetica", 16, "bold")
    normal_font = ("Helvetica", 16)


    # Crear un frame que contendrá la tabla para el borde del grid
    product_form = ctk.CTkFrame(form, corner_radius=10)
    product_form.grid(row=0, column=1, rowspan=20, padx=0, pady=15)

    # Crear el frame de la tabla dentro del frame principal
    table_frame = ctk.CTkFrame(product_form, corner_radius=10)
    table_frame.pack(padx=10, pady=10, fill="both", expand=True)

    # Definir variables para la paginación
    items_per_page = 10
    global current_page
    current_page = 0
    total_pages = ((len(data)-1) / items_per_page)-1
    # print(total_pages)


    def crear_celda(master, texto, row, col, es_encabezado=False):
        frame = ctk.CTkFrame(master, corner_radius=0)
        frame.grid(row=row, column=col, padx=1, pady=1, sticky="nsew")
        font = header_font if es_encabezado else normal_font
        if es_encabezado:
            celda = ctk.CTkLabel(frame, text=texto, font=font)
        else:
            celda = ctk.CTkLabel(frame, text=texto, font=font)
        celda.pack(expand=True, fill="both")

    def mostrar_pagina(pagina):
        # Limpiar la tabla
        for widget in table_frame.winfo_children():
            widget.destroy()
        # Mostrar la tabla actualizada
        start_index = pagina * items_per_page + 1
        end_index = start_index + items_per_page
        page_data = [data[0]] + data[start_index:end_index]
        for i, fila in enumerate(page_data):
            for j, valor in enumerate(fila):
                es_encabezado = i == 0  # La primera fila es el encabezado
                crear_celda(table_frame, valor, i, j, es_encabezado)
        # Configurar las columnas para que se expandan
        for i in range(len(data[0])):
            table_frame.grid_columnconfigure(i, weight=1)
        # Configurar las filas para que se expandan
        for i in range(len(page_data)):
            table_frame.grid_rowconfigure(i, weight=1)
        actualizar_botones()

    def actualizar_botones():
        btn_anterior.configure(state=ctk.NORMAL if current_page > 0 else ctk.DISABLED)
        btn_siguiente.configure(state=ctk.NORMAL if current_page < total_pages else ctk.DISABLED)

    def pagina_anterior():
        global current_page
        current_page = current_page - 1
        mostrar_pagina(current_page)

    def pagina_siguiente():
        # print(total_pages)
        global current_page
        current_page = current_page + 1
        mostrar_pagina(current_page)
        # if current_page < total_pages:
        #     mostrar_pagina(current_page + 1)

    # Botones de navegación
    navigation_frame = ctk.CTkFrame(product_form, corner_radius=10)
    navigation_frame.pack(pady=10)

    btn_anterior = ctk.CTkButton(navigation_frame, text="Anterior", command=pagina_anterior)
    btn_anterior.pack(side=tk.LEFT, padx=5)

    btn_siguiente = ctk.CTkButton(navigation_frame, text="Siguiente", command=pagina_siguiente)
    btn_siguiente.pack(side=tk.LEFT, padx=5)

    # Mostrar la primera página
    mostrar_pagina(0)
    # mostrar_pagina(current_page + 1)
    # FIN DE LA TABLA



