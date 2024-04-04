#%%
import pandas as pd

# %%
def exploracion (lista):
    """Esta función proporciona una descripción personalizada de un DataFrame,
    incluyendo estadísticas descriptivas y tipos de datos de cada columna.
    
    Argumentos:
    df : DataFrame de Pandas
        El DataFrame para el cual se generará la descripción
        
    La funcion no tiene return pero devuelve varios prints con
    la informacion que necesitamos:
    - describe separados por col numericas y categoricas
    - dtypes por columna
    - shape
    - info
    - total de nulos
    - total de duplicados)"""
       
    for x, df in enumerate(lista):
        print(f"------Dataframe{x}------")
        print("-------Descripción numéricas:---------")
        print(df.describe())
        print("-------Descripción categoricas:---------")
        print(df.describe(include="O"))
        print("------Tipos:---------")
        print(df.dtypes)
        print("------Forma del DataFrame:------")
        print(df.shape)
        print("------Información:---------")
        print(df.info())
        print("------Nulos:---------")
        print(df.isnull().sum())
        print("------Duplicados:---------")
        print(df.duplicated().sum())

def limpieza_productos (dataframe):
    """Explicacion"""

    # Le añadimos un nuevo indice a productos_df para que la primera columna no sea el indice
    cambio_productos = dataframe.reset_index()

    #las cabeceras estan desplazadas a la derecha, las movemos y a la ultima columna le añadiremos el nombre extra
    nuevas_cabeceras = ['ID', 'Nombre_Producto', 'Categoría', "Precio", "Origen", "Descripción", "Extra"]
    # Asignar las nuevas cabeceras al DataFrame
    cambio_productos.columns = nuevas_cabeceras

    # La columna extra es parte de Descripción, las unimos en una nueva
    cambio_productos['Descripcion'] = cambio_productos.apply(lambda row: str(row['Descripción']) + "," + str(row['Extra']), axis=1)
    # Borramos Descripción y Extra
    cambio_productos.drop(columns = ["Descripción", "Extra"], inplace=True)

    return cambio_productos

def transformacion_cabeceras (lista):
    for df in lista:
        df.columns = [col.capitalize() for col in df.columns]
        
def gestion_nulos (lista):
    for df in lista:
        if "Descripcion" in df.columns:
            df["Descripcion"]= df["Descripcion"].fillna("Desconocido")
        elif "Email" in df.columns:
            df['Country'].fillna('Spain', inplace=True)
            df[["Gender", "Email", "City", "Address"]]= df[["Gender", "Email", "City", "Address"]].fillna("Desconocido")

# %%
def union (dataframe1, dataframe2, dataframe3):
    merged_df = pd.merge(dataframe1, dataframe2, left_on="Id_producto", right_on="Id", how='left')
    merged_df = pd.merge(merged_df, dataframe3, left_on='Id_cliente', right_on='Id', how='right')

    merged_df.drop(['Id_x', 'Id_cliente'], axis=1, inplace=True)
    merged_df = merged_df.rename(columns={'Id_y': 'Id_cliente'})
    return merged_df

# %%
