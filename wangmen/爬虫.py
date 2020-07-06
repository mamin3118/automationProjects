import requests
from bs4 import BeautifulSoup
import html5lib

# 封装函数,作用是获取列表页下面的所有租房页面链接,返回一个链接列表
def get_page(url):
    responce = requests.get(url)
    soup = BeautifulSoup(responce.text, features="html5lib")
    return soup

def get_links(link_url):
    url = 'https://bj.lianjia.com/zufang/'
    response = requests.get(url)
    soup = get_page(link_url)
    links_div = soup.find_all('div', class_="content__list--item")  # 与class区分加_
    links = [div.a.get('href') for div in links_div]
    return links

housd_url = 'https://bj.lianjia.com/zufang/BJ2556474366187806720.html'
soup = get_page(housd_url)


price = soup.find_all('div', class_='content__aside--title')


# price = soup.find_all('span')
# housr_info = soup.find_all('span', class_='label')
# a = housr_info[0].text[3:]# 81.5平米

# info = {
#     '价格':price,
#     '单价':unit,
#     '面积':area,
#     '户型':layout,
#     '楼层':floor,
#     '朝向':direction,
#     '发布时间':create_time,
#     '地铁':subway,
#     '小区':community,
#     '位置':location,
#     '经纪人名字':agent_name,
#     '经纪人Id':agent_id
# }
# return info








