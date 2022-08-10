# 添加INSERT

## 添加行

pandas没有专门添加行的方法，添加行可以使用append或concat方式合并两个Dataframe实现，当然，也可以使用loc定位到行尾或新标签修改数据，二者的效率没有进行对比。

```sql
insert into table1 values ('pp','??','SFE',5,-1.23)
```

```python
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
```

## 添加列

添加列的方式则简单了很多，直接使用[]包含不存在的列名并赋值即可。

```python
df['VALUE3'] = 0
print(df)
```
