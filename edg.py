# Python作业
# 日期:2023/7/11 20:25
# File:jd
# Author 比窦娥还冤
# 清华镜像源: pip install -i https://pypi.tuna.tsinghua.edu.cn/simple
import random
import time

import openpyxl
import requests

proxies = []


def ip_dai():
    proxies.clear()
    url = "http://www.857ip.cn/getIP/json/hailee123333/zzxzzxzzx9/10"
    # 芝麻IP代理
    r = requests.get(url).json()
    # 拿到代理里面的列表
    data = r['data']
    for i in data:
        dict = {}
        # dict['http'] = 'ip:port'
        #              '119.131.45.94' + ':' + '4225'
        dict['http'] = i['ip'] + ':' + str(i['port'])
        proxies.append(dict)

    print(proxies)


def jd():
    workbook = openpyxl.load_workbook('皮肤用药.xlsx')

    worksheet = workbook.worksheets[0]  # 根据索引选择

    first_column = [cell.value for cell in worksheet['A']]
    second_column = [cell.value for cell in worksheet['B']]
    third_column = [cell.value for cell in worksheet['C']]
    with open('列表_e.csv', 'w', newline='') as f:
        f.write('')
    # with open('列表.csv', 'a', newline='') as f:
    #     f.write('商品sku,商品链接图片,标题,商品类别,商品品牌,价格,促销,支持\n')
    gai = 6740
    num = gai
    timer = 0
    k = -1
    for value in third_column[gai:]:
        if timer == 100:
            timer = 0
            ip_dai()

        timer += 1
        print(value)
        t = int(random.random() * 1000000000)
        url = f'https://api.m.jd.com/?appid=pc-item-soa&functionId=pc_detailpage_wareBusiness&client=pc&clientVersion=1.0.0&t={t}&body=%7B%22skuId%22%3A{value}%2C%22cat%22%3A%2213314%2C21909%2C21921%22%2C%22area%22%3A%2215_1213_3038_59931%22%2C%22shopId%22%3A%221000300492%22%2C%22venderId%22%3A1000300492%2C%22paramJson%22%3A%22%7B%5C%22platform2%5C%22%3A%5C%22100000000001%5C%22%2C%5C%22specialAttrStr%5C%22%3A%5C%22p0ppppppppp2ppppppppppp1ppp%5C%22%2C%5C%22skuMarkStr%5C%22%3A%5C%2200%5C%22%7D%22%2C%22num%22%3A1%2C%22bbTraffic%22%3A%22%22%7D&h5st=20230721233620076%3B0019346180975917%3Bfb5df%3Btk03w6cb21bbd18ngD60nURkN4VqK5450__-L87EK9FNGrLWVlLtGdn_ndI_ZcZVluFpLy1n2Hsd_zIBf28stlCyn6lZ%3Bf06f4209674fb2a08e787873e9190dd0d7fbdcfc3f78c3a407f4996d21e4ac4e%3B3.1%3B1689953780076%3B24c9ee85e67cf80746dd82817ecbeafc7a829b35c7f446a4c7d476cc9faa1d8834a93323ad7bce9bef1bba682b93d2e3938e6fdf0b116e62557e4895c51d3caa6184e718c80776beed9a76bc5dab0760883ddb9eab33ae2cffd611791f1e53e2&x-api-eid-token=jdd03EY4JZ7VKCH4H2LLCCK6NWPZIUNHNVMFFM4NULLBW542L4Q4N6QLWEE77XBXD6IRYSRQP5AUMJMXHHV65AA4Z4J5MBAAAAAMJPEL4DLQAAAAAC3EAPPHQNCHCKEX&loginType=3&uuid=125919621.168907979814479342390.1689079798.1689942538.1689953748.4'
        headers = {
            "Authority": "api.m.jd.com",
            "Method": "GET",
            "Path": f"/?appid=pc-item-soa&functionId=pc_detailpage_wareBusiness&client=pc&clientVersion=1.0.0&t={t}&body=%7B%22skuId%22%3A{value}%2C%22cat%22%3A%2213314%2C21909%2C21921%22%2C%22area%22%3A%2215_1213_3038_59931%22%2C%22shopId%22%3A%221000300492%22%2C%22venderId%22%3A1000300492%2C%22paramJson%22%3A%22%7B%5C%22platform2%5C%22%3A%5C%22100000000001%5C%22%2C%5C%22specialAttrStr%5C%22%3A%5C%22p0ppppppppp2ppppppppppp1ppp%5C%22%2C%5C%22skuMarkStr%5C%22%3A%5C%2200%5C%22%7D%22%2C%22num%22%3A1%2C%22bbTraffic%22%3A%22%22%7D&h5st=20230721191159621%3B0019346180975917%3Bfb5df%3Btk03w6cb21bbd18ngD60nURkN4VqK5450__-L87EK9FNGrLWVlLtGdn_ndI_ZcZVluFpLy1n2Hsd_zIBf28stlCyn6lZ%3Be7b213c7f157841c10bb47714493d926b831e8d7d6f967707e395c0f2004d9a3%3B3.1%3B1689937919621%3B24c9ee85e67cf80746dd82817ecbeafc7a829b35c7f446a4c7d476cc9faa1d8834a93323ad7bce9bef1bba682b93d2e3938e6fdf0b116e62557e4895c51d3caa6184e718c80776beed9a76bc5dab0760883ddb9eab33ae2cffd611791f1e53e2&x-api-eid-token=jdd03EY4JZ7VKCH4H2LLCCK6NWPZIUNHNVMFFM4NULLBW542L4Q4N6QLWEE77XBXD6IRYSRQP5AUMJMXHHV65AA4Z4J5MBAAAAAMJPATDRGYAAAAADTRNZAFAD4BOVMX&loginType=3&uuid=125919621.168907979814479342390.1689079798.1689079798.1689937735.2",
            "Scheme": "https",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Cookie": "shshshfpb=vVB3fpqWuLjDAIJzVtIz5yQ; jsavif=0; __jdv=125919621|direct|-|none|-|1689079798145; __jda=125919621.168907979814479342390.1689079798.1689079798.1689937735.2; __jdb=125919621.1.168907979814479342390|2.1689937735; __jdc=125919621",
            "Origin": "https://item.yiyaojd.com",
            "Referer": "https://item.yiyaojd.com/",
            "Sec-Ch-Ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Microsoft Edge\";v=\"114\"",
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "\"Windows\"",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "cross-site",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82",
            "X-Referer-Page": f"https://item.yiyaojd.com/{value}.html",
            "X-Rp-Client": "h5_1.0.0"
        }

        t = 0
        li = [5]
        while 1:
            k += 1
            if k == 10:
                k = 0
            print(k)
            try:
                time.sleep(random.choice(li))
                # t += 1
                # if t == 2:
                #     time.sleep(5)
                #     t = 0

                print(proxies[k])
                e = requests.get(url=url, headers=headers, proxies=proxies[k])
                r = e.json()
                print(r)
                if 'extendWarrantyInfo' in r:
                    break
                if 'extendWarrantyInfo' not in r:
                    time.sleep(50)

            except:
                t += 1
                if t == 2:
                    time.sleep(3)
                if t == 3:
                    time.sleep(5)
                    t = 0
                print(e)

        type = first_column[num]
        pp = second_column[num]
        num += 1
        try:
            name = r['wareInfo']['wname']
        except:
            continue
        imag = 'https://img10.360buyimg.com/n1/' + r['wareInfo']['imageurl']
        try:
            youh = r['promotion']['activity']
        except:
            youh = []
        youhui = ''
        for yh in youh:
            youhui += yh['text'] + ':' + yh['value'] + '  '
        price = r['price']['p']
        zhic = r['servicesInfoUnited']['serviceInfo']['basic']['iconList']
        zhichi = ''
        for zc in zhic:
            zhichi += zc['text'] + '  '
        print(value, imag, name, type, pp, price, youhui, zhichi)
        with open('列表_e.csv', 'a', newline='',encoding='gb18030') as f:
            f.write(f'{value}, {imag}, {name}, {type}, {pp}, {price}, {youhui}, {zhichi}\n')


if __name__ == '__main__':
    ip_dai()
    jd()
