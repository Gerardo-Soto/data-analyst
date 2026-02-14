'''
Docstring for Module_1.missingnessPatternDetectorByGroup
Detect patterns of missingness by group
Objective: Evaluate whether missing city data depends on any business variable.

Instructions:

Calculate the percentage of missing city values by payment_method.
Look at the percentages to decide whether the pattern appears to be MCAR, MAR, or MNAR.
'''
import pandas as pd
df = pd.read_csv("/datasets/everpeak_retail.csv")

# Calculate the percentage of missing city values by payment_method group by payment_method
missing_city_by_pay = df["city"].isna().groupby(df["payment_method"]).mean()
print(missing_city_by_pay)

'''
Output:
payment_method
cash           0.020101
credit_card    0.021517
debit_card     0.021300
paypal         0.015319
Name: city, dtype: float64
Analysis:
The percentages of missing city values by payment method are relatively similar, with values around 2% 
for cash, credit_card, and debit_card, and slightly lower for paypal. This suggests that the missingness 
of city data does not appear to be strongly associated with the payment method, which may indicate that 
the missingness is Missing Completely at Random (MCAR).
'''