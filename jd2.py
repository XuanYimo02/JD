import random

import openpyxl
import requests
from openpyxl import worksheet


def jd():
    # value = 100014212478
    value =10072436421360



    workbook = openpyxl.load_workbook('皮肤用药.xlsx')

    worksheet = workbook.worksheets[0]  # 根据索引选择
    first_column = [cell.value for cell in worksheet['A']]
    second_column = [cell.value for cell in worksheet['B']]
    third_column = [cell.value for cell in worksheet['C']]
    headers = {
        "Origin": "https://item.yiyaojd.com",
        # "Origin": "https://item.jd.com",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        # "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "X-Referer-Page": f"https://item.yiyaojd.com/{value}.html",
        "X-Rp-Client": "h5_1.0.0"
    }
    t = int(random.random() * 1000000000)
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

    # for i in range(10):

    url = f'https://api.m.jd.com/?appid=pc-item-soa&functionId=pc_detailpage_wareBusiness&client=pc&clientVersion=1.0.0&t=1689078234457&body=%7B%22skuId%22%3A{value}%2C%22cat%22%3A%2213314%2C21909%2C21921%22%2C%22area%22%3A%2215_1213_3038_59931%22%2C%22shopId%22%3A%221000015441%22%2C%22venderId%22%3A1000015441%2C%22paramJson%22%3A%22%7B%5C%22platform2%5C%22%3A%5C%22100000000001%5C%22%2C%5C%22specialAttrStr%5C%22%3A%5C%22p0ppp1pppppp2ppppppppppp1ppp%5C%22%2C%5C%22skuMarkStr%5C%22%3A%5C%2200%5C%22%7D%22%2C%22num%22%3A1%2C%22bbTraffic%22%3A%22%22%7D&h5st=20230711202354499%3B2628994075236133%3Bfb5df%3Btk03wa0021bb918niO1lTFMmjM5huxtv9p1QafKdoGE9rH7FEKFFUy1MGbAgYIJLBBYBoMoxSlI9fATpGSaPFPK2rvOT%3B961c13a4978bca762a95fe67662fa2f8b89a384cb5ce18fc597bdc136c8eea8f%3B3.1%3B1689078234499%3B24c9ee85e67cf80746dd82817ecbeafc7a829b35c7f446a4c7d476cc9faa1d8834a93323ad7bce9bef1bba682b93d2e39660ae8d453e3b0662c62666381aa5f076aaf79dcd3c545165153dc06d071a59b57c4150e88cce87de6b3c3847d40d3c&x-api-eid-token=jdd03OPG4EXSGXN6WBCEYLMW7IMXKWBDH6DI7WWONS4IWRTHO2Y66KTI54PS4DWDBPYQFKVOQCMZ5ROBV33RLDRW2YAS62UAAAAMJITTLPVQAAAAADYI4FG4KTWBRFQX&loginType=3&uuid=125919621.16890670765522085068047.1689067077.1689075586.1689078119.4'
    while 1:
        try:
            r = requests.get(url=url, headers=headers).json()
            break
        except:
            pass
    print(r)
    num = 18634
    type = first_column[num]
    pp = second_column[num]
    num += 1
    # try:
    name = r['wareInfo']['wname']
    # except:
    #     continue
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
    with open('列表1.csv', 'w', newline='') as f:
        f.write(f'{value}, {imag}, {name}, {type}, {pp}, {price}, {youhui}, {zhichi}\n')


if __name__ == '__main__':
    jd()
