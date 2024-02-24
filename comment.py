# Python作业
# 日期:2023/7/12 18:21
# File:comment
# Author 比窦娥还冤
# 清华镜像源: pip install -i https://pypi.tuna.tsinghua.edu.cn/simple
import random

import openpyxl
import requests


def jd():
    workbook = openpyxl.load_workbook('end.xlsx')

    worksheet = workbook.worksheets[0]  # 根据索引选择

    A_column = [cell.value for cell in worksheet['A']]
    B_column = [cell.value for cell in worksheet['B']]
    C_column = [cell.value for cell in worksheet['C']]
    D_column = [cell.value for cell in worksheet['D']]
    E_column = [cell.value for cell in worksheet['E']]
    F_column = [cell.value for cell in worksheet['F']]
    G_column = [cell.value for cell in worksheet['G']]
    H_column = [cell.value for cell in worksheet['H']]
    with open('comment_3.csv', 'w', newline='') as f:
        f.write("商品sku,商品链接图片,标题,商品类别,商品品牌,价格,促销,支持,用户名称,会员级别,评论内容,评论图片链接,用户评分,商品标题,商品sku,评论时间,用户所在城市,点赞数\n")
    gai = 1
    idex = gai - 1
    for value in A_column[gai:]:
        idex += 1
        print(idex)
        # value = 10036116511304
        # url = f'https://item.jd.com/10031528895911.html#comment'
        # url = f'https://item.jd.com/{value}.html#comment'
        for page in range(0, 100):
            t = int(random.random() * 1000000000)
            url = f'https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t={t}&loginType=3&uuid=122270672.16890670765522085068047.1689067077.1689151442.1689154959.7&productId={value}&score=0&sortType=5&page={page}&pageSize=10&isShadowSku=0&rid=0&fold=1&bbtf=&shield='
            r = requests.get(url).json()
            # print(page)
            try:
                comment_list = r['comments']
            except:
                comment_list = []
            if page == 0 and len(comment_list) != 10:
                num = 0
                for list in comment_list:
                    num += 1
                    uname = list['nickname'].replace(',', '，')
                    plusAvailable = list['plusAvailable']
                    if plusAvailable == 201:
                        plusAvailable = 'PLUS会员'
                    else:
                        plusAvailable = '普通用户'
                    comment = list['content'].replace('\r\n', ' ').replace('\n', ' ').replace(',', ' ')
                    try:
                        image_list = list['images']
                    except:
                        image_list = []
                    imgUrl = ''
                    for image in image_list:
                        imgUrl += 'https' + image['imgUrl'] + '  '
                    score = list['score']
                    productColor = list['productColor'].replace(',', ' ').replace('\n', ' ')
                    referenceId = list['referenceId']
                    creationTime = list['creationTime']
                    try:
                        location = list['location']
                    except:
                        location = ''
                    usefulVoteCount = list['usefulVoteCount']
                    with open('comment_3.csv', 'a', newline='', encoding='gb18030') as f:
                        f.write(
                            f"{referenceId},{B_column[idex]},{productColor},{D_column[idex]},{E_column[idex]},{F_column[idex]},{G_column[idex]},{H_column[idex]},{uname},{plusAvailable},{comment},{imgUrl},{score},{C_column[idex]},{value},{creationTime},{location},{usefulVoteCount}\n")
                print(f"num={num}")
                for i in range(num, 10):
                    with open('comment_3.csv', 'a', newline='', encoding='gb18030') as f:
                        f.write(" , , , , , , , , , ,此用户未填写评价内容, , , , , , , \n")
                break
            if len(comment_list) == 0:
                break
            for list in comment_list:
                uname = list['nickname'].replace(',', '，')
                plusAvailable = list['plusAvailable']
                if plusAvailable == 201:
                    plusAvailable = 'PLUS会员'
                else:
                    plusAvailable = '普通用户'
                comment = list['content'].replace('\r\n', ' ').replace('\n', ' ').replace(',', ' ')
                try:
                    image_list = list['images']
                except:
                    image_list = []
                imgUrl = ''
                for image in image_list:
                    imgUrl += 'https' + image['imgUrl'] + '  '
                score = list['score']
                productColor = list['productColor'].replace(',', ' ').replace('\n', ' ')
                referenceId = list['referenceId']
                creationTime = list['creationTime']
                try:
                    location = list['location']
                except:
                    location = ''
                usefulVoteCount = list['usefulVoteCount']

                with open('comment_3.csv', 'a', newline='', encoding='gb18030') as f:
                    f.write(
                        f"{referenceId},{B_column[idex]},{productColor},{D_column[idex]},{E_column[idex]},{F_column[idex]},{G_column[idex]},{H_column[idex]},{uname},{plusAvailable},{comment},{imgUrl},{score},{C_column[idex]},{value},{creationTime},{location},{usefulVoteCount}\n")


if __name__ == '__main__':
    jd()
