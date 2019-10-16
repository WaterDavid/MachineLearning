import numpy as np

if __name__ == '__main__':
    # genfromtxt的使用
    data = np.genfromtxt('world_alcohol.txt', delimiter=",", dtype=np.str)
    print(data)

    # 创建一个ndarray
    vector = np.array([5, 10, 15, 20])
    martrix = np.array([[5, 10, 15, 20], [35, 40, 45, 50]])

    print(vector, vector.shape)
    print(martrix, martrix.shape)
