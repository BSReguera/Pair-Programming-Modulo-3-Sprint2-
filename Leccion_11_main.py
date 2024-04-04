#%%
import pandas as pd
from src import Leccion_11_soporte as soporte
from src import query_creacion_bbdd as query
# %%
ventas_df = pd.read_csv('ventas.csv')
productos_df = pd.read_csv('productos.csv', error_bad_lines=False, warn_bad_lines=False)
clientes_df = pd.read_csv('clientes.csv')
#%%
lista_df = [ventas_df, productos_df, clientes_df]
info = soporte.exploracion(lista_df)
# %%
productos_df_limpio = soporte.limpieza_productos(productos_df)
# %%
lista_df2 = [ventas_df, productos_df_limpio, clientes_df]
soporte.transformacion_cabeceras(lista_df2)
# %%
soporte.gestion_nulos(lista_df2)
# %%
df_mergeado = soporte.union(ventas_df, productos_df_limpio, clientes_df)
# %%
df_mergeado
# %%
