import inline
import matplotlib
import pandas as pd
#%matplotlib inline
titanic = pd.read_csv('/Users/mamin/PycharmProjects/automationProjects/wangmen/ticket.csv')
# print(titanic.head())
# print(titanic.head(2))
# print(titanic.isnull().sum) # 统计Null值的个数
# print(titanic.fillna(0))
# print(titanic.Age.median()) #
# titanic.Age.fillna(titanic.Age.median(),inplace=True)
# print(titanic.isnull().sum())
print(titanic.Sex.value_counts())# 做简单的汇总统计,经常用到
print()