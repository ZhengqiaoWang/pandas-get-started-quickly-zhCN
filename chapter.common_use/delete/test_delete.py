import pandas as pd

# 数据加载
df = pd.read_csv('chapter.common_use/load_data/data.csv')
print(df)

df = df.loc[(df['CLASS_ID'] != 'AP'), :]
print(df)
df = df.drop(df[df['EXCHANGE_ID'] == 'SFE'].index)
df.drop(3, inplace=True)
print(df)

# 数据加载
df = pd.read_csv('chapter.common_use/load_data/data.csv')
print(df)

df2 = df.drop(['VALUE1', 'VALUE2'], axis=1)
# drop也可以使用inplace参数drop自身的行或列
print(df2)
