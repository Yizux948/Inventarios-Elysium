import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
#no necesario
# from matplotlib import interactive
# interactive(False)

# scripts
import components.color_palette as cp


def create_bar_chart(root, y, x, rx, ry, W, title, ylabel, xlabel):
    
    # Datos para el gráfico de barras
    # categories = ['A', 'B', 'C', 'D', 'E', 'F', "G"]
    # values = [23, 45, 56, 78, 32, 23, 4]
    categories = x
    values = y
    csfont = {'fontname':'Arial'}
    hfont = {'fontname':'Arial'}
    
    # Colores para las barras
    colors = [cp.COLORS["primary"]]
    value_colors = [cp.COLORS["dark"], cp.COLORS["dark"], cp.COLORS["dark"], cp.COLORS["dark"], cp.COLORS["dark"], cp.COLORS["dark"], cp.COLORS["dark"]]
    
    # Crear la figura y los ejes con tamaño personalizado (ancho x alto en pulgadas)
    fig, ax = plt.subplots(figsize=(W, 3)) # width, height

    # Establecer el color de fondo del gráfico
    fig.set_facecolor(cp.COLORS["light"])

    # Crear el gráfico de barras
    bars = ax.bar(categories, values, color=colors, edgecolor=cp.COLORS["secondary"])

    # Etiquetas y título
    ax.set_xlabel(xlabel, color=cp.COLORS["dark"], **csfont)
    ax.set_ylabel(ylabel, color=cp.COLORS["dark"], **hfont)
    ax.set_title(title, color=cp.COLORS["dark"])

    # ============================
    # Cambiar el color de los valores
    for bar, value, color in zip(bars, values, value_colors):
        ax.annotate(str(value), xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
                    xytext=(0, 3), textcoords='offset points', ha='center', va='bottom', color=color)

    # Cambiar el color de las etiquetas del eje x y del eje y
    ax.tick_params(axis='x', colors=cp.COLORS["primary"])  # Cambiar el color de las etiquetas del eje x
    ax.tick_params(axis='y', colors=cp.COLORS["success"])  # Cambiar el color de las etiquetas del eje y

    # Ajustar los límites del eje y para dar espacio adicional arriba de la barra más alta
    ax.set_ylim(0, max(values) * 1.3)
    
    # Mostrar el gráfico
    plt.tight_layout()

    # Mostrar el gráfico en la ventana de Tkinter
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().place(relx=rx, rely=ry, anchor=tk.N)