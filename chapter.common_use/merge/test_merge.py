import pandas as pd

# 数据加载
df = pd.read_csv('chapter.common_use/load_data/data.csv')
print(df)

df2 = pd.DataFrame([['AP', 99], ['pb', 100], ['SM', -100],
                   ['SR', 66]], columns=['CLASS_ID', 'VALUE3'])
print(df2)

#LEFT JOIN
df3 = pd.merge(df, df2, how='left', on=['CLASS_ID'])
print(df3)

## RIGHT JOIN
df4 = pd.merge(df, df2, how='right', left_on=[
               'CLASS_ID'], right_on=['CLASS_ID'])
print(df4)

## INNER JOIN
df5 = pd.merge(df, df2, how='inner', left_on=[
               'CLASS_ID'], right_on=['CLASS_ID'])
print(df5)

## OUTER JOIN
df6 = pd.merge(df, df2, how='outer', left_on=[
               'CLASS_ID'], right_on=['CLASS_ID'])
print(df6)
