# @Date    : 14:35 04/12/2020
# @Author  : ClassicalPi
# @FileName: Assistant.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import random
import urllib.request
import urllib.parse
import bs4
import time


def get_ip_list(obj):
    ip_text = obj.findAll('tr', {'class': 'odd'})  # 获取带有IP地址的表格的所有行
    ip_list = []
    for i in range(len(ip_text)):
        ip_tag = ip_text[i].findAll('td')
        ip_port = ip_tag[1].get_text() + ':' + ip_tag[2].get_text()  # 提取出IP地址和端口号
        ip_list.append(ip_port)
    print("共收集到了{}个代理IP".format(len(ip_list)))
    print(ip_list)
    return ip_list


class Assistant:

    def __init__(self):
        self.chrome = webdriver.Chrome()

    def get_random_ip(self):
        random_ip = 'http://' + random.choice(self.ip_list)
        proxy_ip = {'http:': random_ip}
        print('\tUsing Proxy:{}'.format(random_ip))
        return proxy_ip

    def parse_ip_web(self):
        url = 'http://www.xicidaili.com/'
        headers = {
            'User-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'}
        request = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(request)
        bsObj = bs4.BeautifulSoup(response, 'lxml')  # 解析获取到的html
        self.ip_list = get_ip_list(bsObj)


