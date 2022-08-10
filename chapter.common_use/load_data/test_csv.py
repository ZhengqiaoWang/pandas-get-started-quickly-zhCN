import pandas as pd

# 数据加载,csv
df = pd.read_csv('chapter.common_use/load_data/data.csv',
                 sep=',', encoding='UTF-8')
print(df)
