import pandas as pd
from sklearn.decomposition import PCA
import time

'''
Instacart Market Basket Analysis
Which products will an Instacart counsumer puchase agin？
数据：
products.csv                       product_id,aisle_id     商品信息  ['product_id' 'product_name' 'aisle_id' 'department_id']
order_products__prior.csv          order_id, user_id    订单与商品信息 ['order_id' 'user_id' 'eval_set' 'order_number' 'order_dow''order_hour_of_day' 'days_since_prior_order']
orders.csv                         order_id,product_id     用户的订单信息['order_id' 'product_id' 'add_to_cart_order' 'reordered']
aisles.csv                         aisle_id,aisle    商品所属具体物品类别['aisle_id' 'aisle']


prior:product_id,order_id
products:product_id,aisle_id
orders:order_id,user_id
aisles:aisle_id,aisle


'''


def imba():
    start_time = time.time()

    products = pd.read_csv("./data/products.csv")  # product_id,aisle_id
    orders = pd.read_csv("./data/orders.csv")  # order_id, user_id
    prior = pd.read_csv("./data/order_products__prior.csv")  # order_id,product_id
    aisles = pd.read_csv("./data/aisles.csv")  # aisle_id,aisle

    _mg = pd.merge(products, prior, on=['product_id', 'product_id'])
    _mg = pd.merge(_mg, orders, on=['order_id', 'order_id'])
    mt = pd.merge(_mg, aisles, on=['aisle_id', 'aisle_id'])

    # 交叉表
    cross = pd.crosstab(mt['user_id'], mt['aisle'])
    print(cross)
    pca = PCA(n_components=0.95)
    cross = pca.fit_transform(cross)

    print(cross, cross.shape)
    print(time.time() - start_time)


if __name__ == '__main__':
    imba()
