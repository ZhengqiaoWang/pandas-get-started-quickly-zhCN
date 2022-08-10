import pandas as pd

# 数据加载
df = pd.read_csv('chapter.common_use/load_data/data.csv')
print(df)

df.loc[0, 'VALUE1'] = 3  # 修改第一个数值（注意第一行的INDEX为0）
df.loc[df['CLASS_ID'] == 'pb', 'VALUE2'] = -100.2
print(df)

df.loc[df['EXCHANGE_ID'] == 'SFE', 'VALUE1'] = 4
df.loc[df['EXCHANGE_ID'] == 'ZCE', 'VALUE2'] = df['VALUE2'] + df['VALUE1']
print(df)
