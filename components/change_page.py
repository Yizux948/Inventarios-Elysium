import customtkinter as ctk
import tkinter as tk
import matplotlib.pyplot as plt
# pantallas
import inventory.content.welcome as wp
import inventory.content.new_product as pp
import inventory.content.product_list as pls
import inventory.content.new_client as nc
import inventory.content.client_list as cl
import inventory.content.edit_product as ep
import inventory.content.edit_client as ec
import inventory.content.new_supplier as ns
import inventory.content.supplier_list as sl
import inventory.content.edit_supplier as es
import inventory.content.new_sale as nws
import inventory.content.sale_list as sal
import inventory.content.sale_details as sd
# CAMBIAR PAGINA
def new_page(frame, type):
    # asegurate de destruir las graficas para evitar problemas de rendimiento
    plt.close('all')
    for widget in frame.winfo_children():
        widget.destroy()
        
    # AQUI VAN LAS RUTAS DE TODAS LAS PANTALLAS, PERO PRIMERO SE DEBE VACIAR EL FRAME CON delete_frame()
    if(type.strip() == 'Dashboard'):
        wp.welcome_page(frame)
    elif (type.strip() == 'Productos'):
        pp.new_product_form(frame)
    elif (type.strip() == 'Lista de Productos'):
        pls.products_list(frame)     
    elif (type.strip() == 'Clientes'):
        nc.new_client_form(frame)    
    elif (type.strip() == 'Lista de Clientes'):
        cl.clients_list(frame)
    elif (type.strip() == 'Provedores'):
        ns.new_supplier_form(frame)
    elif (type.strip() == 'Lista de Proveedores'):
        sl.suppliers_list(frame)
    elif (type.strip() == 'Ventas'):
        nws.new_sale_form(frame)
    elif (type.strip() == 'Lista de Ventas'):
        sal.sale_list(frame)
        
    
# =============================================================

# CAMBIO DE PAGINA CON PARAMETRO
def new_page_put(frame, type, data):
    # asegurate de destruir las graficas para evitar problemas de rendimiento
    plt.close('all')
    for widget in frame.winfo_children():
        widget.destroy()
    
    # AQUI VAN LAS RUTAS DE TODAS LAS PANTALLAS, PERO PRIMERO SE DEBE VACIAR EL FRAME CON delete_frame()
    if(type.strip() == 'Editar Producto'):
        ep.edit(frame, data)
    elif (type.strip() == 'Editar Cliente'):
        ec.edit(frame, data)
    elif (type.strip() == 'Editar Proveedor'):
        es.edit(frame, data)
    elif (type.strip() == 'Ver Venta'):
        sd.details(frame, data)

# =============================================================

# =============================================================

# CREAR VENTANA TEMPORAL CON PARAMETRO
def temp_page_put(frame, data):
        
    frame.toplevel = ctk.CTkToplevel(frame)
    frame.toplevel.title("Datos de venta")

    
    frame.toplevel.geometry("400x300")
    
    label = ctk.CTkLabel(frame.toplevel, text=data)
    label.pack(pady=20)
    
    close_button = ctk.CTkButton(frame.toplevel, text="Cerrar", command=frame.toplevel.destroy)
    close_button.pack(pady=20)        
    
    # AQUI VAN LAS RUTAS DE TODAS LAS PANTALLAS, PERO PRIMERO SE DEBE VACIAR EL FRAME CON delete_frame()
    # if(type.strip() == 'Editar Producto'):
    #     ep.edit(frame, data)
    # elif (type.strip() == 'Editar Cliente'):
    #     ec.edit(frame, data)
    # elif (type.strip() == 'Editar Proveedor'):
    #     es.edit(frame, data)

# =============================================================

# CERRAR SESIÓN
def close_session(root, app):
    # asegurate de destruir las graficas para evitar problemas de rendimiento
    plt.close('all')    
    app.destroy()
    root.deiconify()