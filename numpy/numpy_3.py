import numpy as np
from numpy import pi

if __name__ == '__main__':
    # numpy形状
    a = np.arange(15).reshape(3, 5)
    print(a)
    print('形状', a.shape)
    print('维数', a.ndim)
    print('类型名称', a.dtype.name)
    print('大小元素个数', a.size)

    # 创建值都为0的ndarray 需要转入一个元祖 一维可以直接传入大小
    print(np.zeros((3, 4)))
    print(np.zeros((3,)))
    print(np.zeros(4))

    # 创建值都为1，类型为int32的ndarray
    print(np.ones((2, 3, 4), dtype=np.int32))

    # 创建10到30步长为5的ndarray
    print(np.arange(10, 30, 5))

    # 创建2行3列的随机数数组
    print(np.random.random((2, 3)))

    # 在0至2*pi 的范围里 创建100个数
    print(np.linspace(0, pi * 2, 100))

    # np.sin(ndarray) 求余弦值
    print(np.sin(np.arange(0, 30)))

    # ndarray运算
    a = np.array([20, 30, 40, 50])
    b = np.arange(4)
    print(a, b)
    c = a - b  # a中元素减b中元素
    print(c)

    print(b ** 2)  # b中每一个元素平方

    print(a < 35)  # a中每个元素与35做比较

    A = np.array([[1, 1],
                  [0, 1]])

    B = np.array([[2, 0],
                  [3, 4]])

    print('A', A, 'B', B)
    # 元素相乘
    print('元素相乘', A * B)
    # 矩阵相乘
    print('矩阵相乘', A.dot(B))
    # 矩阵相乘
    print('矩阵相乘', np.dot(A, B))

    '''
    numpy.ceil(x,)      向正无穷取整
    numpy.floor(x,)     向负无穷取整
    numpy.trunc/fix(x,) 截取整数部分
    numpy.rint(x,)      四舍五入到最近整数
    numpy.around(x,)    四舍五入到给定的小数位
    '''
    B = np.arange(3)
    # ndarray根号np.sqrt(ndarray)
    print(np.sqrt(B))

    C = np.random.random((100,)) * 10
    #  向下取整np.ceil(ndarray)
    print(C)
    print(np.ceil(C))

    #  向下取整np.floor(ndarray)
    print(C)
    print(np.floor(C))

    # ndarray合并、分离
    a = np.floor(10 * np.random.random((2, 2)))
    b = np.floor(10 * np.random.random((2, 2)))
    print(a, b)
    print('横向合并 列相加', np.hstack((a, b)))
    print('列合并 行相加', np.vstack((a, b)))

    # nadrray拷贝
    a = np.arange(12)
    b = a  # a和b指向同一片内存空间
    print('b is a', b is a)
    b.shape = (3, 4)
    print(a.shape)
    print('aid', id(a))
    print('bid', id(b))

    c = a.view()  # c和a指向不同的内存空间但是共享数据
    print('c is a', c is a)
    c.shape = 2, 6
    print(a.shape)
    c[0, 4] = 1234
    print(c)
    print(a)

    d = a.copy()  # d和a指向不同的内存空间
    print('d is a', d is a)
    d[0, 0] = 9999
    print(d)
    print(a)

    # ndarray 最大值 ndarray.max(axsi=0)
    a = np.arange(20).reshape(5, 4)
    print(a)
    # 每一列最大值
    print(a.max(axis=0))

    # 通过重复A重复给出的次数来构造数组
    a = np.arange(0, 40, 10)
    b = np.tile(a, (3, 5))
    print(a)
    print(b)

    # ndarray 排序
    a = np.array([[4, 3, 5], [1, 2, 1]])
    print(a)
    b = np.sort(a, axis=1)
    # 按行排序
    print(b)
    a.sort(axis=1)  # 按行排序
    print(a)

    a = np.array([4, 3, 1, 2])
    j = np.argsort(a)  # 返回排序后的索引
    print(j)
    print(a[j])

    # 转置 平铺
    a = np.arange(12).reshape(3, 4)
    print(a)
    # 转置
    print(a.T)
    print(np.transpose(a))
    print(a.swapaxes(0, 1))
    # 平铺
    print(a.ravel())
