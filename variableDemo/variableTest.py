print(type(100)) # 查看类型<class 'int'>
print((round(2/6, 4))) #取小数有效位(4位)
print(2**4)
str = '''abc'''
print(type(str)) # <class 'str'>
print('hello'+'2')# 先入为主 TypeError: must be str, not int
print('hello')
print('xintian')
print(3+2)
'''
数字对象
字符串对象
所有的数据类型都是对像
字面量  Literal  3    3.5  
'''
welcome = '欢迎来我家玩耍'
print('小A'+welcome)
a1=100
print(a1)
import keyword
print(keyword.kwlist)
print(id(100))# 查看内存地址
print(6/7)
print(6.0/7)
print(6//7) # 0 整除
# sin(90)=1
# sin(45)=2**0.5/2
a = 'abc'
b=123
print(type(a),type(b))
d=10
d+=9
print(d)