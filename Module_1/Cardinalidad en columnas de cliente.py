'''
Cardinalidad en columnas de cliente
Objetivo: Calcular la cardinalidad de columnas clave para entender si son IDs, categorías o variables poco útiles.

Instrucciones:

Calcula cuántos valores únicos tiene customer_id.
Calcula cuántos valores únicos tiene customer_segment.
Calcula cuántos valores únicos tienen city y state (cada una por separado).
Imprime cada resultado con print(), mostrando el nombre de la columna y su número de valores únicos.
Mantén el precódigo para evitar errores en la revisión del ejercicio.
'''
import pandas as pd
df = pd.read_csv("/datasets/everpeak_retail.csv")

# conteo de cuantos valores únicos tiene cada columna
customer_id_unicos = df["customer_id"].nunique()
payment_unicos =  df["payment_method"].nunique()
city_unicos =  df["city"].nunique()
state_unicos = df["state"].nunique()

print("customer_id nunique:", customer_id_unicos)
print("payment_method nunique:", payment_unicos)
print("city nunique:", city_unicos)
print("state nunique:", state_unicos)

