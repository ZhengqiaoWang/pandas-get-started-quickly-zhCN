import pandas as pd

# 数据加载
df = pd.read_csv('chapter.common_use/load_data/data.csv')
print(df)

print(df[['CLASS_ID', 'CLASS_NAME', 'VALUE1']].head(2))
print(df.loc[:, ['CLASS_ID', 'CLASS_NAME', 'VALUE1']].head(2))  # 更推荐使用这类方式

# 将结果赋给原变量
df2 = df.loc[:, ['CLASS_ID', 'CLASS_NAME']]
print(df2)

'''
SELECT CLASS_ID, VALUE1 FROM TABLE1 
WHERE (EXCHANGE_ID = 'ZCE' AND VALUE2 > 0) 
OR (EXCHANGE_ID = 'SFE' AND CLASS_ID IN ('pb','pp'));
'''
df3 = df.loc[((df['EXCHANGE_ID'] == 'ZCE') & (df['VALUE2'] > 0)) | (
    (df['EXCHANGE_ID'] == 'SFE') & (df['CLASS_ID'].isin(['pp', 'pb']))), ['CLASS_ID', 'VALUE1']]
print(df3)
