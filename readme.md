# Pandas 快速介绍与使用实例

## 介绍

Pandas是一个开源的，BSD许可的库，为Python编程语言提供高性能，易于使用的数据结构和数据分析工具。

- 一个快速、高效的DataFrame对象，用于数据操作和综合索引；
- 用于在内存数据结构和不同格式之间读写数据的工具：CSV和文本文件、Microsoft Excel、SQL数据库和快速HDF 5格式；
- 智能数据对齐和丢失数据的综合处理：在计算中获得基于标签的自动对齐，并轻松地将凌乱的数据操作为有序的形式；
- 数据集的灵活调整和旋转；
- 可以从数据结构中插入和删除列，以实现大小可变；
- 通过在强大的引擎中聚合或转换数据，允许对数据集进行拆分应用组合操作;
- 数据集的高性能合并和连接；
- 层次轴索引提供了在低维数据结构中处理高维数据的直观方法；
- 时间序列-功能：日期范围生成和频率转换、移动窗口统计、移动窗口线性回归、日期转换和滞后。甚至在不丢失数据的情况下创建特定领域的时间偏移和加入时间序列；
- 对性能进行了高度优化，用Cython或C编写了关键代码路径。

### 参考资料

中文：[https://www.pypandas.cn/](https://www.pypandas.cn/)

英文：

    快速使用：[https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sql.html#compare-with-sql](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sql.html#compare-with-sql)

    完整文档：[https://pandas.pydata.org/docs/user_guide/index.html#user-guide](https://pandas.pydata.org/docs/user_guide/index.html#user-guide)

### 容器类型

| 维数 | 名称      | 描述                               |
| ---- | --------- | ---------------------------------- |
| 1    | Series    | 带标签的一维同构数组               |
| 2    | DataFrame | 带标签的，大小可变的，二维异构表格 |

DataFrame 是 Series 的容器，Series 则是标量的容器。使用这种方式，可以在容器中以字典的形式插入或删除对象。

#### [Serial](chapter.container/Serial)

#### [DataFrame](chapter.container/DataFrame)

### 数据类型

pandas的底层是numpy，因此类型与numpy.dtype集合一致。

#### [数值](chapter.dtypes/number)

#### 字符串

#### [日期时间](chapter.dtypes/datetime)

日期时间是Pandas的一大杀手锏，可以提供纳秒级的时间管理，除此之外，还人性化的提供了工作日、周、月、季度的偏移方式。

### 常用方法

这里类比SQL来进行说明

#### [查找](chapter.common_use/select)

#### [修改](chapter.common_use/update)

#### [删除](chapter.common_use/delete)

#### [增加](chapter.common_use/insert)

#### [合并](chapter.common_use/merge)

#### [分组](chapter.common_use/groupby)

#### [数据加载](chapter.common_use/load_data)

## 安装

### Python3完整环境安装

使用yum安装

```shell
sudo yum install bzip2-devel xz-devel
```

之后步骤参考《Python3安装手册》

### Pandas安装

使用pip安装

```shell
pip3 install pandas
```
