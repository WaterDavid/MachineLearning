import pandas as pd
import numpy as np

if __name__ == '__main__':
    titanic_survival = pd.read_csv("titanic_train.csv")
    print(titanic_survival.head())

    #统计年龄为NaN缺失的数量
    age = titanic_survival["Age"]
    print(age.loc[0:10])
    #获取bool索引列表  NaN为True
    age_is_null = pd.isnull(age)
    print(age_is_null)
    #获取bool为True的行
    age_null_true = age[age_is_null]
    print(age_null_true)
    #统计为NaN的行数
    age_null_count = len(age_null_true)
    print(age_null_count)

    #船舱类别
    passenger_classes = [1, 2, 3]
    fares_by_class = {}
    # 遍历船舱类别
    for this_class in passenger_classes:
        #获取当前船舱的数据
        pclass_rows = titanic_survival[titanic_survival["Pclass"] == this_class]
        #获取当前船舱票价数据
        pclass_fares = pclass_rows["Fare"]
        #求票价数据平均值
        fare_for_class = pclass_fares.mean()
        fares_by_class[this_class] = fare_for_class
    print(fares_by_class)

    #DataFrame.pivot_table(values=None, index=None, columns=None, aggfunc='mean', fill_value=None, margins=False, dropna=True, margins_name='All')
    #Create a spreadsheet-style pivot table as a DataFrame. The levels in the pivot table will be stored in MultiIndex objects (hierarchical indexes) on the index and columns of the result DataFrame.
    #每个船舱存活率
    passenger_survival = titanic_survival.pivot_table(index="Pclass", values="Survived", aggfunc=np.mean)
    print(passenger_survival)
    #每个船舱年龄平均数
    passenger_age = titanic_survival.pivot_table(index="Pclass", values="Age")
    print(passenger_age)

    #删除有空值的列
    drop_na_columns = titanic_survival.dropna(axis=1)
    print(drop_na_columns)
    #删除Age或Sex中有空值的行
    new_titanic_survival = titanic_survival.dropna(axis=0, subset=["Age", "Sex"])
    print(new_titanic_survival)

    #按照年龄降序排列
    new_titanic_survival = titanic_survival.sort_values("Age", ascending=False)
    print(new_titanic_survival[0:10])
    #重设index
    itanic_reindexed = new_titanic_survival.reset_index(drop=True)
    print(itanic_reindexed.iloc[0:10])

    #自定义函数处理
    def hundredth_row(column):
        print(column)
        # Extract the hundredth item
        hundredth_item = column.iloc[99]
        return hundredth_item


    # Return the hundredth item from each column
    hundredth_row = titanic_survival.apply(hundredth_row)
    print(hundredth_row)
