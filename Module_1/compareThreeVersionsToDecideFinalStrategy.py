
'''
Objective: Compare three versions of a numeric column to decide on the final strategy.

Instructions:

Taking the numeric column with missing values: customer_age.
Calculate:
the original mean,
the mean imputed using the median,
and the mean imputed using the mean.
Analyze which strategy is most appropriate for the EverPeak–SilverBasket case.
'''

import pandas as pd
df = pd.read_csv("/datasets/everpeak_retail.csv")

before = df["customer_age"].dropna().mean()

# Create "customer_age_med"
df["customer_age_med"] = df["customer_age"].fillna(df["customer_age"].dropna().median())
after_med = df["customer_age_med"].mean() # calculate the mean

# Create "customer_age_mean"
df["customer_age_mean"] = df["customer_age"].fillna(df["customer_age"].dropna().mean())
after_mean = df["customer_age_mean"].mean() # calculate the mean

print(before)
print(after_med)
print(after_mean)

'''output:
43.72869493618773
43.88658146964856
43.728694936187736

The original mean is 43.73, the mean imputed using the median is 43.89, and the mean 
imputed using the mean is 43.73. The mean imputed using the median is higher than 
the original mean, while the mean imputed using the mean is the same as the original 
mean. This suggests that imputing with the median may be more appropriate for this 
dataset, as it may better represent the central tendency of the data without being 
influenced by outliers.'''
