# DataFrame

**DataFrame** 是由多种类型的列构成的二维标签数据结构，类似于 Excel 、SQL 表，或 Series 对象构成的字典。DataFrame 是最常用的 Pandas 对象。

DataFrame有多种生成方式，可以使用多个Serial组合生成，可以手动生成，也可以从多种数据源导入（CSV、DB、EXCEL等）。

```python
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

```