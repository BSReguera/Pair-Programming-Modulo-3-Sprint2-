#%%
import pandas as pd
from src import Leccion_11_soporte as soporte
from src import query_creacion_bbdd as query
from src import empresa_conexion_soporte as bss
# %%
ventas_df = pd.read_csv('ventas.csv')
productos_df = pd.read_csv('productos.csv', on_bad_lines="warn")
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
bss.creacion_bbdd_tablas(query.query_creacion_bbdd, "AlumnaAdalab", "Empresa_f")
bss.creacion_bbdd_tablas(query.query_tabla_clientes, "AlumnaAdalab")
bss.creacion_bbdd_tablas(query.query_tabla_producto, "AlumnaAdalab")

# %%
datos_tabla_clientes = list(set(zip(clientes_df["Id"].values, clientes_df["First_name"].values, clientes_df["Last_name"].values, clientes_df["Email"].values, clientes_df["Gender"].values, clientes_df["City"].values, clientes_df["Country"].values, clientes_df["Address"].values)))
datos_tabla_productos = list(set(zip(productos_df_limpio["Id"].values, productos_df_limpio["Nombre_producto"].values, productos_df_limpio["Categoría"].values, productos_df_limpio["Precio"].values, productos_df_limpio["Origen"].values, productos_df_limpio["Descripcion"].values)))
#%%
datos_clientes_def = bss.convertir_int(datos_tabla_clientes)
datos_clientes_def2 = bss.convertir_float(datos_clientes_def)
datos_productos_def = bss.convertir_int(datos_tabla_productos)
datos_productos_def2 = bss.convertir_float(datos_productos_def)
#%%
#Error en la insercion: Id clientes duplicados
bss.insertar_datos(query.query_insertar_clientes, "AlumnaAdalab", "Empresa_f", datos_clientes_def2)
bss.insertar_datos(query.query_insertar_producto, "AlumnaAdalab", "Empresa_f", datos_productos_def2)
# %%
clientes_df["Id"].duplicated().sum() #este codigo nos da 0 duplicados