import pandas as pd

# 多个Serial合并
ser1 = pd.Series(['苹果', '铅', '螺纹钢', '锰硅'], index=['AP', 'pb', 'rb', 'SM'])
ser2 = pd.Series(['ZCE', 'SFE', 'SFE', 'SFE'], index=['AP', 'pb', 'rb', 'pp'])
print(ser1, ser2)

df1 = pd.DataFrame({'CLASS_NAME': ser1, 'EXCHANGE_ID': ser2})
print(df1)

# 手动创建DataFrame
df2 = pd.DataFrame([['AP101', 123.1], ['AP102', 234.5], [
                   'CF101', -123.2]], columns=['COMMODITY_ID', 'SETTLE_PRICE'])
print(df2)

# 使用字典或元组创建创建
df3 = pd.DataFrame({('a', 'b'): {('A', 'B'): 1, ('A', 'C'): 2}, ('a', 'a'): {('A', 'C'): 3, ('A', 'B'): 4}, ('a', 'c'): {
                   ('A', 'B'): 5, ('A', 'C'): 6}, ('b', 'a'): {('A', 'C'): 7, ('A', 'B'): 8}, ('b', 'b'): {('A', 'D'): 9, ('A', 'B'): 10}})
print(df3)
