import pandas as pd

# 指数es_class_info
ser_cls = pd.Series(['苹果','铅','螺纹钢','锰硅'], index=['AP','pb','rb','SM'])
print(ser_cls)

# 修改
ser_cls['AP'] = 'APPLE'
print(ser_cls)

# 添加
ser_cls['TC']='动力煤'
print(ser_cls)

# 删除
ser_cls = ser_cls.drop('AP')
ser_cls.drop('SM',inplace=True)
print(ser_cls)