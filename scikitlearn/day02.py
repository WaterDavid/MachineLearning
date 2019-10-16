from sklearn.datasets import load_iris, fetch_20newsgroups, load_boston
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np


def knncls():
    '''
    File descriptions
    train.csv, test.csv
    row_id: id of the check-in event
    x y: coordinates
    accuracy: location accuracy
    time: timestamp
    place_id: id of the business, this is the target you are predicting
    sample_submission.csv - a sample submission file in the correct format with random predictions
    :return:
    '''
    data = pd.read_csv("./facebook-v-predicting-check-ins/train.csv")

    # 1、缩小数据集范围
    data = data.query("x > 1.0 & x < 1.25 & y > 2.5 & y < 2.75")

    # 2、处理日期数据
    time = pd.to_datetime(data['time'], unit='s')
    time = pd.DatetimeIndex(time)
    data = data.drop(['time'], axis=1)
    data['day'] = time.day
    data['weekday'] = time.weekday
    data['hour'] = time.hour

    place_count = data.groupby("place_id").aggregate(np.count_nonzero)
    # print(place_count)
    tf = place_count[place_count.row_id > 5].reset_index()
    data = data[data['place_id'].isin(tf.place_id)]

    y = data['place_id']
    x = data.drop(['place_id', 'row_id'], axis=1)

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

    std = StandardScaler()
    x_train = std.fit_transform(x_train)
    x_test = std.fit_transform(x_test)

    knn = KNeighborsClassifier(n_neighbors=5)

    knn.fit(x_train, y_train)

    y_ttt = knn.predict(x_test)

    print(knn.score(x_test, y_test))


def iris():
    ir = load_iris()
    # print(ir.data)
    # print(ir.target)
    # print(ir.target_names)
    # print(ir.DESCR)
    # 训练集的特征值, 测试集的特征值,训练集的目标值,测试集的目标值 x训练集  y测试集  train特征值 test目标值
    x_train, y_train, x_test, y_test = train_test_split(ir.data, ir.target, test_size=0.25)
    print(x_train, x_test, y_train, y_test)


def news():
    ir = fetch_20newsgroups(subset='all')
    print(ir.data)
    print(ir.target)
    print(ir.target_names)
    print(ir.DESCR)


def boston():
    ir = load_boston()
    print(ir.data)
    print(ir.target)
    print(ir.feature_names)
    print(ir.DESCR)


def iris_knn():
    ir = load_iris()
    x_train, x_test, y_train, y_test = train_test_split(ir.data, ir.target, test_size=0.25)
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(x_train, y_train)
    print(knn.score(x_test, y_test))


if __name__ == '__main__':
    iris_knn()
