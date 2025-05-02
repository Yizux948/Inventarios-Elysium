import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

#no necesario
from matplotlib import interactive
interactive(False)

def create_bar_chart():
    # Datos para el gráfico de barras
    categories = ['A', 'B', 'C', 'D', 'E']
    values = [23, 45, 56, 78, 32]

    # Crear la figura y los ejes
    fig, ax = plt.subplots()

    # Crear el gráfico de barras
    ax.bar(categories, values)

    # Etiquetas y título
    ax.set_xlabel('Categorías')
    ax.set_ylabel('Valores')
    ax.set_title('Gráfico de Barras')

    # Mostrar el gráfico
    plt.tight_layout()

    # Mostrar el gráfico en la ventana de Tkinter
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()


def on_closing():
    plt.close('all')
    root.quit()
    root.destroy()


# Crear la ventana de Tkinter
root = tk.Tk()
root.title("Gráfico de Barras con Tkinter")

# Botón para crear el gráfico
button = tk.Button(root, text="Crear Gráfico de Barras", command=create_bar_chart)
button.pack()

# Manejar el evento de cierre de la ventana
root.protocol("WM_DELETE_WINDOW", on_closing)

# Bucle principal de Tkinter
root.mainloop()
