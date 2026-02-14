'''

Función para reemplazar Sentinels
Objetivo: : Crear una función básica que reemplace valores centinela por NaN en una columna específica.

Instrucciones:

Comencemos con una función básica que iremos mejorando.

Crea una función reemplazar_sentinels que reciba 2 entradas:
df: el DataFrame a corregir
sentinels: los valores a corregir.
Dentro de la función,
Crea un código para reemplazar los sentinels por NaNs, directamente en la columna "customer_age" del DF.
Regresa el DF corregido.
Después, en valores_erroneos fija los siguientes valores a corregir: -999, 999, 0 y -1.
Aplica la función al DF.
Observa los cambios en la cantidad de valores ausentes presentes en el DF.
'''

def reemplazar_sentinels(df, sentinels, numeric_cols):
    for column in numeric_cols:
        df[column] = df[column].replace(sentinels, pd.NA)
    
    return df

# --------------------------------------------------------------------
# Importar librería y leer datos
import pandas as pd
df = pd.read_csv("/datasets/everpeak_retail.csv")

# observar valores ausentes iniciales
print("Valores ausentes iniciales:")
print(df[["customer_age", "price"]].isna().sum())

# Fijar valores a corregir y columnas
valores_erroneos = [-999, 999, 0, -1]
columnas_numericas = ['customer_age', 'price']

# Aplicar función y observar cambios
df = reemplazar_sentinels(df, valores_erroneos, columnas_numericas)
print("\nValores ausentes después:")
print(df[["customer_age", "price"]].isna().sum())