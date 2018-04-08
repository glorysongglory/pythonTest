import pandas as pd
from pandas import Series, DataFrame

print
'用一维数组生成Series'
x = Series([1, 2, 3, 4])
print
x
'''
0    1
1    2
2    3
3    4
'''
print
x.values  # [1 2 3 4]
# 默认标签为0到3的序号
print
x.index  # RangeIndex(start=0, stop=4, step=1)

print
'指定Series的index'  # 可将index理解为行索引
x = Series([1, 2, 3, 4], index=['a', 'b', 'd', 'c'])
print
x
'''
a    1
b    2
d    3
c    4
'''
print
x.index  # Index([u'a', u'b', u'd', u'c'], dtype='object')
print
x['a']  # 通过行索引来取得元素值：1
x['d'] = 6  # 通过行索引来赋值
print
x[['c', 'a', 'd']]  # 类似于numpy的花式索引
'''
c    4
a    1
d    6
'''
print
x[x > 2]  # 类似于numpy的布尔索引
'''
d    6
c    4
'''
print
'b' in x  # 类似于字典的使用：是否存在该索引：True
print
'e' in x  # False

print
'使用字典来生成Series'
data = {'a': 1, 'b': 2, 'd': 3, 'c': 4}
x = Series(data)
print
x
'''
a    1
b    2
c    4
d    3
'''
print
'使用字典生成Series,并指定额外的index，不匹配的索引部分数据为NaN。'
exindex = ['a', 'b', 'c', 'e']
y = Series(data, index=exindex)  # 类似替换索引
print
y
'''
a    1.0
b    2.0
c    4.0
e    NaN
'''
print
'Series相加，相同行索引相加，不同行索引则数值为NaN'
print
x + y
'''
a    2.0
b    4.0
c    8.0
d    NaN
e    NaN
'''
print
'指定Series/索引的名字'
y.name = 'weight of letters'
y.index.name = 'letter'
print
y
'''
letter
a    1.0
b    2.0
c    4.0
e    NaN
Name: weight of letters, dtype: float64
'''
print
'替换index'
y.index = ['a', 'b', 'c', 'f']
print
y  # 不匹配的索引部分数据为NaN
'''
a    1.0
b    2.0
c    4.0
f    NaN
Name: weight of letters, dtype: float64
'''

print
'使用字典生成DataFrame，key为列名字。'
data = {'state': ['ok', 'ok', 'good', 'bad'],
        'year': [2000, 2001, 2002, 2003],
        'pop': [3.7, 3.6, 2.4, 0.9]}
print
DataFrame(data)  # 行索引index默认
'''
   pop state  year
0  3.7    ok  2000
1  3.6    ok  2001
2  2.4  good  2002
3  0.9   bad  2003
'''
print
DataFrame(data, columns=['year', 'state', 'pop', 'debt'])  # 指定列顺序,不匹配的列为NaN
'''
   year state  pop
0  2000    ok  3.7
1  2001    ok  3.6
2  2002  good  2.4
3  2003   bad  0.9
'''

print
'指定行索引index'
x = DataFrame(data,
              columns=['year', 'state', 'pop', 'debt'],
              index=['one', 'two', 'three', 'four'])
print
x
'''
       year state  pop debt
one    2000    ok  3.7  NaN
two    2001    ok  3.6  NaN
three  2002  good  2.4  NaN
four   2003   bad  0.9  NaN
'''
import numpy

print
'DataFrame元素的索引与修改'
print
x['state']  # 返回一个名为state的Series
'''
one        ok
two        ok
three    good
four      bad
Name: state, dtype: object
'''
print
x.state  # 可直接用.进行列索引
print
x.ix['three']  # 用.ix[]来区分[]进行行索引
'''
year     2002
state    good
pop       2.4
debt      NaN
Name: three, dtype: object
'''
x['debt'] = 16.5  # 修改一整列数据
print
x
'''
       year state  pop  debt
one    2000    ok  3.7  16.5
two    2001    ok  3.6  16.5
three  2002  good  2.4  16.5
four   2003   bad  0.9  16.5
'''
x.debt = numpy.arange(4)  # 用numpy数组修改元素
print
x
'''
       year state  pop  debt
one    2000    ok  3.7     0
two    2001    ok  3.6     1
three  2002  good  2.4     2
four   2003   bad  0.9     3
'''
print
'用Series修改元素，没有指定的默认数据用NaN'
val = Series([-1.2, -1.5, -1.7, 0], index=['one', 'two', 'five', 'six'])
x.debt = val  # DataFrame的行索引不变
print
x
'''
       year state  pop  debt
one    2000    ok  3.7  -1.2
two    2001    ok  3.6  -1.5
three  2002  good  2.4   NaN
four   2003   bad  0.9   NaN
'''
print
'给DataFrame添加新列'
x['gain'] = (x.debt > 0)  # 如果debt大于0为True
print
x
'''
       year state  pop  debt   gain
one    2000    ok  3.7  -1.2  False
two    2001    ok  3.6  -1.5  False
three  2002  good  2.4   NaN  False
four   2003   bad  0.9   NaN  False
'''
print
x.columns
# Index([u'year', u'state', u'pop', u'debt', u'gain'], dtype='object')
print

print
'DataFrame转置'
print
x.T
'''
DataFrame转置
         one    two  three   four
year    2000   2001   2002   2003
state     ok     ok   good    bad
pop      3.7    3.6    2.4    0.9
debt    -1.2   -1.5    NaN    NaN
gain   False  False  False  False
'''

print
'使用切片初始化数据,未被匹配的数据为NaN'
pdata = {'state': x['state'][0:3], 'pop': x['pop'][0:2]}
y = DataFrame(pdata)
print
y
'''
       pop state
one    3.7    ok
three  NaN  good
two    3.6    ok
'''

print
'指定索引和列的名称'
# 与Series的index.name相区分
y.index.name = '序号'
y.columns.name = '信息'
print
y
'''
信息 pop state
序号
one    3.7    ok
three  NaN  good
two    3.6    ok
'''
print
y.values
'''
[[3.7 'ok']
 [nan 'good']
 [3.6 'ok']]
'''

from pandas import Index

print
'获取Index对象'
x = Series(range(3), index=['a', 'b', 'c'])
index = x.index
print
index
# Index([u'a', u'b', u'c'], dtype='object')
print
index[0:2]
# Index([u'a', u'b'], dtype='object')
try:
    index[0] = 'd'
except:
    print
    "Index is immutable"

print
'构造/使用Index对象'
index = Index(numpy.arange(3))
obj2 = Series([1.5, -2.5, 0], index=index)
print
obj2
'''
0    1.5
1   -2.5
2    0.0
dtype: float64
'''
print
obj2.index is index  # True

print
'判断列/行索引是否存在'
data = {'pop': {2.4, 2.9},
        'year': {2001, 2002}}
x = DataFrame(data)
print
x
'''
          pop          year
0  {2.4, 2.9}  {2001, 2002}
1  {2.4, 2.9}  {2001, 2002}
'''
print
'pop' in x.columns  # True
print
1 in x.index  # True

print
'重新指定索引及NaN填充值'
x = Series([4, 7, 5], index=['a', 'b', 'c'])
y = x.reindex(['a', 'b', 'c', 'd'])
print
y
'''
a    4.0
b    7.0
c    5.0
d    NaN
dtype: float64
'''
print
x.reindex(['a', 'b', 'c', 'd'], fill_value=0)  # 指定不存在元素NaN的默认值
'''
a    4
b    7
c    5
d    0
dtype: int64
'''

print
'重新指定索引并指定填充NaN的方法'
x = Series(['blue', 'purple'], index=[0, 2])
print
x.reindex(range(4), method='ffill')
'''
0      blue
1      blue
2    purple
3    purple
dtype: object
'''

print
'对DataFrame重新指定行/列索引'
x = DataFrame(numpy.arange(9).reshape(3, 3),
              index=['a', 'c', 'd'],
              columns=['A', 'B', 'C'])
print
x
'''
   A  B  C
a  0  1  2
c  3  4  5
d  6  7  8
'''
x = x.reindex(['a', 'b', 'c', 'd'], method='bfill')
print
x
'''
   A  B  C
a  0  1  2
b  3  4  5
c  3  4  5
d  6  7  8
'''
print
'重新指定column'
states = ['A', 'B', 'C', 'D']
x = x.reindex(columns=states, fill_value=0)
print
x
'''
   A  B  C  D
a  0  1  2  0
b  3  4  5  0
d  6  7  8  0
c  3  4  5  0
'''
print
x.ix[['a', 'b', 'd', 'c'], states]
'''
   A  B  C  D
a  0  1  2  0
b  3  4  5  0
d  6  7  8  0
c  3  4  5  0
'''

print
'Series根据行索引删除行'
x = Series(numpy.arange(4), index=['a', 'b', 'c', 'd'])
print
x.drop('c')
'''
a    0
b    1
d    3
dtype: int32
'''
print
x.drop(['a', 'b'])  # 花式删除
'''
c    2
d    3
dtype: int32
'''

print
'DataFrame根据索引行/列删除行/列'
x = DataFrame(numpy.arange(16).reshape((4, 4)),
              index=['a', 'b', 'c', 'd'],
              columns=['A', 'B', 'C', 'D'])
print
x
'''
    A   B   C   D
a   0   1   2   3
b   4   5   6   7
c   8   9  10  11
d  12  13  14  15
'''
print
x.drop(['A', 'B'], axis=1)  # 在列的维度上删除AB两行
'''
    C   D
a   2   3
b   6   7
c  10  11
d  14  15
'''
print
x.drop('a', axis=0)  # 在行的维度上删除
'''
    A   B   C   D
b   4   5   6   7
c   8   9  10  11
d  12  13  14  15
'''
print
x.drop(['a', 'b'], axis=0)
'''
  A   B   C   D
c   8   9  10  11
d  12  13  14  15
'''

print
'Series的数组索引/字典索引'
x = Series(numpy.arange(4), index=['a', 'b', 'c', 'd'])
print
x['b']  # 1 像字典一样索引
print
x[1]  # 1  像数组一样索引
print
x[[1, 3]]  # 花式索引
'''
b    1
d    3
dtype: int32
'''
print
x[x < 2]  # 布尔索引
'''
a    0
b    1
dtype: int32
'''
print
'Series的数组切片'
print
x['a':'c']  # 闭区间，索引顺序须为前后
'''
a    0
b    1
c    2
'''
x['a':'c'] = 5
print
x
'''
a    5
b    5
c    5
d    3
'''

print
'DataFrame的索引'
data = DataFrame(numpy.arange(16).reshape((4, 4)),
                 index=['a', 'b', 'c', 'd'],
                 columns=['A', 'B', 'C', 'D'])
print
data
'''
    A   B   C   D
a   0   1   2   3
b   4   5   6   7
c   8   9  10  11
d  12  13  14  15
'''
print
data['A']  # 打印列
'''
a     0
b     4
c     8
d    12
Name: A, dtype: int32
'''
print
data[['A', 'B']]  # 花式索引
'''
    A   B
a   0   1
b   4   5
c   8   9
d  12  13
'''
print
data[:2]  # 切片索引,选择行
'''
   A  B  C  D
a  0  1  2  3
b  4  5  6  7
'''
print
data.ix[:2, ['A', 'B']]  # 指定行和列索引
'''
   A  B
a  0  1
b  4  5
'''
print
data.ix[['a', 'b'], [3, 0, 1]]  # 行:字典索引，列:数组索引
'''
   D  A  B
a  3  0  1
b  7  4  5
'''
print
data.ix[2]  # 打印第2行（从0开始）
'''
A     8
B     9
C    10
D    11
'''
print
data.ix[:'b', 'A']  # 行从开始到b，第A列。
'''
a    0
b    4
Name: A, dtype: int32
'''
print
'根据条件选择'
print
data
'''
    A   B   C   D
a   0   1   2   3
b   4   5   6   7
c   8   9  10  11
d  12  13  14  15
'''
print
data[data.A > 5]  # 根据条件选择行
'''
    A   B   C   D
c   8   9  10  11
d  12  13  14  15
'''
print
data < 5  # 打印True或者False
'''
       A      B      C      D
a   True   True   True   True
b   True  False  False  False
c  False  False  False  False
d  False  False  False  False
'''
data[data < 5] = 0  # 条件索引
print
data
'''
    A   B   C   D
a   0   0   0   0
b   0   5   6   7
c   8   9  10  11
d  12  13  14  15
'''

print
'DataFrame算术:不重叠部分为NaN,重叠部分元素运算'
x = DataFrame(numpy.arange(9.).reshape((3, 3)),
              columns=['A', 'B', 'C'],
              index=['a', 'b', 'c'])
y = DataFrame(numpy.arange(12).reshape((4, 3)),
              columns=['A', 'B', 'C'],
              index=['a', 'b', 'c', 'd'])
print
x
print
y
print
x + y
'''
      A     B     C
a   0.0   2.0   4.0
b   6.0   8.0  10.0
c  12.0  14.0  16.0
d   NaN   NaN   NaN
'''
print
'对x/y的不重叠部分填充，不是对结果NaN填充'
print
x.add(y, fill_value=0)  # x不变化
'''

      A     B     C
a   0.0   2.0   4.0
b   6.0   8.0  10.0
c  12.0  14.0  16.0
d   9.0  10.0  11.0
'''

print
'DataFrame与Series运算:行运算'
frame = DataFrame(numpy.arange(9).reshape((3, 3)),
                  columns=['A', 'B', 'C'],
                  index=['a', 'b', 'c'])
series = frame.ix[0]
print
frame
'''
   A  B  C
a  0  1  2
b  3  4  5
c  6  7  8
'''
print
series
'''
A    0
B    1
C    2
'''
print
frame - series  # 按行运算
'''
   A  B  C
a  0  0  0
b  3  3  3
c  6  6  6
'''
series2 = Series(range(4), index=['A', 'B', 'C', 'D'])
print
frame + series2  # 按行运算：缺失列则为NaN
'''
   A  B   C   D
a  0  2   4 NaN
b  3  5   7 NaN
c  6  8  10 NaN
'''
series3 = frame.A
print
series3
'''
a    0
b    3
c    6
'''
print
frame.sub(series3, axis=0)  # 按列运算
'''
   A  B  C
a  0  1  2
b  0  1  2
c  0  1  2
'''

print
'numpy函数在Series/DataFrame的应用'
frame = DataFrame(numpy.arange(9).reshape(3, 3),
                  columns=['A', 'B', 'C'],
                  index=['a', 'b', 'c'])
print
frame
'''
   A  B  C
a  0  1  2
b  3  4  5
c  6  7  8
'''
print
numpy.square(frame)
'''
    A   B   C
a   0   1   4
b   9  16  25
c  36  49  64
'''

series = frame.A
print
series
'''
a    0
b    3
c    6
'''
print
numpy.square(series)
'''
a     0
b     9
c    36
'''

print
'lambda(匿名函数)以及应用'
print
frame
'''

   A  B  C
a  0  1  2
b  3  4  5
c  6  7  8
'''
print
frame.max()
'''
A    6
B    7
C    8
'''
f = lambda x: x.max() - x.min()
print
frame.apply(f)  # 作用到每一列
'''
A    6
B    6
C    6
'''
print
frame.apply(f, axis=1)  # 作用到每一行
'''
a    2
b    2
c    2
'''


def f(x):  # Series的元素的类型为Series
    return Series([x.min(), x.max()], index=['min', 'max'])


print
frame.apply(f)
'''
     A  B  C
min  0  1  2
max  6  7  8
'''

print
'applymap和map：作用到每一个元素'
_format = lambda x: '%.2f' % x
print
frame.applymap(_format)  # 针对DataFrame
'''
      A     B     C
a  0.00  1.00  2.00
b  3.00  4.00  5.00
c  6.00  7.00  8.00
'''
print
frame['A'].map(_format)  # 针对Series
'''
a    0.00
b    3.00
c    6.00
Name: A, dtype: object
'''

print
'Series排序'
x = Series(range(4), index=['b', 'a', 'c', 'd'])
print
x.sort_index()  # Series按索引排序
'''
a    1
b    0
c    2
d    3
'''
print
x.sort_values()  # Series按值排序
'''
b    0
a    1
c    2
d    3
'''

print
'DataFrame按索引排序'
frame = DataFrame(numpy.arange(8).reshape((2, 4)),
                  index=['b', 'a'],
                  columns=list('ABDC'))
print
frame
'''
   A  B  D  C
b  0  1  2  3
a  4  5  6  7
'''
print
frame.sort_index()  # 根据行索引来排序
'''
   A  B  D  C
a  4  5  6  7
b  0  1  2  3
'''
print
frame.sort_index(axis=1)  # 根据列索引来排序
'''
   A  B  C  D
b  0  1  3  2
a  4  5  7  6
'''
print
frame.sort_index(axis=1, ascending=False)  # 设置降序排序
'''
   D  C  B  A
b  2  3  1  0
a  6  7  5  4
'''
print
'DataFrame按列的值排序'
frame = DataFrame({'b': [4, 7, -3, 2], 'a': [0, 1, 0, 1]})
print
frame
'''
   a  b
0  0  4
1  1  7
2  0 -3
3  1  2
'''
print
frame.sort_values(by='b')  # 指定b这列的值进行排序
'''
   a  b
2  0 -3
3  1  2
0  0  4
1  1  7
'''
print
frame.sort_values(by=['a', 'b'])  # 先a后b进行列的值排序
'''
   a  b
2  0 -3
0  0  4
3  1  2
1  1  7
'''
print

print
'rank：默认升序，排名值从1开始'
obj = Series([4, 2, 0, 4], index=['a', 'b', 'c', 'd'])
# 以值从小到大来赋排名值：c:0(1) b:2(2) a:4(3) d:4(4)
print
obj.rank()
'''
a    3.5  求平均值(4+3)/2
b    2.0
c    1.0
d    3.5
'''
print
obj.rank(method='first')  # 按出现顺序排名，不求平均值。
'''
a    3.0
b    2.0
c    1.0
d    4.0
'''
print
obj.rank(ascending=False, method='max')  # 逆序，并取排名值最大值。所以-5的rank是7
# a:4(1) d:4(2) b:2(3) c:0(4)
'''
dtype: float64
a    2.0
b    3.0
c    4.0
d    2.0
'''
frame = DataFrame({'b': [4.3, 7, -3, 2],
                   'a': [0, 1, 0, 1],
                   'c': [-2, 5, 8, -2.5]})
print
frame
'''
   a    b    c
0  0  4.3 -2.0
1  1  7.0  5.0
2  0 -3.0  8.0
3  1  2.0 -2.5
'''
print
frame.rank(axis=1)  # 按行进行排名，默认升序
'''
     a    b    c
0  2.0  3.0  1.0
1  1.0  3.0  2.0
2  2.0  1.0  3.0
3  2.0  3.0  1.0
'''

print
'重复索引:进行两层索引'
obj = Series([0, 1, 2, 3, 4], index=['a', 'a', 'b', 'b', 'c'])
print
obj.index.is_unique  # 判断是非有重复索引
# False
print
obj['a'][0]
# 0
print
obj.a[1]
# 1
df = DataFrame(numpy.arange(12).reshape(4, 3), index=['a', 'a', 'b', 'b'])
print
df
'''
   0   1   2
a  0   1   2
a  3   4   5
b  6   7   8
b  9  10  11
'''
print
df.ix['b'].ix[0]  # 两次行索引
'''
0    6
1    7
2    8
Name: b, dtype: int32
'''
print
df.ix['b'].ix[1]
'''
0     9
1    10
2    11
Name: b, dtype: int32
'''

print
'求和'
df = DataFrame([[1, numpy.nan], [7, 4], [numpy.nan, numpy.nan], [0, 1]],
               index=['a', 'b', 'c', 'd'],
               columns=['one', 'two'])
print
df
'''
   one  two
a  1.0  NaN
b  7.0  4.0
c  NaN  NaN
d  0.0  1.0
'''
print
df.sum()  # 按列求和
# 排除缺失值，skipna默认值为True
'''
one    8.0
two    5.0
dtype: float64
'''
print
df.sum(skipna=False)
'''
one   NaN
two   NaN
'''
print
df.sum(axis=1)  # 按行求和
'''
a     1.0
b    11.0
c     0.0
d     1.0
dtype: float64
'''

print
'求平均数'
print
df.mean(axis=1, skipna=False)
'''
a    NaN
b    5.5
c    NaN
d    0.5
'''
print
df.mean(axis=1)
'''
a    1.0
b    5.5
c    NaN
d    0.5
'''

print
'其它函数'
print
df
'''
   one  two
a  1.0  NaN
b  7.0  4.0
c  NaN  NaN
d  0.0  1.0
'''
print
df.idxmax()  # 计算每一列最大值的索引
'''
one    b
two    b
'''
print
df.cumsum()  # 每一列的累加和
'''
   one  two
a  1.0  NaN
b  8.0  4.0
c  NaN  NaN
d  8.0  5.0
'''
print
df.describe()  # 对DataFrame每列计算汇总统计
'''
            one      two
count  3.000000  2.00000
mean   2.666667  2.50000
std    3.785939  2.12132
min    0.000000  1.00000
25%         NaN      NaN
50%         NaN      NaN
75%         NaN      NaN
max    7.000000  4.00000
'''
obj = Series([2, 4, 8, 4], index=['a', 'a', 'b', 'c'])
print
obj.describe()  # 对Series计算汇总统计
'''
count    4.000000
mean     4.500000
std      2.516611
min      2.000000
25%      3.500000
50%      4.000000
75%      5.000000
max      8.000000
dtype: float64
'''

print
'去重'
obj = Series(['c', 'a', 'd', 'b', 'b', 'c'])
print
obj.unique()
print
obj.value_counts()
print

print
'判断元素存在'
mask = obj.isin(['b', 'c'])
print
mask
print
obj[mask]  # 只打印元素b和c
data = DataFrame({'Qu1': [1, 3, 4, 3, 4],
                  'Qu2': [2, 3, 1, 2, 3],
                  'Qu3': [1, 5, 2, 4, 4]})
print
data
print
data.apply(pd.value_counts).fillna(0)
# 计算每列中各个数字出现的次数，缺失值为0
print
data.apply(pd.value_counts, axis=1).fillna(0)
# 计算每行中各个数字出现的次数，缺失值为0

print
'作为null处理的值'
string_data = Series(['a', 'b', numpy.nan, 'd'])
print
string_data
'''
0      a
1      b
2    NaN
3      d
'''
print
string_data.isnull()
'''
0    False
1    False
2     True
3    False
'''
string_data[0] = None
print
string_data
'''
0    None
1       b
2     NaN
3       d
'''
# None也被当作NA处理
print
string_data.isnull()
'''
0     True
1    False
2     True
3    False
'''

from numpy import nan as NA

print
'丢弃缺失数据NaN'
data = Series([1, NA, 3.5, NA, 7])
print
data.dropna()
'''
0    1.0
2    3.5
4    7.0
'''

print
'DataFrame对丢弃NA的处理'
data = DataFrame([[1., 6.5, 3.], [1., NA, NA],
                  [NA, NA, NA], [NA, 6.5, 3.]])
print
data
'''
     0    1    2
0  1.0  6.5  3.0
1  1.0  NaN  NaN
2  NaN  NaN  NaN
3  NaN  6.5  3.0
'''
print
data.dropna()  # 默认只要某行有NA就全部删除
'''
     0    1    2
0  1.0  6.5  3.0
'''
print
data.dropna(how='all')  # 某行全部为NA才删除
'''
     0    1    2
0  1.0  6.5  3.0
1  1.0  NaN  NaN
3  NaN  6.5  3.0
'''
data[0] = NA
print
data.dropna(axis=1, how='all')  # 某行有NA就全部删除
'''
     1    2
0  6.5  3.0
1  NaN  NaN
2  NaN  NaN
3  6.5  3.0
'''
data = DataFrame(numpy.arange(21).reshape(7, 3))
data.ix[:4, 1] = NA
data.ix[:2, 2] = NA
print
data
'''
    0     1     2
0   0   NaN   NaN
1   3   NaN   NaN
2   6   NaN   NaN
3   9   NaN  11.0
4  12   NaN  14.0
5  15  16.0  17.0
6  18  19.0  20.0
'''
print
data.dropna(thresh=2)  # 每行至少要有2个非NA元素则删除
'''
    0     1     2
3   9   NaN  11.0
4  12   NaN  14.0
5  15  16.0  17.0
6  18  19.0  20.0
'''

print
'填充0'
df = DataFrame(numpy.arange(9).reshape(3, 3))
df.ix[:1, 1] = NA
df.ix[:2, 2] = NA
print
df.fillna(0)  # 默认inplace为False
'''
   0    1    2
0  0  0.0  0.0
1  3  0.0  0.0
2  6  7.0  0.0
'''
print
df
'''
   0    1   2
0  0  NaN NaN
1  3  NaN NaN
2  6  7.0 NaN
'''
df.fillna(0, inplace=True)  # 就地修改
print
df
'''
   0    1    2
0  0  0.0  0.0
1  3  0.0  0.0
2  6  7.0  0.0
'''
df = DataFrame(numpy.arange(9).reshape(3, 3))
df.ix[:1, 1] = NA
df.ix[:2, 2] = NA
print
'不同行列填充不同的值'
print
df.fillna({1: 0.5, 2: -1})  # 第3列不存在
'''
   0    1    2
0  0  0.5 -1.0
1  3  0.5 -1.0
2  6  7.0 -1.0
'''
print
'不同的填充方式'
print
df
'''
   0    1   2
0  0  NaN NaN
1  3  NaN NaN
2  6  7.0 NaN
'''
print
df.fillna(method='bfill')  # 向前填充
'''
   0    1   2
0  0  7.0 NaN
1  3  7.0 NaN
2  6  7.0 NaN
'''
print
df.fillna(method='bfill', limit=1)  # 只可向前填充一步
'''
   0    1   2
0  0  NaN NaN
1  3  7.0 NaN
2  6  7.0 NaN
'''

print
'用统计数据填充'
data = Series([1, NA, 2, NA, 3])
print
data.fillna(data.mean())
'''
0    1.0
1    2.0
2    2.0
3    2.0
4    3.0
'''

from pandas import MultiIndex

print
'Series的多层次索引'
data = Series(numpy.arange(8),
              index=[['a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'],
                     [1, 2, 1, 2, 1, 2, 1, 2]])
print
data  # 两层行索引
'''
a  1    0
   2    1
b  1    2
   2    3
c  1    4
   2    5
d  1    6
   2    7
'''
print
data.index
'''
MultiIndex(levels=[[u'a', u'b', u'c', u'd'], [1, 2]],
           labels=[[0, 0, 1, 1, 2, 2, 3], [0, 1, 0, 1, 0, 1, 0]])
'''
print
data.b
'''
1    2
2    3
'''
print
data['b':'c']  # 闭区间
'''
b  1    2
   2    3
c  1    4
   2    5
'''
print
data[:2]  # 数组索引不区分标签
'''
a  1    0
   2    1
'''
print
data.unstack()  # 将Series转换为DataFrame
'''
   1  2
a  0  1
b  2  3
c  4  5
d  6  7
'''
print
data.unstack().stack()  # 将DataFrame转换回Series
'''
a  1    0
   2    1
b  1    2
   2    3
c  1    4
   2    5
d  1    6
   2    7
'''
print

print
'DataFrame的多层次化索引'
frame = DataFrame(numpy.arange(12).reshape((4, 3)),
                  index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                  columns=[['A', 'A', 'B'], ['A1', 'A2', 'B1']])
print
frame  # 两层行索引和两层列索引
'''
     A       B
    A1  A2  B1
a 1  0   1   2
  2  3   4   5
b 1  6   7   8
  2  9  10  11
'''
print
frame.index
'''
MultiIndex(levels=[[u'a', u'b'], [1, 2]],
           labels=[[0, 0, 1, 1], [0, 1, 0, 1]])
'''
print
frame.columns
'''
MultiIndex(levels=[[u'A', u'B'], [u'A1', u'A2', u'B1']],
           labels=[[0, 0, 1], [0, 1, 2]])
'''
frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'more']
print
frame
'''
state      A       B
more      A1  A2  B1
key1 key2
a    1     0   1   2
     2     3   4   5
b    1     6   7   8
     2     9  10  11
'''
print
frame.ix['a', 1]
'''
A      A1      0
       A2      1
B      B1      2
'''
print
frame.ix['a', 1]['B']
'''
more
B1    2
'''
print
frame.ix['a', 1]['A']['A1']
'''
0
'''
print

print
'直接用MultiIndex创建层次索引结构index'
print
MultiIndex.from_arrays([['A', 'A', 'B'], ['Gree', 'Red', 'Green']],
                       names=['state', 'color'])
'''
MultiIndex(levels=[[u'A', u'B'], [u'Gree', u'Green', u'Red']],
           labels=[[0, 0, 1], [0, 2, 1]],
           names=[u'state', u'color'])
'''

print
'索引层交换'
frame = DataFrame(numpy.arange(12).reshape((4, 3)),
                  index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                  columns=[['A', 'A', 'B'], ['A1', 'A2', 'B1']])
frame.index.names = ['key1', 'key2']
print
frame
'''
           A       B
          A1  A2  B1
key1 key2
a    1     0   1   2
     2     3   4   5
b    1     6   7   8
     2     9  10  11
'''
frame_swapped = frame.swaplevel('key1', 'key2')  # 交互索引层
print
frame_swapped
'''
           A       B
          A1  A2  B1
key2 key1
1    a     0   1   2
2    a     3   4   5
1    b     6   7   8
2    b     9  10  11
'''
print
frame_swapped.swaplevel(0, 1)  # 交换回来
'''
           A       B
          A1  A2  B1
key1 key2
a    1     0   1   2
     2     3   4   5
b    1     6   7   8
     2     9  10  11
'''
print

print
'对某个索引层进行排序'
print
frame.sortlevel('key2')
'''
           A       B
          A1  A2  B1
key1 key2
a    1     0   1   2
b    1     6   7   8
a    2     3   4   5
b    2     9  10  11
'''
print
frame.swaplevel(0, 1).sortlevel(0)
'''
           A       B
          A1  A2  B1
key2 key1
1    a     0   1   2
     b     6   7   8
2    a     3   4   5
     b     9  10  11
'''

print
'根据索引层进行统计'
print
frame
'''
           A       B
          A1  A2  B1
key1 key2
a    1     0   1   2
     2     3   4   5
b    1     6   7   8
     2     9  10  11
'''
print
frame.sum(level='key2')
'''
       A       B
      A1  A2  B1
key2
1      6   8  10
2     12  14  16
'''

print
'将列转化行层次索引'
frame = DataFrame({'a': range(7),
                   'b': range(7, 0, -1),
                   'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two'],
                   'd': [0, 1, 2, 0, 1, 2, 3]})
print
frame
'''
  a  b    c  d
0  0  7  one  0
1  1  6  one  1
2  2  5  one  2
3  3  4  two  0
4  4  3  two  1
5  5  2  two  2
6  6  1  two  3
'''
print
frame.set_index(['c', 'd'])  # 把c/d列索引变成行索引
'''
       a  b
c   d
one 0  0  7
    1  1  6
    2  2  5
two 0  3  4
    1  4  3
    2  5  2
    3  6  1
'''
print
frame.set_index(['c', 'd'], drop=False)  # 列依然保留
'''
       a  b    c  d
c   d
one 0  0  7  one  0
    1  1  6  one  1
    2  2  5  one  2
two 0  3  4  two  0
    1  4  3  two  1
    2  5  2  two  2
    3  6  1  two  3
'''
frame2 = frame.set_index(['c', 'd'])
print
frame2.reset_index()  # 恢复索引
'''
     c  d  a  b
0  one  0  0  7
1  one  1  1  6
2  one  2  2  5
3  two  0  3  4
4  two  1  4  3
5  two  2  5  2
6  two  3  6  1
'''

print
'索引值为整数时的歧义'
ser = Series(numpy.arange(3))
print
ser
'''
0    0
1    1
2    2
'''
try:
    print
    ser[-1]  # 这里会有歧义.
except:
    print
    'exception'
ser2 = Series(numpy.arange(3), index=['a', 'b', 'c'])
print
ser2[-1]  # 索引值类型不是整数
# 2
ser3 = Series(range(3), index=[-5, 1, 3])
print
ser3.iloc[2]  # 使用iloc避免直接用[2]产生的歧义
# 2
print

print
'对DataFrame使用整数索引'
frame = DataFrame(numpy.arange(6).reshape((3, 2)), index=[2, 0, 1])
print
frame
'''
   0  1
2  0  1
0  2  3
1  4  5
'''
print
frame.iloc[-1]
'''
0    4
1    5
'''
# print frame[2] 有歧义则会发生异常错误
# print frame['2'] 不存在'2'该索引
print
frame.iloc[:, 1]
'''
2    1
0    3
1    5
'''