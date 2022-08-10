# 分组GROUPBY

分组与SQL相同

## 分组

```sql
select exchange_id, count(*) from table1
```

```python
exchg_cls_count = df.groupby(['EXCHANGE_ID']).size()
print(exchg_cls_count)
```

## 求和

```sql
select exchange_id, sum(value1) from table1
```

```python
exchg_value1_sum = df.groupby(['EXCHANGE_ID'])['VALUE1'].sum()
print(exchg_value1_sum)
```

## 排序

一般排序：EXCHANGE_ID升序，VALUE1降序

```sql
select * from table1 order by exchange_id, value1 desc;
```

```python
df2 = df.sort_values(by=['EXCHANGE_ID', 'VALUE1'], ascending=[True, False])
print(df2)
```

分组排序

```sql
select * from (
    select t.*, row_number() over(partition by exchange_id order by value1 desc) as rn
    from table1 t
)
where rn < 3
order by exchange_id, rn;
```

```python
df3 = df.assign(rn=df.sort_values(by=['VALUE1'], ascending=[False]).groupby(
    ['EXCHANGE_ID']).cumcount()+1).query('rn<3').sort_values(['EXCHANGE_ID', 'rn'])
print(df3)
```
