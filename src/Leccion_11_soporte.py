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
    - total de duplicados"""
       
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
    """Esta función realiza varias operaciones para limpiar y reorganizar el DataFrame de productos.

    Argumentos:
    df : DataFrame de Pandas
        El DataFrame de productos que se limpiará y reorganizará

    Returns:
    DataFrame limpio y reorganizado
    """

    # Añadimos un nuevo indice a productos_df para que la primera columna no sea el indice
    cambio_productos = dataframe.reset_index()

    # Desplazamos las cabeceras, puesto que estan hacia la derecha y a la ultima columna le añadiremos el nombre extra
    nuevas_cabeceras = ['ID', 'Nombre_Producto', 'Categoría', "Precio", "Origen", "Descripción", "Extra"]
    
    # Asignamos las nuevas cabeceras al DataFrame
    cambio_productos.columns = nuevas_cabeceras

    # Unión de columnas: Extra y Descripción
    cambio_productos['Descripcion'] = cambio_productos.apply(lambda row: str(row['Descripción']) + "," + str(row['Extra']), axis=1)
    
    # Borramos Descripción y Extra
    cambio_productos.drop(columns = ["Descripción", "Extra"], inplace=True)

    return cambio_productos

def transformacion_cabeceras (lista):
    """
    Esta función transforma las cabeceras de un conjunto de DataFrames en la lista dada, 
    capitalizando la primera letra de cada palabra en los nombres de las columnas.

    Argumentos:
    lista : list
        Una lista de DataFrames de Pandas cuyas cabeceras serán transformadas.

    La función no devuelve nada directamente. Transforma los nombres de las columnas en cada DataFrame de la lista
    para capitalizar la primera letra de cada palabra."""
    
    for df in lista:
        df.columns = [col.capitalize() for col in df.columns]
        
def gestion_nulos (lista):
    """
    Esta función gestiona los valores nulos en una lista de DataFrames de Pandas.

    Argumentos:
    lista : list
        Una lista de DataFrames de Pandas que serán procesados para gestionar los valores nulos.

    La función itera sobre cada DataFrame en la lista y realiza las siguientes operaciones:
    - Si el DataFrame contiene una columna llamada "Descripcion", rellena los valores nulos en esa columna con "Desconocido".
    - Si el DataFrame contiene una columna llamada "Email", rellena los valores nulos en las columnas "Gender", "Email", "City" y "Address" con "Desconocido". Además, rellena los valores nulos en la columna "Country" con "Spain".

    La función no devuelve nada directamente, pero modifica los DataFrames en la lista proporcionada.
    """
    
    for df in lista:
        if "Descripcion" in df.columns:
            df["Descripcion"]= df["Descripcion"].fillna("Desconocido")
        elif "Email" in df.columns:
            df['Country'].fillna('Spain', inplace=True)
            df[["Gender", "Email", "City", "Address"]]= df[["Gender", "Email", "City", "Address"]].fillna("Desconocido")

# %%
def union (dataframe1, dataframe2, dataframe3):
    """
    Esta función combina los tres DataFrames de Pandas en uno solo utilizando la operación de fusión (merge).

    Argumentos:
    dataframe1 - ventas_df : DataFrame de Pandas
        El primer DataFrame que se fusionará.
    dataframe2 cambios_productos : DataFrame de Pandas
        El segundo DataFrame que se fusionará.
    dataframe3 clientes_df : DataFrame de Pandas
        El tercer DataFrame que se fusionará.

    La función utiliza la operación de fusión (merge) para combinar los DataFrames de la siguiente manera:
    - Fusiona dataframe1 y dataframe2 utilizando la columna 'Id_producto' de dataframe1 y la columna 'Id' de dataframe2.
    - Fusiona el resultado anterior con dataframe3 utilizando la columna 'Id_cliente' del DataFrame resultante y la columna 'Id' de dataframe3.
    - Elimina las columnas 'Id_x' (de dataframe1) y 'Id_cliente' (de dataframe3) del DataFrame resultante.
    - Renombra la columna 'Id_y' (de dataframe2) a 'Id_cliente' en el DataFrame resultante.
    
    Returns:
    DataFrame fusionado
        Un DataFrame que resulta de combinar los tres DataFrames proporcionados.
    """
    merged_df = pd.merge(dataframe1, dataframe2, left_on="Id_producto", right_on="Id", how='left')
    merged_df = pd.merge(merged_df, dataframe3, left_on='Id_cliente', right_on='Id', how='right')

    merged_df.drop(['Id_x', 'Id_cliente'], axis=1, inplace=True)
    merged_df = merged_df.rename(columns={'Id_y': 'Id_cliente'})
    return merged_df

# %%
