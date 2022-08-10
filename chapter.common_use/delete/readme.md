# 删除DELETE

## 删除行

一般pandas不采用删除行的方式进行，普遍采用select且覆盖的方式，当然，也可以使用drop行的方式进行。

```sql
delete from table1 where class_id='AP';
delete from table1 where exchange_id='SFE';
```

```python
df = df.loc[(df['CLASS_ID'] != 'AP'), :]
print(df)
df = df.drop(df[df['EXCHANGE_ID'] == 'SFE'].index)
df.drop(3,inplace=True)
print(df)
```

## 删除列

删除列也同样使用drop，不过需要指定列名以及axis=1

```python
df2 = df.drop(['VALUE1', 'VALUE2'], axis=1)
print(df2)
```
