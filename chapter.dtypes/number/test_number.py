import pandas as pd
import numpy as np

df1 = pd.DataFrame([
    [1, 3.1415,'3212','34.2'],
    [2, 312.2,'321','32.12']
],columns=[1,2,3,4])
print(df1)
print(df1.dtypes)
df1.loc[:,3] = pd.to_numeric(df1.loc[:,3])
df1.loc[:,4] = pd.to_numeric(df1.loc[:,4])

print("==============")
print(df1)
print(df1.dtypes)