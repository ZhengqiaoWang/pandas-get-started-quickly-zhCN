# Serial

Serial是带标签的一维数组，可存储整数、浮点数、字符串、Python 对象等类型的数据。轴标签统称为 **索引** 。调用 `pd.Series` 函数即可创建 Series。

一个Serial可以看作成一列数据：

```python
ser_cls = pd.Series(['苹果','铅','螺纹钢','锰硅'], index=['AP','pb','rb','SM'])
print(ser_cls)
```

我们可以根据INDEX(标签，这里是品种ID)对数值进行修改

```python
ser_cls['AP']='APPLE'
print(ser_cls)
```

可以添加行（记录）

```python
ser_cls['TC']='动力煤'
print(ser_cls)
```

删除行

```python
ser_cls = ser_cls.drop('AP')
ser_cls.drop('SM',inplace=True)
print(ser_cls)
```

Serial我们一般可以视为

```sql
SELECT CLASS_ID, CLASS_NAME FROM ES_CLASS_INFO;
```

然后做一个以CLASS_ID为KEY，CLASS_NAME为值的MAP(table)。
