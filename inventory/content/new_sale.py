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

    

def new_sale_form(right_menu_frame):   
    
    # FORMULARIO PARA CREAR NUEVO REGISTRO
    def validate():
        
        fecha_venta = fecha_hora.get()
        # VERIFICAMOS LA FECHA DE VENTA PROPUESTA POR EL USUARIO
        if not fecha_venta:
            showerror("Error", "La fecha de venta es requerida")
            return
        
        print(productos_list.get())
        formato = "%Y-%m-%d %H:%M:%S"
        fecha_hora_ac = datetime.now().strftime(formato)
        print(fecha_hora_ac)
        
        # DEFINIMOS LOS ULTIMOS DATOS ANTES DE ENVIAR
        bill["fecha_registro"] = fecha_hora_ac
        bill["fecha_venta"] = fecha_venta
        
        print(bill)
        
        # CREAMOS EL ARCHIVO JSON
        # CREAREMOS UN ARCHIVO JSON POR CADA VENTA, POR LO TANTO DEBEN TENER FECHA Y HORA COMO NOMBRE
        # df = pd.DataFrame(bill)
        # data_dict = df.to_dict()
        filename = f'{fecha_hora_ac}.json'
        filename = filename.replace(":", "_")
        filename = filename.replace(" ", "T")
        # df.to_json("tuki.json", encoding='utf-8')
        with open(f"./data/sales/{filename}", 'w', encoding='utf-8') as json_file:
            json.dump(bill, json_file, ensure_ascii=False)



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
    
    def contruir_fecha(event):
        # Esta función se ejecutará cada vez que se introduce un caracter en el Entry
        fecha_unformatted = fecha_hora.get()
        if(len(fecha_unformatted) == 2):
            fecha_hora.insert(2, "-")
        elif(len(fecha_unformatted) == 5):
            fecha_hora.insert(5, "-")
        
        if(len(fecha_unformatted) > 10):
            print("no hay mas que agregar")
                
    # FECHA
    fecha_hora = ctk.CTkEntry(master=form, placeholder_text="Fecha de la venta",
                    width=250,
                    font=("Helvetica", 15),
                 )
    fecha_hora.bind("<KeyRelease>", contruir_fecha)
    fecha_hora.grid(row=0, column=0, padx=12, pady=15)
    # CEDULA DEL CLIENTE
    def buscar_cliente(event):
    # Leer el archivo CSV y establecer la columna "Cédula" como índice
        df = pd.read_csv('data/inventory/clients.csv', index_col="Cédula")
        # print(df)
        try:
            # Convertir el valor del Entry a entero si es necesario
            cedula_value = int(cedula.get().strip())
            
            # Utilizar loc para acceder a la fila con el índice ingresado en el Entry
            data_finded = df.loc[cedula_value]

            status_client.configure(text="Cliente encontrado")
            client = data_finded.values.tolist()
            
            # DEFINIMOS LOS DATOS DEL CLIENTE EN EL JSON
            global bill
            bill["cliente"][0]["Cédula"]= cedula_value
            bill["cliente"][0]["Nombre"]= client[0]
            bill["cliente"][0]["Apellidos"]= client[1]
            
            # MOSTRAMOS AL USUARIO LOS DATOS DEL CLIENTE
            global data_client
            data_client.configure(text=f"Cédula: {cedula_value}, Nombres Y Apellidos: {client[0]} {client[1]}")
            
            
        except ValueError:
            status_client.configure(text=f"El valor ingresado '{cedula.get().strip()}' no es un número válido.")
        except KeyError:
            status_client.configure(text=f"El cliente con cédula '{cedula_value}' no se encuentra en el sistema.")
        except Exception as e:
            print(e)
            status_client.configure(text=f"Ha ocurrido un error: {e}")
            
            
    cedula = ctk.CTkEntry(master=form, placeholder_text="Cédula del cliente",
                    width=250,
                    font=("Helvetica", 15),
                 )
    cedula.bind("<KeyRelease>", buscar_cliente)
    cedula.grid(row=1, column=0, padx=12, pady=15)
    status_client = ctk.CTkLabel(master=form, text="no se encuentra cliente")
    status_client.grid(row=2, column=0, padx=0, pady=0)
    # =================================
    # PRODUCTOS
    def agregar_producto(event):
        # print(productos_list.get())
        product = productos_list.get()
        if product == "Productos":
            return
        # LIMPIAMOS LA CADENA ANTES DE DIVIDIRLA
        product = product.replace("Cantidad ", "")
        product = product.replace("Precio: ", "")
        # DIVIMOS LA CADENA
        product_split = product.split("-")
        print(product_split)
        # ORGANIZAMOS EL ARRAY COMO UN OBJETO PARA IDENTIFICAR CADA COSA MAS FACIL
        product_data = {
            "Nombre": product_split[0],
            "Precio": float(product_split[1]),
            "Cantidad": float(product_split[2]),
            "Medida": product_split[3]
        }
        # print(product_split)
        # PEDIMOS AL USUARIO LA CANTIDAD DEL PRODUCTO QUE VA A VENDER
        stock = simpledialog.askstring("Cantidad", "Por favor, introduce la cantidad del producto a vender:")
        # VALIDAMOS SU RESPUESTA
        if stock is not None and stock.isdigit():
            pass
        else:
            showerror(title="Error de datos", message="La cantidad a vender no puede estar en blanco, y solo se permiten números")
        # VERIFICAMOS QUE EL STOCK SOLICITADO ESTA DISPONIBLE
        if float(stock) > product_data["Cantidad"]:
            showwarning(title="No hay stock", message="No cuentas con la suficiente cantidad del producto para realizar la venta")
            return
        # RESTAMOS LA CANTIDAD DISPONIBLE Y LA CANTIDAD A VENDER PARA OBTENER EL RESTANTE
        rest = product_data["Cantidad"] - float(stock) 
        # print(rest)
        # MULTIPLICAMOS LA CANTIDAD A VENDER POR EL PRECIO
        total_product_price = product_data["Precio"] * float(stock)
        # AGREGAMOS EL PRODUCTO AL CARRITO DE COMPRA
        container = ctk.CTkLabel(master=puchrase_cart, fg_color=cp.COLORS["light"], text_color=cp.COLORS["dark"], width=610, height=20, corner_radius=5, font=("Helvetica", 15), text=f"{product_data["Nombre"]} - Precio: {total_product_price} - Cantidad a vender: {stock} -{product_data["Medida"]}")
        container.pack(pady=5, anchor=tk.W)
        # ACTUALIZAMOS EL PRECIO TOTAL DE LA VENTA
        global total_cart_price
        total_cart_price += total_product_price
        total_price.configure(text=f"Total a cancelar: {total_cart_price}")
        # AGREGAMOS EL NUEVO PRODUCTO AL JSON
        global bill
        # bill["productos"][0]['producto']
        bill["productos"].append({
            "Producto":product_data["Nombre"],
            "Precio_total":total_product_price,
            "Precio_unitario":product_data["Precio"],
            "Cantidad":stock,
            "Medida":product_data["Medida"],
            # "fecha_registro": datetime.now(),
        })
        bill["total"] = total_cart_price
        print(bill)
        # ESTOY PENSANDO QUE CUANDO SE GENERE EL BOTON DE ELIMINAR TENGA EL ID DEL CONTADOR DONDE VA EL JSON,
        # PUEDE OBTENERSE CON UN LEN Y ENTONCES ELIMNAR LA POSICION DEL ARRAY, POR LO TANTO EL BOTON TIENE COMO
        # PARAMETRO EL ID
        # ESTO ES UNA IDEA, NO SE SI SEA LA MEJOR FORMA DE HACERLO
        
        
    df = pd.read_csv('data/inventory/products.csv')
    productos = ["Productos"]
    for producto in df.values.tolist():
        # CONSTRUIMOS LA ESTRUCTURA DEL PRODUCTO PARA EL CLIENTE
        productos.append(f"{producto[0]} - Precio: {producto[2]} - Cantidad {producto[4]} -{producto[5]}")
    productos_list = ctk.CTkOptionMenu(master=form, values=productos, command=agregar_producto, width=250, font=("Helvetica", 15))
    productos_list.grid(row=3, column=0, padx=0, pady=15)
    
    # MOSTRAMOS DATOS DEL CLIENTE
    global data_client
    data_client = ctk.CTkLabel(master=form, text="Esperando cédula del cliente...", width=610, font=("Helvetica", 15,"bold"),)
    data_client.grid(row=0, column=1, padx=0)    
    
    # CARRITO DE COMPRAS    
    puchrase_cart = ctk.CTkScrollableFrame(master=form, width=610, height=200, corner_radius=10, 
                                                    orientation="vertical",
                                                    label_text="Carrito de compras",
                                                    # label_fg_color="blue",
                                                    label_text_color="white",
                                                    label_font=("Helvetica", 18),
                                                    label_anchor = "center",
                                                    # fg_color=cp.COLORS["light"]
                                                    )
    puchrase_cart.grid(row=1, column=1, rowspan=10, padx=100, pady=5)
    
    # MONTO TOTAL A PAGAR
    global total_cart_price
    total_cart_price = 0
    total_price = ctk.CTkLabel(master=form, text=f"Total a pagar: {total_cart_price}", width=610, font=("Helvetica", 15),)
    total_price.grid(row=11, column=1, padx=0, pady=5)
    
    global bill
    bill = {
        "productos": [
        # {
        # "producto":"jabon",
        # "precio":"1",
        # "cantidad":"12"
        # }, {
        # "producto":"secadora",
        # "precio":"1",
        # "cantidad":"12"            
        # }
        ],
        "cliente": [
            {
            "Cédula":"",
            "Nombre":"",
            "Apellidos":"",
            }
        ],
        "total": 0,
        "fecha_registro": "",
        "fecha_venta": ""
    }
    # print(bill["productos"][0]['producto'])
    
    submit = ctk.CTkButton(master=form, text="Realizar venta", width=250, font=("Helvetica", 15), command=lambda:validate()).grid(row=7, column=0, padx=30, pady=35)