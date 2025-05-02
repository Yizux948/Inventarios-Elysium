import pandas as pd
import os
# scripts 
import components.change_page as chp

def delete_file_json(filename, frame, destine):
    print("Eliminando archivo")
    # ELIMINAMOS EL ARCHIVO
    # Verifica si el archivo existe antes de intentar eliminarlo
    # LA RUTA DEBE ESTAR COMPLETA, NO DEBE IR SOLO EL NOMBRE DEL ARCHIVO
    if os.path.exists(filename):
        os.remove(filename)
        print(f"El archivo {filename} ha sido eliminado correctamente.")
    else:
        print(f"El archivo {filename} no existe.")
    
    # VAMOS A LA PANTALLA DESTINO
    chp.new_page(frame, destine)