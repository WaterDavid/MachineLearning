import numpy as np

if __name__ == '__main__':
    # numpy索引
    # 在vector中取出等于5的值
    vector = np.array([5, 10, 15, 20])
    bool_index = (vector == 5)
    print(bool_index)
    print(vector[bool_index])

    # 在第二列中找出值等于25的行
    matrix = np.array([
        [5, 10, 15],
        [20, 25, 30],
        [35, 40, 45]
    ])

    bool_index = (matrix[:, 1] == 25)
    print(matrix[bool_index, :])

    # 布尔索引的与 或
    vector = np.array([5, 10, 15, 20])
    equal_to_ten_and_five = (vector == 10) & (vector == 5)
    print(equal_to_ten_and_five)

    # 或
    vector = np.array([5, 10, 15, 20])
    equal_to_ten_or_five = (vector == 10) | (vector == 5)
    print(equal_to_ten_or_five)

    vector = np.array(["1", "2", "3"])
    print(vector, vector.dtype)
    # ndarray.astype() 改变ndarray值的类型
    vector = vector.astype(np.float)
    print(vector, vector.dtype)

    # ndarray.sum() 求和
    # numpy中axis=1 表示将列归为一组 即按行分割
    vector = np.array([5, 10, 15, 20])
    print(vector.sum())

    matrix = np.array([
        [5, 10, 15],
        [20, 25, 30],
        [35, 40, 45]
    ])
    print(matrix.sum(axis=1))

    matrix = np.array([
        [5, 10, 15],
        [20, 25, 30],
        [35, 40, 45]
    ])
    print(matrix.sum(axis=0))
    print(matrix.mean())  # 平均数
