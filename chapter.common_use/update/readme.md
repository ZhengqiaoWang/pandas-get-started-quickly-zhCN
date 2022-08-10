# 修改UPDATE

## 修改一个值

我们可以通过loc方法获取一行或多行数据修改其中的一列：

```sql
update table1 set value1 = 3 where rownum = 1;
update table1 set value2 = -100.2 where class_id = 'pb';
```

```python
df.loc[0, 'VALUE1'] = 3  # 修改第一个数值（注意第一行的INDEX为0）
df.loc[df['CLASS_ID'] == 'pb', 'VALUE2'] = -100.2
print(df)
```

## 修改多个值

实际上pandas是默认修改多个值的，上述的例子只不过是因为查询的结果为一行才导致这个问题。

```sql
update table1 set value1 = 4 where exchange_id = 'SFE';
update table1 set value2 = value2 + value1 where exchange_id = 'ZCE';
```

```python
df.loc[df['EXCHANGE_ID'] == 'SFE', 'VALUE1'] = 4
df.loc[df['EXCHANGE_ID'] == 'ZCE', 'VALUE2'] = df['VALUE2'] + df['VALUE1']
print(df)
```

注意ZCE的修改方法，赋值时等号后不再包含条件。因为左侧经过查询后得到了mask，右侧计算时则按照mask进行赋值。
