
import inline as inline
import matplotlib
import pandas as pd
import time
df = pd.read_csv('/Users/mamin/PycharmProjects/automationProjects/wangmen/成绩表.csv')
a = df.head(2)
# print(type(df)) #<class 'pandas.core.frame.DataFrame'>
# DataFrame
# print(df.columns) #列名
# print(df.index)
# print(df.loc[0])
# print(type(df.数学 > 80))
# print(df[df.数学 > 80])
# print(df[df.数学 < 70])
# print(df[(df.语文 > 80) & (df.数学 > 80) & (df.英语>80)]) #复杂筛选
#排序
# print(df.sort_values(['数学','语文']).head())
#访问
# print(df.head())
# print(df.loc[1])
#索引
# score = {
#     '英语':[90,78,89],
#     '数学':[64,78,45],
#     '姓名':['wang','li','sum']
# }
# df = pd.DataFrame(score, index=['one','two','three'])
# print(df)
# print(df.index)
# print(df.loc['onw']) #此时不存在数字索引,不能通过索引访问
# print(df.iloc[0]) #实实在在的所谓的第几行
# print(df.loc['two'])
# print(df.ix[:2])# 当索引 为数字索引的时候,Ix和ioc是等价的
# print(df.values)
# print(df.数学.value_counts())
# print(df.head())
# 提取多列

# def func(score):
#     if score>=80:
#         return '优秀'
#     elif score >=70:
#         return '良'
#     elif score>=60:
#         return '及格'
#     else:
#         return '不及格'
# df['数学分数']=df.数学.map(func)
# print(df.head())

# def func(number):
#     return number+10
# # 等价于
# # func = lambda number: return number+10
# # applymap对dataframe中所有的数据进行操作一个函数
# print(df.applymap(lambda x: str(x) + '-'))
# 匿名函数
# print([i+100 for i in range(10)])
# def func(x):
#     return x + 100 #[100, 101, 102, 103, 104, 105, 106, 107, 108, 109]
# print(list(map(func,range(10))))#[100, 101, 102, 103, 104, 105, 106, 107, 108, 109]
# print(df.apply(lambda x: x.数学, axis=1))
# df['new_score']= df.apply(lambda x: x.数学 + x.语文, axis=1)
# 前几行
# matplotlib绘图

import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

import inline
x = np.linspace(0,10,20)
# print(x)
y = np.sin(x)
# print(y)
plt.plot(x,y)
time.sleep(5)
plt.plot(x,np.cos(x))
plt.plot(x,y,'--')

