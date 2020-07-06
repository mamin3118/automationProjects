import array
import timeit

import axis as axis
import numpy as np
a = array.array('i',range(10))
# a_list = list(range(10))
# b = np.array(a_list)
# print(type(b))#<class 'numpy.ndarray'>
#
# aa = np.zeros(10, dtype=int)
# print(type(aa))#<class 'numpy.ndarray'>

# aaa = np.zeros((4,4), dtype=int)
# print(aaa)
# print(type(aaa))
# b = np.ones((4,4), dtype=float)
# print(b)
#
# c = np.full((3,3), 3.14)
# print(c)
# cc = np.ones_like(c)
# print(cc)
#
# e = np.full_like(c, 4.12, dtype=float)
# print(e)
import random
# print(random.randint(5,10))
# print(random.random)

# print(np.random.randint(0,10,(5,5)))
# print(list(range(0,10,2)))
# print(np.arange(0,3,2))
# print(np.linspace(0,3,10))
# print(np.eye(5)) #n维的单位矩阵
# qian套列表的元素访问
# var = [[1,2,3],[3,4,5],[5,6,7]]
# print(var[0][0])
# a = np.array(var)
# print(a)
# print(a[-1][0])
# print(a[2,0],a[2][0]) # 方式一样
# print(a[:2,:2])
# print(a[:2][:2])
# 维度

##print(a.naim)
# a = np.array(list(range(10)))
# print(a+10)
# print(a-10)
# print(a*100)
# a = np.full((3,3),1.0,dtype=float)
# print(a+10)
# aa = np.linspace(0,np.pi,5)
# bb = np.sin(aa)
# print(aa)
# print(bb)
# 统计类型
# print(sum([1,2,3,4,5,6]))
# a = np.full(10, 2.3)# 数组一维求和
# print(sum(a))
# aa = np.array([[1,2],[3,4]])# 多维求和
# print(sum(aa))
# print(np.sum(a))
# print(np.sum(aa,axis=1))
# print(np.max(aa,axis=1))
# n = np.random.rand(1000)
# print(n)
# notebook使用小技巧
#%timeit 代码 判断程序的执行效率
# s = np.array(range(10))
# print(s)
# print(s>3)
# print(s != 3)
# print(s == 3)
# print(np.all(s >-1))
# print(np.any(a>-1))
# 变形
# a = np.full((2,10),1,dtype=float)
# print(a)
# print(a.reshape(4,5))
# 排序
# l = [1,2,3],[3,12,4],[32,2,33]
# a = np.array(l)
# print(a)
# print(np.sort(a))
# print(a.sort((axis=0)))
