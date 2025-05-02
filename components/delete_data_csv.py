import pandas as pd
# scripts 
import components.change_page as chp

def delete_csv(filename, frame, destine, id):
    print("Eliminando resgistro")
    # ABRIMOS EL CSV
    df = pd.read_csv('data/inventory/'+filename)

    # ELIMINAMOS EL REGISTRO
    df = df.drop(index=id)

    # REAJUSTAMOS INDICES, NO NECESARIO ESTA VEZ
    # df.reset_index(drop=True, inplace=True)

    # GUARDAMOS LOS CAMBIOS
    df.to_csv('data/inventory/'+filename, index=False)
    
    # VAMOS A LA PANTALLA DESTINO
    chp.new_page(frame, destine)
    