# 日期时间

## Timestamp

### 构造

Pandas的日期时间类型就是Timestamp类型，其有多种写入形式：

```python
import pandas as pd
import datetime

# Timestamp
dt1 = pd.to_datetime('20100101')
print(dt1)
dt2 = pd.to_datetime(20100101)  # 实际时间为1970-01-01 00:00:00.020100101
print(dt2)
dt3 = pd.to_datetime('2010/1/1')
print(dt3)
dt4 = pd.to_datetime('2010-1-01')
print(dt4)
dt5 = pd.to_datetime('10-01-01')  # 实际时间是2001-10-01，因此这种写法是有问题的
print(dt5)
dt5 = pd.to_datetime('10-01-01', format='%y-%M-%d')  # 这样写就没问题了
print(dt5)
dt6 = pd.to_datetime(datetime.datetime.now())
print(dt6)
dt7 = pd.to_datetime('2020-03-31')
print(dt7)
```

可以看出来，对于一般的格式而言，是可以自适应其日期结构的，但对于一些较为特殊的用法（例如dt5）就必须使用format来指导获取日期了，format的写法与python的Datetime一致（或者说，只有ORACLE是YYYYMMDD，其他大部分数据库和语言都统一的使用%来表示）。

从dt6可以看出来，pandas的timestamp和python自带的datetime是可以互相随意转换的，但相比而言，pandas的datetime使用起来更方便，同时具有更多的功能。

### 方法

单一的timestamp有多个方法（method）来帮助提供信息，这里举了几个例子，分别获取日期的年月日季度周，还判断是否是年月季度的始末，惊喜的是，还可以判断年份是否是闰年。

```python
# Timestamp.??
print(dt1.year)
print(dt1.month)
print(dt1.quarter)
print(dt1.day)
print(dt1.week)
print(dt1.day_of_week)
print(dt1.day_of_year)
print(dt1.day)
print(dt1.days_in_month)  # 所在月天数

# datetime
print(dt1.is_year_start)  # 是否是一年之初
print(dt1.is_month_start)
print(dt1.is_quarter_start)
print(dt6.is_year_start)  # 是否是一年之初
print(dt6.is_month_start)
print(dt7.is_leap_year)  # 20年是闰年
print(dt7.is_month_end)  # 月最后一天
print(dt7.is_quarter_end)  # 季度最后一天
```

## 时间段

一般认为，年，月，日都可以表述成一个时间段，这部分不再细讲。
```python
# Periods
print(pd.Period('2010-01'))
print(dt7.to_period(freq='M'))
```

## 时间序列

我们可以根据需要，获取某个时间段内制定数量制定频率的日期序列：

```python
dt8 = pd.date_range(start='2010-01-01',end='20100102',freq='H') # 注意是左闭右闭区间
print(dt8)
dt9 = pd.date_range(start='2010-01-01',periods=3,freq='H') # 注意是左闭右闭区间
print(dt9)
```

## DateOffset

DateOffset即日期偏移量是相当好用的工具。
在示例里，获取了上一自然天，下一个月的第一个工作日，下一个月的最后一个工作日，往后12小时，往后2周：

```python
print(dt7+pd.offsets.Day(-1))
print(dt7+pd.offsets.BMonthBegin())  # 3月31日的下一个月的第一个工作日
print(dt7+pd.offsets.BMonthEnd())  # 3月31日的下一个月的最后工作日
print(dt7+pd.offsets.Hour(12))
print(dt7+pd.offsets.Week(2))  # 往后两周
```

除上述的使用offsets来解决偏移问题，还有专门的Timedelta、DataOffset等方法可以使用，效果与上述相近，不过用法略有不同。

> Pandas 时间戳的最低单位为纳秒，64 位整数显示的时间跨度约为 584 年，这就是 Timestamp 的界限

## 节假日与工作日

Pandas可以自定义工作日以及工作时间，这一点或许可以与交易日匹配。但此处不再详细说明，现有的偏移量方法问题不大。