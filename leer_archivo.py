import pandas as pd

def leer_archivo():
     #Leer el archivo CSV 
        archivo= 'observatorio-de-obras-urbanas.csv'        

        try: 
            df= pd.read_csv(archivo, sep=",")
            return df
        except FileNotFoundError as e:
            print("Error al ejecutar el archivo", e)
            return False