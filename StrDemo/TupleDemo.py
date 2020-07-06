# tuple2=(100,200,180,201)
# print(tuple2)
# count_stu=200
# print('今天有:'+ str(count_stu) +'位同学考了100分')
# a =35
# print('abc'+str(a))
# print(type(str()))
# print('abc'*3)
# print('abc'+'bcd')
# a ='ABCDEFG'
# print(a[0])
# print(True+True)# 算术运算=1+1(等价于) 2  true和false参与算术运算
# print(True+False) # 1
# 关系运算符 >,<,>=,<=,!=
# print(True>False)#True
# print(False<True)
# print(123**2>100**3)
# print('a'>'b')# False ASCII码比大小  a=97  A=65 字母间只比较首位,如相同则看后一位,以此类推
# a = 30
# b =28
# print(a>b)# True
# print('a'>'b')#False
list1=[10,20,30,40,[50,60]]
list2=['abc','cde','efg']
print(50 in list1[-1])#True
# print(11 in list1)
# print('a bc' in list2)# False 空格本身也是一个字符
# print('a b' not in list2)
# 条件组合  and or not
# and 全真为真 一假为假 优先于Or 括号可以改变优先级
# or  一真为真 全假为假
# print(3>1 and 4>5 and 2>1 )# False  and中 一假为假
# print(3>1 and 4>5 and 2>1 or 1>0) # or 一真为真
# print(3>1 and 'ABCCDEFG')# true和字符串放一起就不打true了;≈
# print(1>3 and 'ABCCDEFG')#print(3>1 and 'ABCCDEFG')
# print(1>3 or 'ABCDEFG')#ABCDEFG 前面的式子为真,就不再执行后面的式子了
# print(True or False or True or ...)# 前面的式子为真,就不再执行后面的式子
# not非
# print(not 1 >0 or True)# True 优先级是not 优先于or
# =和==区别 =是赋值      == 恒等
# print(3==4)
# print(3**3!=27)#False
# print(1!=2)#True

#-----------------------------------
# 深拷贝浅拷贝
list3=[11,[22,33],44,55,66]
import copy

# list4=list3[:]# 浅拷贝
# list4=copy.copy(list3) # 属于浅拷贝 子列表会被改掉
list4=copy.deepcopy(list3)# 深拷贝 列表会分开来
# list4 = list3
print('list3原列:'+str(list3),id(list3))
print('liar4原列表:'+str(list4),id(list4))
list3[1].append(77)
print('更改后list3'+str(list3))
print('未做任何改变的List4'+str(list4))