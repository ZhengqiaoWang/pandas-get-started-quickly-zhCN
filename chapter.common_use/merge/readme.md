# 合并MERGE

## LEFT JOIN

```sql
select t.* from table1 left join table2 s on t.class_id = s.class_id
```

```python
df3 = pd.merge(df, df2, how='left', on=['CLASS_ID'])
print(df3)
```

## RIGHT JOIN

```sql
select t.* from table1 right join table2 s on t.class_id = s.class_id
```

```python
df4 = pd.merge(df, df2, how='right', left_on=[
               'CLASS_ID'], right_on=['CLASS_ID'])
print(df4)
```

## INNER JOIN

```sql
select t.* from table1 inner join table2 s on t.class_id = s.class_id
```

```python
df4 = pd.merge(df, df2, how='inner', left_on=[
               'CLASS_ID'], right_on=['CLASS_ID'])
print(df4)
```

## OUTER JOIN

```sql
select t.* from table1 full outer join table2 s on t.class_id = s.class_id
```

```python
df6 = pd.merge(df, df2, how='outer', left_on=[
               'CLASS_ID'], right_on=['CLASS_ID'])
print(df6)
```
