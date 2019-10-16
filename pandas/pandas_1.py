import pandas as pd

if __name__ == '__main__':
    food_info = pd.read_csv("food_info.csv")
    # pandas.core.frame.DataFrame
    print(type(food_info))
    # 每个特征的类型 int64 object float64 bool datetime
    print(food_info.dtypes)
    # 默认返回前五行 可以传入参数  def head(self, n=5):
    print(food_info.head())
    # 默认返回后五行 可以传入参数
    print(food_info.tail())
    # 返回列特征索引
    print(food_info.columns)
    # 返回DataFrame形状
    print(food_info.shape)

    # 获取第一行数据
    print(food_info.loc[0])
    # DataFrame 每行数据类型为pandas.core.series.Series
    print(type(food_info.loc[0]))
    # 获取3、4、5行数据
    print(food_info.loc[3:6])
    # 获取2、5、10行数据
    print(food_info.loc[[2, 5, 10]])

    # 获取NDB_No列数据
    ndb_col = food_info["NDB_No"]
    # Name: NDB_No, Length: 8618, dtype: int64
    print(ndb_col)
    # Series
    print(type(ndb_col))

    # 获取多列数据
    columns = ["Zinc_(mg)", "Copper_(mg)"]
    zinc_copper = food_info[columns]
    print(zinc_copper)
    # pandas.core.frame.DataFrame
    print(type(zinc_copper))

    # 获取所有特征名称以g结尾的特征
    col_names = food_info.columns.tolist()
    # print col_names
    gram_columns = []

    for c in col_names:
        if c.endswith("(g)"):
            gram_columns.append(c)
    gram_df = food_info[gram_columns]
    print(gram_df.head(3))


    # pandas排序
    #ascending：默认True升序排列；False降序排列
    #inplace：默认False，否则排序之后的数据直接替换原来的数据
    food_info.sort_values("Sodium_(mg)", inplace=True)
    print(food_info["Sodium_(mg)"])

    #降序排列
    food_info.sort_values("Sodium_(mg)", inplace=True, ascending=False)
    print(food_info["Sodium_(mg)"])
