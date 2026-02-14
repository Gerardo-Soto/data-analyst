# Crear función
def rellenar_ausentes(df, cols_fill):
    # bucle para recorrer columnas
    for column in cols_fill:
        # convertir a numérico
        df[column] = pd.to_numeric(df[column], errors='coerce')
        # tu código aquí: rellenar con promedio usando inplace=True
        mean_column = df[column].mean()
        df[column] = df[column].fillna(mean_column)
    return df

# --------------------------------------------------------------------
# Importar librería y leer datos
import pandas as pd
df = pd.read_csv("/datasets/everpeak_retail.csv")

# observar valores ausentes iniciales
print("Valores ausentes iniciales:")
print(df[["customer_age", "price"]].isna().sum())

# Definir columnas a rellenar
columnas_rellenar = ['customer_age', 'price']

# Aplicar función y observar cambios
df = rellenar_ausentes(df, columnas_rellenar)
print("\nValores ausentes después:")
print(df[["customer_age", "price"]].isna().sum())