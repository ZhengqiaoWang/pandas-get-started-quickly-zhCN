import pandas as pd

# 数据加载
df = pd.read_csv('chapter.common_use/load_data/data.csv')
print(df)

exchg_cls_count = df.groupby(['EXCHANGE_ID']).size()
print(exchg_cls_count)

exchg_value1_sum = df.groupby(['EXCHANGE_ID'])['VALUE1'].sum()
print(exchg_value1_sum)

df2 = df.sort_values(by=['EXCHANGE_ID', 'VALUE1'], ascending=[True, False])
print(df2)

df3 = df.assign(rn=df.sort_values(by=['VALUE1'], ascending=[False]).groupby(
    ['EXCHANGE_ID']).cumcount()+1).query('rn<3').sort_values(['EXCHANGE_ID', 'rn'])
print(df3)
