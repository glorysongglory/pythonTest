import pandas as pd
from pandas import Series,DataFrame
import numpy as np

'''
Series：一维数组，与Numpy中的一维array类似。二者与Python基本的数据结构List也很相近，其区别是：List中的元素可以是不同的数据类型，而Array和Series中则只允许存储相同的数据类型，这样可以更有效的使用内存，提高运算效率。
Time- Series：以时间为索引的Series。
DataFrame：二维的表格型数据结构。很多功能与R中的data.frame类似。可以将DataFrame理解为Series的容器。以下的内容主要以DataFrame为主。
Panel ：三维的数组，可以理解为DataFrame的容器。
Pandas 有两种自己独有的基本数据结构。读者应该注意的是，它固然有着两种数据结构，因为它依然是 Python 的一个库，所以，Python 中有的数据类型在这里依然适用，也同样还可以使用类自己定义数据类型。只不过，Pandas 里面又定义了两种数据类型：Series 和 DataFrame，它们让数据操作更简单了。
'''

# Series

s = Series([1, 4, 'ww', 'tt'])
print(s)

print(s.index)
print(s.values)

s2 = Series(['Wangxing', 'man', 24], index=['name', 'sex', 'age'])
print(s2)

print(s2['name'])

s2['name'] = 'wudalao'
print(s2['name'])

sd = {'python': 9000, 'c++': 9001, 'c#': 9000}
s3 = Series(sd)
print(s3)

s4 = Series(sd, index=['java', 'c++', 'c#'])
print(s4)

print(pd.isnull(s4))
print(s4.isnull)

s4.index = ['语文', '数学', 'English']
print(s4)

print(s4 * 2)

print(s4[s4 > 9000])

# dataFrame

data={"name":['google','baidu','yahoo'],"marks":[100,200,300],"price":[1,2,3]}
f1=DataFrame(data)
print(f1)

f2=DataFrame(data,columns=['name','price','marks'])
print(f2)

f3=DataFrame(data,columns=['name','marks','price'],index=['a','b','c'])
print(f3)


f4=DataFrame(data={"lang":{"firstline":"python","secondline":"java"}, "price":{"firstline":8000}})
print(f4)

print(DataFrame(data={"lang":{"firstline":"python","secondline":"java"}, "price":{"firstline":8000}},index=["firstline","secondline","thirdline"]))

print(f3['name'])

f6=DataFrame(data={'username':{'first':'wangxing','second':'dadiao'},'age':{'first':24,'second':25}},columns=['username','age','sex']);
print(f6)

f6['sex']='man'
print(f6)

f6['age']['second'] = 30
print(f6)

rng = pd.date_range('1/1/2013',periods=5,freq='D')
data = np.random.randn(5, 4)
cols = ['A','B','C','D']
df1, df2, df3 = pd.DataFrame(data, rng, cols), pd.DataFrame(data, rng, cols), pd.DataFrame(data, rng, cols)
pf = pd.Panel({'df1':df1,'df2':df2,'df3':df3});
print(pf['df1'])
