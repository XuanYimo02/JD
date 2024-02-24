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
    with open('列表_1.csv', 'w', newline='') as f:
        f.write('')
    # with open('列表.csv', 'a', newline='') as f:
    #     f.write('商品sku,商品链接图片,标题,商品类别,商品品牌,价格,促销,支持\n')
    gai = 15723
    num = gai
    timer = 0
    k = -1
    for value in third_column[gai:]:
        if timer == 100:
            timer = 0
            ip_dai()

        timer += 1
        print(value)

        url = f'https://api.m.jd.com/?appid=pc-item-soa&functionId=pc_detailpage_wareBusiness&client=pc&clientVersion=1.0.0&t=1690111917922&body=%7B%22skuId%22%3A{value}%2C%22cat%22%3A%2213314%2C21909%2C21921%22%2C%22area%22%3A%2215_1213_3038_59931%22%2C%22shopId%22%3A%221000300492%22%2C%22venderId%22%3A1000300492%2C%22paramJson%22%3A%22%7B%5C%22platform2%5C%22%3A%5C%22100000000001%5C%22%2C%5C%22specialAttrStr%5C%22%3A%5C%22p0ppppppppp2ppppppppppp1ppp%5C%22%2C%5C%22skuMarkStr%5C%22%3A%5C%2200%5C%22%7D%22%2C%22num%22%3A1%2C%22bbTraffic%22%3A%22%22%7D&h5st=20230723193157992%3B8333628654621072%3Bfb5df%3Btk03wba1f1c9c18nqV7afQhwF9cLk9kCySZWxDylQq5kL65JQHgRvYcdLeD3mx48XQsPLp1P4Si3cMNsxirWZkAIfbNh%3B20b0899a0c3a7831a9b6c7c6aff171a565b5b0f6382c3228fc4dc48010f7ce18%3B3.1%3B1690111917992%3B24c9ee85e67cf80746dd82817ecbeafc7a829b35c7f446a4c7d476cc9faa1d8834a93323ad7bce9bef1bba682b93d2e3d7f70cc2e6f7e902188e8a3640d207da74bc7d8c7d6ad6b0545db33c1aca877f096a61ee5d060fba70b4d180986ad828&x-api-eid-token=jdd034JN7IR3VHS5PPDULQJMCAFGKR6QFULJJ4MYZ2YCIU4VON356GFCTATLBLYYX4GIRT7NAYRKSBAH5PXGL2R7Z3743XMAAAAMJQKCSYJYAAAAACFOAGYD6OAVHY4X&loginType=3&uuid=125919621.1689938728638330604939.1689938729.1690109791.1690111913.15'

        t = int(random.random() * 1000000000)
        headers = [{
            "authority": "api.m.jd.com",
            "method": "GET",
            "path": f"/?appid=pc-item-soa&functionId=pc_detailpage_wareBusiness&client=pc&clientVersion=1.0.0&t={t}&body=%7B%22skuId%22%3A{value}%2C%22cat%22%3A%2213314%2C21909%2C21921%22%2C%22area%22%3A%2215_1213_3038_59931%22%2C%22shopId%22%3A%221000300492%22%2C%22venderId%22%3A1000300492%2C%22paramJson%22%3A%22%7B%5C%22platform2%5C%22%3A%5C%22100000000001%5C%22%2C%5C%22specialAttrStr%5C%22%3A%5C%22p0ppppppppp2ppppppppppp1ppp%5C%22%2C%5C%22skuMarkStr%5C%22%3A%5C%2200%5C%22%7D%22%2C%22num%22%3A1%2C%22bbTraffic%22%3A%22%22%7D&h5st=20230721192534711%3B8333628654621072%3Bfb5df%3Btk03w91c71ac518nJq8FXiwUdNhqVCpa6bTEqQ9333loO6THJhAm1f5_xo1jrfSxD6SS4X7Wt3Gt6-NhJH9G7-TaGDJS%3Bb41e1fd7a217fe4c9cb37c9eb479a8695fb76df4ef84aa67d0c526bf74d4a620%3B3.1%3B1689938734711%3B24c9ee85e67cf80746dd82817ecbeafc7a829b35c7f446a4c7d476cc9faa1d8834a93323ad7bce9bef1bba682b93d2e3d7f70cc2e6f7e902188e8a3640d207da74bc7d8c7d6ad6b0545db33c1aca877f096a61ee5d060fba70b4d180986ad828&x-api-eid-token=jdd034JN7IR3VHS5PPDULQJMCAFGKR6QFULJJ4MYZ2YCIU4VON356GFCTATLBLYYX4GIRT7NAYRKSBAH5PXGL2R7Z3743XMAAAAMJPAZJFMAAAAAACJWKVZLOYRD4K4X&loginType=3&uuid=125919621.1689938728638330604939.1689938729.1689938729.1689938729.1",
            "scheme": "https",
            "accept": "application/json, text/javascript, */*; q=0.01",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9",
            "cookie": "shshshfpb=d8nTAEyqCJTpxqADATh-ddQ; __jda=125919621.1689938728638330604939.1689938729.1689938729.1689938729.1; __jdb=125919621.1.1689938728638330604939|1.1689938729; __jdc=125919621; __jdv=125919621|direct|-|none|-|1689938728639",
            "origin": "https://item.yiyaojd.com",
            "referer": "https://item.yiyaojd.com/",
            "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"8\"",
            "sec-ch-ua-mobile": "?0",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.1.4031 SLBChan/30",
            "x-referer-page": f"https://item.yiyaojd.com/{value}.html",
            "x-rp-client": "h5_1.0.0"
        }, {
            "authority": "api.m.jd.com",
            "method": "GET",
            "path": f"/?appid=pc-item-soa&functionId=pc_detailpage_wareBusiness&client=pc&clientVersion=1.0.0&t={t}&body=%7B%22skuId%22%3A{value}%2C%22cat%22%3A%2213314%2C21909%2C21921%22%2C%22area%22%3A%2215_1213_3038_59931%22%2C%22shopId%22%3A%221000300492%22%2C%22venderId%22%3A1000300492%2C%22paramJson%22%3A%22%7B%5C%22platform2%5C%22%3A%5C%22100000000001%5C%22%2C%5C%22specialAttrStr%5C%22%3A%5C%22p0ppppppppp2ppppppppppp1ppp%5C%22%2C%5C%22skuMarkStr%5C%22%3A%5C%2200%5C%22%7D%22%2C%22num%22%3A1%2C%22bbTraffic%22%3A%22%22%7D&h5st=20230721192534711%3B8333628654621072%3Bfb5df%3Btk03w91c71ac518nJq8FXiwUdNhqVCpa6bTEqQ9333loO6THJhAm1f5_xo1jrfSxD6SS4X7Wt3Gt6-NhJH9G7-TaGDJS%3Bb41e1fd7a217fe4c9cb37c9eb479a8695fb76df4ef84aa67d0c526bf74d4a620%3B3.1%3B1689938734711%3B24c9ee85e67cf80746dd82817ecbeafc7a829b35c7f446a4c7d476cc9faa1d8834a93323ad7bce9bef1bba682b93d2e3d7f70cc2e6f7e902188e8a3640d207da74bc7d8c7d6ad6b0545db33c1aca877f096a61ee5d060fba70b4d180986ad828&x-api-eid-token=jdd034JN7IR3VHS5PPDULQJMCAFGKR6QFULJJ4MYZ2YCIU4VON356GFCTATLBLYYX4GIRT7NAYRKSBAH5PXGL2R7Z3743XMAAAAMJPAZJFMAAAAAACJWKVZLOYRD4K4X&loginType=3&uuid=125919621.1689938728638330604939.1689938729.1689938729.1689938729.1",
            "scheme": "https",
            "accept": "application/json, text/javascript, */*; q=0.01",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9",
            "cookie": "shshshfpb=d8nTAEyqCJTpxqADATh-ddQ; __jda=125919621.1689938728638330604939.1689938729.1689938729.1689938729.1; __jdb=125919621.1.1689938728638330604939|1.1689938729; __jdc=125919621; __jdv=125919621|direct|-|none|-|1689938728639",
            "origin": "https://item.yiyaojd.com",
            "referer": "https://item.yiyaojd.com/",
            "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"8\"",
            "sec-ch-ua-mobile": "?0",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.1.4031 SLBChan/30",
            "x-referer-page": f"https://item.yiyaojd.com/{value}.html",
            "x-rp-client": "h5_1.0.0"
        }, {
            "authority": "api.m.jd.com",
            "method": "GET",
            "path": f"/?appid=pc-item-soa&functionId=pc_detailpage_wareBusiness&client=pc&clientVersion=1.0.0&t={t}&body=%7B%22skuId%22%3A{value}%2C%22cat%22%3A%2213314%2C21909%2C21921%22%2C%22area%22%3A%2215_1213_3038_59931%22%2C%22shopId%22%3A%221000300492%22%2C%22venderId%22%3A1000300492%2C%22paramJson%22%3A%22%7B%5C%22platform2%5C%22%3A%5C%22100000000001%5C%22%2C%5C%22specialAttrStr%5C%22%3A%5C%22p0ppppppppp2ppppppppppp1ppp%5C%22%2C%5C%22skuMarkStr%5C%22%3A%5C%2200%5C%22%7D%22%2C%22num%22%3A1%2C%22bbTraffic%22%3A%22%22%7D&h5st=20230721192534711%3B8333628654621072%3Bfb5df%3Btk03w91c71ac518nJq8FXiwUdNhqVCpa6bTEqQ9333loO6THJhAm1f5_xo1jrfSxD6SS4X7Wt3Gt6-NhJH9G7-TaGDJS%3Bb41e1fd7a217fe4c9cb37c9eb479a8695fb76df4ef84aa67d0c526bf74d4a620%3B3.1%3B1689938734711%3B24c9ee85e67cf80746dd82817ecbeafc7a829b35c7f446a4c7d476cc9faa1d8834a93323ad7bce9bef1bba682b93d2e3d7f70cc2e6f7e902188e8a3640d207da74bc7d8c7d6ad6b0545db33c1aca877f096a61ee5d060fba70b4d180986ad828&x-api-eid-token=jdd034JN7IR3VHS5PPDULQJMCAFGKR6QFULJJ4MYZ2YCIU4VON356GFCTATLBLYYX4GIRT7NAYRKSBAH5PXGL2R7Z3743XMAAAAMJPAZJFMAAAAAACJWKVZLOYRD4K4X&loginType=3&uuid=125919621.1689938728638330604939.1689938729.1689938729.1689938729.1",
            "scheme": "https",
            "accept": "application/json, text/javascript, */*; q=0.01",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9",
            "cookie": "shshshfpb=d8nTAEyqCJTpxqADATh-ddQ; __jda=125919621.1689938728638330604939.1689938729.1689938729.1689938729.1; __jdb=125919621.1.1689938728638330604939|1.1689938729; __jdc=125919621; __jdv=125919621|direct|-|none|-|1689938728639",
            "origin": "https://item.jd.com",
            "referer": "https://item.jd.com/",
            "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"8\"",
            "sec-ch-ua-mobile": "?0",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.1.4031 SLBChan/30",
            "x-referer-page": f"https://item.jd.com/{value}.html",
            "x-rp-client": "h5_1.0.0"
        }, {
            "authority": "api.m.jd.com",
            "method": "GET",
            "path": f"/?appid=pc-item-soa&functionId=pc_detailpage_wareBusiness&client=pc&clientVersion=1.0.0&t={t}&body=%7B%22skuId%22%3A{value}%2C%22cat%22%3A%2213314%2C21909%2C21921%22%2C%22area%22%3A%2215_1213_3038_59931%22%2C%22shopId%22%3A%221000300492%22%2C%22venderId%22%3A1000300492%2C%22paramJson%22%3A%22%7B%5C%22platform2%5C%22%3A%5C%22100000000001%5C%22%2C%5C%22specialAttrStr%5C%22%3A%5C%22p0ppppppppp2ppppppppppp1ppp%5C%22%2C%5C%22skuMarkStr%5C%22%3A%5C%2200%5C%22%7D%22%2C%22num%22%3A1%2C%22bbTraffic%22%3A%22%22%7D&h5st=20230721192534711%3B8333628654621072%3Bfb5df%3Btk03w91c71ac518nJq8FXiwUdNhqVCpa6bTEqQ9333loO6THJhAm1f5_xo1jrfSxD6SS4X7Wt3Gt6-NhJH9G7-TaGDJS%3Bb41e1fd7a217fe4c9cb37c9eb479a8695fb76df4ef84aa67d0c526bf74d4a620%3B3.1%3B1689938734711%3B24c9ee85e67cf80746dd82817ecbeafc7a829b35c7f446a4c7d476cc9faa1d8834a93323ad7bce9bef1bba682b93d2e3d7f70cc2e6f7e902188e8a3640d207da74bc7d8c7d6ad6b0545db33c1aca877f096a61ee5d060fba70b4d180986ad828&x-api-eid-token=jdd034JN7IR3VHS5PPDULQJMCAFGKR6QFULJJ4MYZ2YCIU4VON356GFCTATLBLYYX4GIRT7NAYRKSBAH5PXGL2R7Z3743XMAAAAMJPAZJFMAAAAAACJWKVZLOYRD4K4X&loginType=3&uuid=125919621.1689938728638330604939.1689938729.1689938729.1689938729.1",
            "scheme": "https",
            "accept": "application/json, text/javascript, */*; q=0.01",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9",
            "cookie": "shshshfpb=d8nTAEyqCJTpxqADATh-ddQ; __jda=125919621.1689938728638330604939.1689938729.1689938729.1689938729.1; __jdb=125919621.1.1689938728638330604939|1.1689938729; __jdc=125919621; __jdv=125919621|direct|-|none|-|1689938728639",
            "origin": "https://item.jd.com",
            "referer": "https://item.jd.com/",
            "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"8\"",
            "sec-ch-ua-mobile": "?0",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.1.4031 SLBChan/30",
            "x-referer-page": f"https://item.jd.com/{value}.html",
            "x-rp-client": "h5_1.0.0"
        }]

        t = 0
        li = [5]
        while 1:
            k += 1
            if k == 10:
                k = 0
            # print(k)
            try:
                time.sleep(random.choice(li))
                # t += 1
                # if t == 2:
                #     time.sleep(5)
                #     t = 0

                print(proxies[k])
                e = requests.get(url=url, headers=headers[random.choice(range(0, 4))], proxies=proxies[k])
                r = e.json()
                print(r)
                if 'extendWarrantyInfo' in r:
                    print(num - gai)
                    break
                if 'extendWarrantyInfo' not in r:
                    time.sleep(50)

            except:
                t += 1
                # if t == 1:
                #     time.sleep(2)
                if t == 2:
                    time.sleep(3)
                if t == 3:
                    time.sleep(5)
                    t = 0
                # print(e)

        type = first_column[num]
        pp = second_column[num]
        num += 1
        try:
            name = r['wareInfo']['wname'].replace(',', ' ')
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
        with open('列表_1.csv', 'a', newline='', encoding='gb18030') as f:
            f.write(f'{value}, {imag}, {name}, {type}, {pp}, {price}, {youhui}, {zhichi}\n')


if __name__ == '__main__':
    ip_dai()
    jd()
