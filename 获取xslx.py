# Python作业
# 日期:2023/7/11 17:27
# File:获取xslx
# Author 比窦娥还冤
# 清华镜像源: pip install -i https://pypi.tuna.tsinghua.edu.cn/simple

import openpyxl


def jd():
    workbook = openpyxl.load_workbook('商品详情.xlsx')

    worksheet = workbook.worksheets[0]  # 根据索引选择

    first_column = [cell.value for cell in worksheet['A']]

    for value in first_column[1:]:
        print(value)
        url = f'https://item.yiyaojd.com/{value}.html'


if __name__ == '__main__':
    jd()
