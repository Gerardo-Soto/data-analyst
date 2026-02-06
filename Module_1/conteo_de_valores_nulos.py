'''
1.Conteo de valores faltantes por columna
Objetivo: Contar cuántos valores faltantes tiene cada variable de segmentación y ubicación, usando sumas, no porcentajes.

Instrucciones:

Calcula cuántos valores faltantes tienen las columnas payment_method, city y state.
Crea una variable distinta por columna.
Usa print() para mostrar el resultado de cada variable en una línea separada.
Mantén el precódigo para evitar errores en la revisión del ejercicio.
'''
import pandas as pd
df = pd.read_csv("/datasets/everpeak_retail.csv")

#df.info()
payment_missing = df["payment_method"].isna().sum()
city_missing = df["city"].isna().sum()
state_missing = df["state"].isna().sum()

print("payment_method missing:", payment_missing)
print("city missing:", city_missing)
print("state missing:", state_missing)
