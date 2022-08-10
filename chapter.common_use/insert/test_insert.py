import pandas as pd

# 数据加载
df = pd.read_csv('chapter.common_use/load_data/data.csv')
print(df)

# append
df = df.append(pd.DataFrame([['a', '??', 'DCE', 5, -1],
                             ['b', '??', 'DCE', 6, -1]
                             ], columns=['CLASS_ID', 'CLASS_NAME', 'EXCHANGE_ID', 'VALUE1', 'VALUE2']), ignore_index=True)
print(df)
# concat
df = pd.concat([df, pd.DataFrame([['c', '??', 'DCE', 5, -1],
                                  ['d', '??', 'DCE', 6, -1]
                                  ], columns=['CLASS_ID', 'CLASS_NAME', 'EXCHANGE_ID', 'VALUE1', 'VALUE2'])], ignore_index=True)
print(df)
#loc，必须要求index为数值且连续，或者为一个新的标签
df.loc[df.last_valid_index()+1] = ['e', '??', 'DCE', 6, -1]
print(df)

df['VALUE3'] = 0
print(df)
