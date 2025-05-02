import sys
sys.path.append("../../components")
import components.charts as chart
import components.color_palette as cp
import components.items as itm
import tkinter as tk
import customtkinter as ctk
from calendar import monthrange, Day, Month
from datetime import date  # date.today().year, date.today().month


def welcome_page(right_menu_frame):    
    # crear un grafico de barras
    # ventas semanales
    X = ["L", "M", "MR", "J", "V", "S", "D"]
    Y = [1, 2, 3, 0, 5, 6, 7]
    chart.create_bar_chart(
        right_menu_frame, # FRAME  
        Y, # Y
        X, # X
        0.16, # DISTANCIA EN X
        0.0, # DISTANCIA EN Y
        3, # WIDTH 
        "VENTAS SEMANAL", # NOMBRE GRÁFICA
        "Ventas", # Y LABEL
        "Día" # X LABEL        
        )
    
    # ventas mensual
    num_days = monthrange(date.today().year, date.today().month)[1] # obtenemos la cantidad de días del mes 
    # creamos un array con la cantidad de dias del mes 
    month_array = [None] * num_days
    for i in range(num_days):
        month_array[i] = i+1
    
    # X
    X = month_array
    # Y
    Y = month_array
    chart.create_bar_chart(
        right_menu_frame, # FRAME 
        Y, # Y
        X, # X
        0.66, # DISTANCIA EN X
        0.0, # DISTANCIA EN Y
        7.5, # WIDTH 
        "VENTAS MENSUAL", # NOMBRE GRÁFICA
        "Ventas", # Y LABEL
        "Día" # X LABEL
        ) 
    
    # ventas del anual
    X = ["ENE", "FEB", "MAR", "ABR", "MAY", "JUN", "JUL", "AGO", "SEP", "OCT", "NOV", "DIC"]
    Y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    chart.create_bar_chart(
        right_menu_frame, # FRAME  
        Y, # Y
        X, # X
        0.27, # DISTANCIA EN X
        0.44, # DISTANCIA EN Y
        6, # WIDTH 
        "VENTAS ANUAL", # NOMBRE GRÁFICA
        "Ventas", # Y LABEL
        "Día" # X LABEL        
        )
    
    # cards de los contadores
    # ventas diarias   Y - X
    itm.contador_card(right_menu_frame, "Hoy", "100 Ventas", 0.5, 0.6)
    
    # ventas ayer
    itm.contador_card(right_menu_frame, "Ayer", "100 Ventas", 0.5, 0.75)
    
    # productos
    itm.contador_card(right_menu_frame, "Productos", "100 Unidades", 0.5, 0.90)
    
    # categorías
    itm.contador_card(right_menu_frame, "Categorías", "100 Tipos", 0.7, 0.6)
    
    # categorías
    itm.contador_card(right_menu_frame, "Precio del Dólar", "100 Bs", 0.7, 0.75)    