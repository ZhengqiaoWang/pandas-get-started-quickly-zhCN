# 加载数据

## CSV

直接读取CSV文件，还可以指定分割符等等

```python
# 数据加载,csv
df = pd.read_csv('chapter.common_use/load_data/data.csv',
                 sep=',', encoding='UTF-8')
print(df)
```

## SQL

可以直接使用符合PYTHON数据库标准的引擎，然后写简单的SQL来实现。

```python
df = pd.read_sql('SELECT * FROM TABLE1', conn)
print(df)
```

## EXCEL

不再说明，有read_excel方法。

使用excel获取数据时，需要提前pip安装插件，由于我们日常使用不多，这里就放个链接：[点击此处](https://baijiahao.baidu.com/s?id=1690909203824706695&wfr=spider&for=pc)
