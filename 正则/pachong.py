import requests #加载网络爬虫模块
import re
import xlwt #excel写入模块

user_header={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

def get_pages():
    web_url = "https://search.51job.com/list/020000,000000,0000,00,9,99,%25E8%2587%25AA%25E5%258A%25A8%25E5%258C%2596%25E6%25B5%258B%25E8%25AF%2595,2,1.html"
    reps = requests.get(web_url, headers=user_header)
    reps.encoding = 'gbk'  # 解决乱码
    page = re.findall('<span class="td">共(.*?)页，到第</span>', reps.text, re.S)[0]# 匹配所有字符
    return int(page)

def excel_wt():
    workbook=xlwt.Workbook(encoding='UTF-8') #实例化一个excel
    worksheet=workbook.add_sheet('51job') #excel添加一个sheet并起名
    colname=['职位名','公司名','工作地点','薪资','发布时间']
    for i in range (len(colname)):
        worksheet.write(0,i,colname[i]) #行，列，内容 在xlwt模块中，行和列是从0开始算起
    workbook.save('51job信息.xls')
    return workbook,worksheet
workbook1,worksheet1=excel_wt()
row=1 #从第1行开始写入，wlxt是从第0行开始算起，第0行已经有标题了，所以row=1实际上是从第二行开始的
for i in range (get_pages()):
    #网址。注意{i+1}.html，表示每次循环获取一页的数据
    web_url=f'https://search.51job.com/list/020000,000000,0000,00,9,99,%25E8%2587%25AA%25E5%258A%25A8%25E5%258C%2596%25E6%25B5%258B%25E8%25AF%2595,2,{i+1}.html'
    #实例化一个requests，需要两个属性，网址和请求头
    reps=requests.get(web_url,headers=user_header) #实例化一个requests
    reps.encoding='gbk' #解决乱码
    # <div class="el"> </div>
    # 将网页上一行的html信息都取出来，reps.text表示从整个网页中获取，re.S表示包括任何字符
    lines=re.findall('<div class="el">(.*?)</div>',reps.text,re.S)
    #开始循环，配合正则表达式获取到需要的数据
    for line in lines:
        temp=re.findall('<a target="_blank" title="(.*?)" href="',line,re.S)
        jobName=temp[0] #获取职位
        company=temp[1] #获取公司名
        address=re.findall('<span class="t3">(.*?)</span>',line,re.S)[0] #地址
        salary = re.findall('<span class="t4">(.*?)</span>',line,re.S)[0] #工资
        jobTime = re.findall('<span class="t5">(.*?)</span>',line,re.S)[0] #发布时间
        # print(jobName,company,address,salary,jobTime)
        #准备开始写入到excel
        k=0
        for value in (jobName,company,address,salary,jobTime):
            worksheet1.write(row,k,value) #行，列，内容
            k+=1
        row+=1
    print(f'正在保存第{i+1}页数据')
workbook1.save('51job信息.xls')

