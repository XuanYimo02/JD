# Python作业
# 日期:2023/7/11 17:36
# File:jd
# Author 比窦娥还冤
# 清华镜像源: pip install -i https://pypi.tuna.tsinghua.edu.cn/simple
import random
import time

import openpyxl
import requests
from lxml import etree
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

proxies = []

def ip_dai():
    url = "http://webapi.http.zhimacangku.com/getip?num=10&type=2&pro=&city=0&yys=0&port=11&pack=306879&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions="
    # 芝麻IP代理
    r = requests.get(url).json()
    # 拿到代理里面的列表
    data = r['data']
    for i in data:
        dict = {}
        # dict['http'] = 'ip:port'
        #              '119.131.45.94' + ':' + '4225'
        dict['https'] = i['ip'] + ':' + str(i['port'])
        proxies.append(dict)

    print(proxies)


def jd():
    with open('data_s.csv', 'w', newline='') as f:
        f.write('')
    # url_ip = "http://webapi.http.zhimacangku.com/getip?num=10&type=2&pro=&city=0&yys=0&port=11&pack=306879&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions="
    # # 芝麻IP代理
    # r = requests.get(url_ip).json()
    # # r = {"code":0,"data":[{"ip":"110.87.251.165","port":4245},{"ip":"113.120.34.165","port":4256},{"ip":"114.99.131.34","port":4215},{"ip":"122.188.192.37","port":4234},{"ip":"113.141.222.36","port":4231},{"ip":"14.157.100.229","port":4215},{"ip":"117.83.81.88","port":4283},{"ip":"27.157.219.86","port":4235},{"ip":"42.56.238.132","port":4268},{"ip":"123.181.235.140","port":4227}],"msg":"0","success":'true'}
    # # 拿到代理里面的列表
    # data = r['data']

    # print(data)

    workbook = openpyxl.load_workbook('皮肤用药.xlsx')

    worksheet = workbook.worksheets[0]  # 根据索引选择

    first_column = [cell.value for cell in worksheet['A']]
    second_column = [cell.value for cell in worksheet['B']]
    third_column = [cell.value for cell in worksheet['C']]

    # f.write('商品sku,商品链接图片,标题,商品类别,商品品牌,价格,促销,支持\n')
    gai = 18174
    num = gai
    for value in third_column[gai:]:
        print(value)
        url = f'https://item.yiyaojd.com/{value}.html'
        # time.sleep(6)
        # proxy = random.choice(data)
        # print(proxy)
        # your_proxy_ip = proxy['ip']
        # your_proxy_port = proxy['port']

        chrome_options = Options()
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        # chrome_options.add_argument(f"--proxy-server={your_proxy_ip}:{your_proxy_port}")
        chrome_options.add_argument(
            'User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36')
        driver = webdriver.Chrome(options=chrome_options)
        driver.implicitly_wait(10)
        driver.maximize_window()

        driver.get(url)

        time.sleep(3)

        source = driver.page_source

        # print(source)

        ret = etree.HTML(source)
        name = ret.xpath('/html/body/div[6]/div/div[2]/div[1]/text()')[0].strip()
        img = 'https:' + ret.xpath('//*[@id="spec-img"]/@src')[0]
        type = first_column[num]
        pp = second_column[num]
        try:
            if "该商品已下柜，欢迎挑选其他商品！" == ret.xpath('/html/body/div[6]/div/div[2]/div[2]/text()')[0]:
                with open('data_s.csv', 'a', newline='') as f:
                    f.write(f'{value}, {img}, {name}, {type}, {pp}, -1, , \n')
                continue
        except:
            pass


        num+=1
        try:
            price = ret.xpath('/html/body/div[6]/div/div[2]/div[5]/div/div[1]/div[2]/span[1]/span[2]/text()')[0]
        except:
            price = ret.xpath('/html/body/div[6]/div/div[2]/div[4]/div/div[1]/div[2]/span[1]/span[2]/text()')[0]
        pre = ret.xpath('//*[@id="prom"]/div/div')
        youhui = ''
        for p in pre:
            youhui += p.xpath('./em[1]/text()')[0] + ':' + p.xpath('./em[2]/text()')[0] + '  '
        zhichi = ret.xpath('//*[@id="ns_services"]/div[1]/a')
        sum = ''
        for zc in zhichi:
            sum += zc.xpath('./text()')[0] + '  '
        print(url, img, name, type, pp, youhui, price, sum)
        with open('data_s.csv', 'a', newline='') as f:
            f.write(f'{value}, {img}, {name}, {type}, {pp}, {price}, {youhui}, {sum}\n')


if __name__ == '__main__':
    # ip_dai()
    jd()

