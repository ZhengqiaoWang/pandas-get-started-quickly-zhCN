# Number

Pandas中的数值均使用的是Numpy中的数值，也就包括了INT8、INT32、INT64、UINT*，FLOAT32，FLOAT64这些记录。

需要注意的是，一般情况我们并不需要过于关注数值的类型，因为DataFrame不能显示的指定某列的类型（Serial则可以，且由多个Serial拼成的Datafram是可以的）。同时如果数据源来源于SQL、CSV等文件，则会自动检测。我们更多的只需要关注该数是否是数值即可。

相对应的，就是可以看下面的例子：

```python
import pandas as pd
import numpy as np

df1 = pd.DataFrame([
    [1, 3.1415,'3212','34.2'],
    [2, 312.2,'321','32.12']
],columns=[1,2,3,4])
print(df1)
print(df1.dtypes)
df1.loc[:,3] = pd.to_numeric(df1.loc[:,3])
df1.loc[:,4] = pd.to_numeric(df1.loc[:,4])

print("==============")
print(df1)
print(df1.dtypes)
```

其结果为：
```
   1         2     3      4
0  1    3.1415  3212   34.2
1  2  312.2000   321  32.12
1      int64
2    float64
3     object
4     object
dtype: object
==============
   1         2     3      4
0  1    3.1415  3212  34.20
1  2  312.2000   321  32.12
1      int64
2    float64
3      int64
4    float64
dtype: object
```
