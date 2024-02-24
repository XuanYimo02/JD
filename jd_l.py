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
    url = "http://www.857ip.cn/getIP/json/jiejiedaren/zzxzzxzzx9/10"
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
    with open('列表.csv', 'w', newline='') as f:
        f.write('')
    # with open('列表.csv', 'a', newline='') as f:
    #     f.write('商品sku,商品链接图片,标题,商品类别,商品品牌,价格,促销,支持\n')
    gai = 16091
    num = gai
    timer = 0
    k = -1
    for value in third_column[gai:]:
        if timer == 100:
            timer = 0
            ip_dai()

        timer += 1
        print(value)

        url = f'https://api.m.jd.com/?appid=pc-item-soa&functionId=pc_detailpage_wareBusiness&client=pc&clientVersion=1.0.0&t=1689078234457&body=%7B%22skuId%22%3A{value}%2C%22cat%22%3A%2213314%2C21909%2C21921%22%2C%22area%22%3A%2215_1213_3038_59931%22%2C%22shopId%22%3A%221000015441%22%2C%22venderId%22%3A1000015441%2C%22paramJson%22%3A%22%7B%5C%22platform2%5C%22%3A%5C%22100000000001%5C%22%2C%5C%22specialAttrStr%5C%22%3A%5C%22p0ppp1pppppp2ppppppppppp1ppp%5C%22%2C%5C%22skuMarkStr%5C%22%3A%5C%2200%5C%22%7D%22%2C%22num%22%3A1%2C%22bbTraffic%22%3A%22%22%7D&h5st=20230711202354499%3B2628994075236133%3Bfb5df%3Btk03wa0021bb918niO1lTFMmjM5huxtv9p1QafKdoGE9rH7FEKFFUy1MGbAgYIJLBBYBoMoxSlI9fATpGSaPFPK2rvOT%3B961c13a4978bca762a95fe67662fa2f8b89a384cb5ce18fc597bdc136c8eea8f%3B3.1%3B1689078234499%3B24c9ee85e67cf80746dd82817ecbeafc7a829b35c7f446a4c7d476cc9faa1d8834a93323ad7bce9bef1bba682b93d2e39660ae8d453e3b0662c62666381aa5f076aaf79dcd3c545165153dc06d071a59b57c4150e88cce87de6b3c3847d40d3c&x-api-eid-token=jdd03OPG4EXSGXN6WBCEYLMW7IMXKWBDH6DI7WWONS4IWRTHO2Y66KTI54PS4DWDBPYQFKVOQCMZ5ROBV33RLDRW2YAS62UAAAAMJITTLPVQAAAAADYI4FG4KTWBRFQX&loginType=3&uuid=125919621.16890670765522085068047.1689067077.1689075586.1689078119.4'

        headers = {
            "GET": "appid=pc-item-soa&functionId=pc_detailpage_wareBusiness&client=pc&clientVersion=1.0.0&t=1689939375647&body=%7B%22skuId%22%3A100012687710%2C%22cat%22%3A%2213314%2C21909%2C21921%22%2C%22area%22%3A%2215_1213_3038_59931%22%2C%22shopId%22%3A%221000300492%22%2C%22venderId%22%3A1000300492%2C%22paramJson%22%3A%22%7B%5C%22platform2%5C%22%3A%5C%22100000000001%5C%22%2C%5C%22specialAttrStr%5C%22%3A%5C%22p0ppppppppp2ppppppppppp1ppp%5C%22%2C%5C%22skuMarkStr%5C%22%3A%5C%2200%5C%22%7D%22%2C%22num%22%3A1%2C%22bbTraffic%22%3A%22%22%7D&h5st=20230721193615687%3B5469866125036971%3Bfb5df%3Btk03w824d1c0418nVbXEUMxqaR31GXm9VI0L8TV0Uivi-BI-crMugJw6FK938-7dKZVsbSlfyrxhpvth2_5wMafIcfJg%3Bd1a9f126fc886bf5d22072c94fecdd9410caf6f3ec8b846454d47632155e6c61%3B3.1%3B1689939375687%3B24c9ee85e67cf80746dd82817ecbeafc7a829b35c7f446a4c7d476cc9faa1d88ac5c6f8bd926f3a1ad74112d65db142235ee329568bfb20afef8cfc37e867ae03b43a669ee40c82f7a34e3f2119a5ef71f357453f8b6fefaf47d98619e812fbf&x-api-eid-token=jdd03HBFOBEUVEZTE4LWT6IMN57EBOQGLOUUGYOIHY5KLBINWEUSULNY3Y4PWDRXDAKJZGEIGYMXHA3BL42YEEYNWYYWIX4AAAAMJPA5OCNYAAAAADNH4Y4KIQA5JEUX&loginType=3&uuid=125919621.16899390788731542418148.1689939079.1689939079.1689939079.1 HTTP/2",
            "Host": "api.m.jd.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Accept-Encoding": "gzip, deflate, br",
            "x-referer-page": "https://item.yiyaojd.com/100012687710.html",
            "x-rp-client": "h5_1.0.0",
            "Origin": "https://item.yiyaojd.com",
            "Connection": "keep-alive",
            "Referer": "https://item.yiyaojd.com/",
            "Cookie": "__jdu=16899390788731542418148; shshshfpb=cXe9ikxjBx9wdgyLC6h95jQ; __jda=125919621.16899390788731542418148.1689939079.1689939079.1689939079.1; __jdb=125919621.2.16899390788731542418148|1.1689939079; __jdc=125919621; __jdv=125919621|direct|-|none|-|1689939078874",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "cross-site",
            "TE": "trailers"
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
        with open('列表.csv', 'a', newline='') as f:
            f.write(f'{value}, {imag}, {name}, {type}, {pp}, {price}, {youhui}, {zhichi}\n')


if __name__ == '__main__':
    ip_dai()
    jd()
