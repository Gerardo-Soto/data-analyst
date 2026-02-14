'''

Compare the impact between drop and imputation
Objective: Measure how the metric changes when you impute or delete data.

Instructions:

Calculate the mean or average of order_value after deleting rows with missing values using dropna().
Impute the missing values in order_value with the median.
Recalculate the mean and compare it with the original.
'''

import pandas as pd
df = pd.read_csv("/datasets/everpeak_retail.csv")

before = df["order_value"].dropna().mean() # calcula la media original
df["order_value_imputed"] = df["order_value"].fillna(df["order_value"].median()) # tu código para imputar con el valor de la mediana: median()
after = df["order_value_imputed"].mean() # calcula la media después de imputar

print(before)
print(after)

'''output:
10071.564696485622
10071.564696485622

the results are the same because the median is the same as the mean in this case, so imputing with the median does not change the average order value.
'''