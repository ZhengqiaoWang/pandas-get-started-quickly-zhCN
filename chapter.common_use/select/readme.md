# 查找Select

## 列查询

在SQL中，使用您要选择的以逗号分隔的列列表（或* 选择所有列）来完成选择：

```sql
select CLASS_ID, CLASS_NAME, VALUE1 from ES_CLASS_INFO where rownum <=2;
```

使用pandas则会是：

```python
print(df[['CLASS_ID','CLASS_NAME','VALUE1']].head(2))
print(df.loc[:,['CLASS_ID','CLASS_NAME','VALUE1']].head(2)) # 更推荐使用这类方式
```

Pandas这类查找的原理就是在原有的基础上覆盖一个mask，所以这些查找方式不户修改原有记录（除非将结果赋给原变量）。

```python
# 将结果赋给原变量
df2 = df.loc[:,['CLASS_ID','CLASS_NAME']]
print(df2)
```

## 条件查询

如果期望实现以下sql：

```sql
SELECT CLASS_ID, VALUE1 FROM TABLE1 WHERE (EXCHANGE_ID = 'ZCE' AND VALUE2 > 0) OR (EXCHANGE_ID = 'SFE' AND CLASS_ID IN ('pb','pp'));
```

即：在表中查：郑商所的VALUE2>0的和上期所的品种为pb和pp的品种的ID和VALUE1。
对应pandas中可以这么写：

```python
df3 = df.loc[((df['EXCHANGE_ID'] == 'ZCE') & (df['VALUE2'] > 0)) | (
    (df['EXCHANGE_ID'] == 'SFE') & (df['CLASS_ID'].isin(['pp', 'pb']))), ['CLASS_ID', 'VALUE1']]
print(df3)
```

这里使用了`.loc`方法，该方法也是官方比较推荐使用的，不容易产生歧义。
loc的使用方法：
loc[<行判断式>,<列名集合>]
