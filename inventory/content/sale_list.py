import sys
sys.path.append("../../components")
import components.color_palette as cp
import components.items as itm
import tkinter as tk
import customtkinter as ctk
import pandas as pd
import os
# scripts
import components.change_page as chp
import components.delete_data_csv as dl_csv
import components.delete_json as dl_json

def sale_list(right_menu_frame):
    
    
    ctk.CTkButton(master=right_menu_frame, 
                  text="Nueva Venta", 
                  font=("Helvetica", 15, "bold"),
                  width=200,
                  height=30,                    # frame_a_vaciar, frame_a_colocar
                  command=lambda:chp.new_page(right_menu_frame, "Ventas")
                  ).place(rely=0.03, relx=0.11, anchor=tk.N)
    
    product_form = ctk.CTkScrollableFrame(right_menu_frame, width=1110, height=420, corner_radius=10, 
                                                    orientation="vertical",
                                                    label_text="Lista de Ventas",
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
    
    # INICIO DE LA TABLA 
    # OBTENEMOS TODAS LAS VENTAS EN FORMATO JSON
    ruta = './data/sales'
    # PASAMOS TODOS LOS JSON A UNA LISTA
    data = [["Fecha de venta", "Hora de venta", "Ver", "Eliminar"],]
    lista_json = [archivo for archivo in os.listdir(ruta) if archivo.endswith('.json')]
    for elemento in lista_json:
        data_splited = elemento.split("T")
        print(data_splited)
        
        # elemento.replace(".json","")
        data.append([data_splited[0],
                     data_splited[1].replace(".json","").replace("_",":"),
                     elemento,
                     elemento
                     ])
    
    # Fuentes personalizadas
    header_font = ("Helvetica", 16, "bold")
    normal_font = ("Helvetica", 16)


    # Crear un frame que contendrá la tabla para el borde del grid
    product_form = ctk.CTkFrame(product_form, corner_radius=10)
    product_form.pack(padx=10, pady=10, fill="both", expand=True)

    # Crear el frame de la tabla dentro del frame principal
    table_frame = ctk.CTkFrame(product_form, corner_radius=10)
    table_frame.pack(padx=10, pady=10, fill="both", expand=True)

    # Definir variables para la paginación
    items_per_page = 10
    global current_page
    current_page = 0
    total_pages = ((len(data)-1) / items_per_page)-1
    # print(total_pages)
    
    # SI SE PULSA EL BOTON DE EDITAR
    def ver_fila(index):
        # chp.temp_page_put(right_menu_frame, data[index][2])
        print(f"Editar fila: {data[index][2]}")
        # frame, nombre a donde vamos, id
        chp.new_page_put(right_menu_frame, "Ver Venta", data[index][2])

    # SI SE PULSA EL BOTON DE BORRAR
    def eliminar_fila(index):
        # Implementa la lógica para eliminar la fila
        print(f"Eliminar fila tuki: {data[index]}")
        # nombre archivo, nombre a donde vamos, id
        dl_json.delete_file_json(f"./data/sales/{data[index][2]}", right_menu_frame, 'Lista de Ventas')


    def crear_celda(master, texto, row, col, es_encabezado=False):
        frame = ctk.CTkFrame(master, corner_radius=0)
        frame.grid(row=row, column=col, padx=1, pady=1, sticky="nsew")
        font = header_font if es_encabezado else normal_font
        if es_encabezado:
            celda = ctk.CTkLabel(frame, text=texto, font=font)
        else:
            if col == 2:  # Columna "Editar"
                celda = ctk.CTkButton(frame, text="Editar", font=font, command=lambda idx=row: ver_fila(idx))
            elif col == 3:  # Columna "Eliminar"
                celda = ctk.CTkButton(frame, text="Eliminar", font=font, command=lambda idx=row: eliminar_fila(idx))
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
        print(total_pages)
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