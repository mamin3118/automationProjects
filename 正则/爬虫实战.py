# 网络爬虫 从网站提取需要的数据
import requests  #加载网络爬虫模块
import re
from selenium import webdriver
import time

import xlwt

# 1.构建请求
# 2.解析响应的数据
# 3.提取需要的数据
# 4.保存数据
# user_header={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
# user_header={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
driver = webdriver.Chrome()

reps = driver.get(
    "https://search.51job.com/list/020000,000000,0000,00,9,99,%25E8%2587%25AA%25E5%258A%25A8%25E5%258C%2596%25E6%25B5%258B%25E8%25AF%2595,2,1.html")


time.sleep(1)
page = re.findall('<span class="td">共(.*?)页，到第</span>',reps.text,re.S)[0]
print(int(page))
time.sleep(1)

driver.quit()
# def get_pages():




    # reps.encoding='gbk' # 解决乱码
    # print(reps.text)
#     page = re.findall('共(.*?)页,到第',reps.text,re.S)[0]
#     return int(page)
# #<div class="el"></div>
# lines = re.findall('<div class="el">(.*?)</div>',reps.text,re.S)
# for line in lines:
#     temp=re.findall('<a target="_blank" title="(.*?)" href=""',line,re.S)
#     # print(line)
#     jobName=temp[0]
#     company=temp[1]
#     address=re.findall('<span class="t3"(.*?)</span>',line,re.S)[0]
#     salary = re.findall('<span class="t4"(.*?)</span>',line,re.S)[0]
#     jobTime = re.findall('<span class="t5"(.*?)</span>',line,re.S)[0]
#     row = 1
#     for value in (jobName,company,address,salary,jobTime):
#         worksheet1.write(row,)
#
# def excel_wt():
#     workbook = xlwt.Workbook(encoding='UTF-8')
#     colname = worksheet=['职位名','公司名','工作地点','薪资','发布时间']
#     for i in range(len(colname)):
#         worksheet.write(0,i,colname[i]) # 行,列,内容 在xlwt模块中,行和列是0开始算起
#     workbook.save('51job信息.xls')
#     return workbook,worksheet
# workbook1,worksheet1=excel_wt()

# 开始

