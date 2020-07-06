import re # 加载正则表达式
str1 = 'songqin'
# a = re.findall('s.',sr1)# findall的返回值是一个列表
# print(a) #['so']
# *表示任意0到N位字符 .*  .*?
# a = re.findall('so*',str1) # ['so']
# b = re.findall('s*',str1)
# print(a) # ['s', '', '', '', '', '', '', '']
# print(b)
# .*贪婪匹配
# e = re.findall('s.*',str1) # 匹配s之后的所有值,包含s
# print(e) # ['songqin']
# d = re.findall('s.*g',str1)#['song'] #匹配s到g之前有所有值,包含s和g
# print(d) #['song']
# .*?偷懒匹配
i = re.findall('s.*?',str1)# 匹配s之后的任意字符,就偷懒了匹配了0字符
# print(i)#['s']
# l=re.findall('s.*?g',str1)#['song'] #匹配s到g之前有所有值,如果匹配到了就停
# print(l) # ['song']
# (.*?) # 带上括号就不包含边界值
# dd = re.findall('so(.*?)',str1)
# print(dd)
# str2 = '但使龙城飞将在'
# ccc = re.findall('但使龙.*?在',str2)
# print(ccc) # ['但使龙城飞将在']
# eee = re.findall('但使龙(.*?)在',str2)
# print(eee) # ['城飞将']
# * 和 +   区别    +号至少匹配一位,而*可以是0位或多位
# print(re.findall('so.+?',str1)) # ['son']
# print(re.findall('so.*?',str1)) #['so']
# print(re.findall('so.+',str1)) # ['songqin']
# print(re.findall('so.*',str1)) # ['songqin']
# print(re.findall('so.+?q',str1)) # ['songq']
# print(re.findall('so.*?q',str1)) #['songq']
# str3= '<span class="td">共31页,到第</span>'
# a1 =(re.findall('<span class="td">共(.+?)页,到第</span>',str3))
# a11 =(re.findall('<span class="td">共(.*?)页,到第</span>',str3))
# print(a1[0]) # 31
# print(a11[0])#31

# \w表示匹配字母数字下划线
str6 ='abc$de'
# a3 =re.findall('\w',str6)
# a33 =re.findall('\w{2}',str6) # {}里面的表示多少个字母数字下划线连续匹配
# print(a3) # ['a', 'b', 'c', 'd', 'e']
# print(a33) #a3 =re.findall('\w',str6)
# \W表示非字母数字下划线
# a4 =re.findall('\W',str6)
# print(a4) #['$']
# \s空字符串 \t制表符 ,换行符\n
# str7 = '      abc\n     '
# a3=re.findall('\s',str7)
# print(a3) # [' ', ' ', ' ', ' ', ' ', ' ', '\n', ' ', ' ', ' ', ' ', ' ']
# a33  = re.findall('\S',str7)
# print(a33) # ['a', 'b', 'c']
 # \d 匹配数字  \D匹配非数字
# str9 = 'adijldiendlkdD3.1415926'
# a3 = re.findall('\d',str9)
# print(a3) # ['3', '1', '4', '1', '5', '9', '2', '6']
# \D匹配非数字
# a33=re.findall('\D',str9)
# print(a33) # ['3', '1', '4', '1', '5', '9', '2', '6']
# 修饰符re.I不区分大小写
# str10 = 'abcABCDEe'
# print(re.findall('abc',str10)) #区分大小写
# print(re.findall('abc',str10,re.I))# 不区分大小写
# re.S 匹配所有字符
# str11='abc\ndef\tegfwf'
# print(re.findall('.*',str11)) # ['abc', '', 'def\tegfwf', '']
# print(re.findall('.*',str11,re.S)) # ['abc\ndef\tegfwf', '']
#  ^匹配开头,$匹配结尾
list11=['abcde','deabc','ghacbde']
for i in list11:
    print(re.findall('^abc',i))
    print(re.findall('^abc$', i))




