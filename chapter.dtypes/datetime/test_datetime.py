import pandas as pd
import datetime

# Timestamp
dt1 = pd.to_datetime('20100101')
print(dt1)
dt2 = pd.to_datetime(20100101)  # 实际时间应为1970-01-01 00:00:00.020100101
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

# Periods
print(pd.Period('2010-01'))
print(dt7.to_period(freq='M'))


dt8 = pd.date_range(start='2010-01-01', end='20100102', freq='H')  # 注意是左闭右闭区间
print(dt8)
dt9 = pd.date_range(start='2010-01-01', periods=3, freq='H')  # 注意是左闭右闭区间
print(dt9)

# dateoffset
print(dt7+pd.offsets.Day(-1))
print(dt7+pd.offsets.BMonthBegin())  # 3月31日的下一个月的第一个工作日
print(dt7+pd.offsets.BMonthEnd())  # 3月31日的下一个月的最后工作日
print(dt7+pd.offsets.Hour(12))
print(dt7+pd.offsets.Week(2))  # 往后两周
