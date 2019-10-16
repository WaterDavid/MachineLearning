import numpy as np
import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import Imputer
from sklearn.feature_selection import VarianceThreshold
from sklearn.decomposition import PCA
# sklearn.feature_extraction.DictVectorizer 字典特征抽取
from sklearn.preprocessing import MinMaxScaler, StandardScaler


def dict_vector():
    li = [{'city': '北京', 'temperature': 100}, {'city': '上海', 'temperature': 60}, {'city': '深圳', 'temperature': 30}]
    dic = DictVectorizer()
    data = dic.fit_transform(li)
    print(data)
    print(data.toarray())


# sklearn.feature_extraction.text.CountVectorizer
def count_vector():
    li = ["life is short,i like python", "life is too long,i dislike python"]
    count = CountVectorizer()
    data = count.fit_transform(li)
    print(data)
    print(data.toarray())
    print(count.get_feature_names())


def tfid():
    tf = TfidfVectorizer()
    li = ["life is short,i like python", "life is too long,i dislike python"]
    data = tf.fit_transform(li)
    print(data)


def max_min():
    li = [[90, 2, 10, 40],
          [60, 4, 15, 45],
          [75, 3, 13, 46]]
    mm = MinMaxScaler()
    data = mm.fit_transform(li)
    print(data)


def stand():
    li = [[90, 2, 10, 40],
          [60, 4, 15, 45],
          [75, 3, 13, 46]]
    st = StandardScaler()
    data = st.fit_transform(li)
    print(data)


def im():
    val = [[1, 2],
           [np.nan, 3],
           [7, 6]]

    imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
    val = imp.fit_transform(val)
    print(val)


def vth():
    arr = [[0, 2, 0, 3],
           [0, 1, 4, 3],
           [0, 1, 1, 3]]
    vt = VarianceThreshold(threshold=1.0)
    arr = vt.fit_transform(arr)
    print(arr)


def pca():
    val = [[2, 8, 4, 5],
           [6, 3, 0, 8],
           [5, 4, 9, 1]]
    pc = PCA(n_components=0.9)
    val = pc.fit_transform(val)
    print(val)

if __name__ == '__main__':
    # dict_vector()
    # count_vector()
    # tfid()
    # max_min()
    # stand()
    # im()
    pca()
