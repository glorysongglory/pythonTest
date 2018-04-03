import numpy as np

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
A = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(a)
print(A)
print(type(a))
print(type(A))

'''
其中 arange([start],stop,[step]) 声明了该数组元素起始与终止的值，
而 step 定义了给定区间内采样的步幅大小。在以上代码中，我们生成一个从零开始到 10 结束（不包含 10），
并且每次加 2 的数组。注意数组元素取值服从左闭右开原则，即取 0 而不取 10，停止数值并不能取到。

'''
a = np.arange(0, 10, 2)
print(a)

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(a)
print(a.shape)
B = a.reshape(3, 3)
print(B.shape)

# np.zeros((n,m)) 将返回一个 n*m 阶矩阵，其中每个值都为零。
print(np.zeros((4, 3)))

# np.eye(n) 将生成一个 n 阶单位方阵，即一个 n 阶矩阵，其主对角线元素都为 1，其它元素都为 0。
print(np.eye(5))

# 矩阵乘法在机器学习中十分重要，以下展示了怎样使用 NumPy 执行矩阵乘法。我们一般使用 np.dot() 执行矩阵乘法，即点积
I = np.eye(3)
D = np.arange(1, 10).reshape(3, 3)
print(np.dot(I, D))

'''np.sum() 会将整个矩阵的所有元素加和为一个标量值：
我们还可以提供参数以确定到底是沿矩阵的行累加还是沿矩阵的列累加。如下我们给定参数 axis=1，其代表将每一行的元素累加为一个标量值。
此外，给定参数 axis=0 则表示沿列累加：
'''
print(np.sum(np.dot(I, D)))
print(np.sum(np.dot(I, D), axis=1))
print(np.sum(np.dot(I, D), axis=0))

'''
使用 np.random.rand() 随机生成矩阵，即给定矩阵的形状，其中每个元素都是随机生成的
'''
print(np.random.rand(2, 3))
print(np.random.rand(12, 13))

'''
需要手动地给一个数组添加一个或多个元素，那么我们可以使用 np.append()
'''
print(np.append(A, 19))

'''
NumPy 提供了 np.diff() 方法以求 A[n+1]-A[n] 的值，该方法将输出一个由所有差分组成的数组。
'''
A = np.array([5, 7, 9, 11, 13, 19, 3, 55, 34, 553])
B = np.diff(A, n=1)
print(B)
print(np.diff(A, n=2))

'''
若我们希望将多个向量或矩阵按一定的方法堆叠成新的矩阵，那么 np.vstack() 和 np.column_stack() 方法将帮助我们实现这一操作,
堆叠一共有两种变体，即按行堆叠还是按列堆叠。按行堆叠即将需要的向量或矩阵作为新矩阵的一个行，按列堆叠即一个向量作为新矩阵的一列
'''
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]

print(np.vstack((a, b, c)))
print(np.vstack((b, a, c)))

print(np.column_stack((a, b, c)))
print(np.column_stack((b, a, c)))

'''
np 数组索引,NumPy 数组的索引方式和 Python 列表的索引方式是一样的，从零索引数组的第一个元素开始我们可以通过序号索引数组的所有元素
,如上 A[2:5] 索引了数组 A 中第 3 到第 5 个元素，注意 Python 列表和数组的索引都是左闭右开
'''
A = np.array([5, 7, 9, 11, 13, 19, 3, 55, 34, 553])
print(A[2:5])

# 矩阵转置
A = np.array([[1, 0], [2, 3]])
print(A)
print(A.transpose())

# 矩阵的迹
print(np.trace(A))



