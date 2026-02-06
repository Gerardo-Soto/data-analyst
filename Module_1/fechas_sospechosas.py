'''
Objetivo: Medir cuántos registros tienen fechas sospechosas y montos anormalmente altos.

Instrucciones:

Convierte la columna order_date a formato fecha, tratando los errores como valores faltantes.
Usando .sum(), calcula cuántos registros tienen como año 2026 en order_date (un año no transcurrido al guardar los datos).
Usando .sum(), calcula cuántos registros tienen order_date vacía después de la conversión.
Imprime cada conteo por separado con print().
'''

import pandas as pd
df = pd.read_csv("/datasets/everpeak_retail.csv")

# convertir a formato de fecha
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

#calcula cuántos registros tienen como año 2026 en order_date
invalid_year_2026_count = (df["order_date"].dt.year == 2026).sum()
#calcula cuántos registros tienen order_date vacía
missing_order_date_count = (df["order_date"].isna()).sum()

print("order_date año 2026:", invalid_year_2026_count)
print("order_date missing:", missing_order_date_count)