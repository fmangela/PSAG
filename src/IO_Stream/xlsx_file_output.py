"""
微软的表格文件输出生成包
"""
# import abc
# import pandas as pd
from openpyxl import Workbook


class XlsxFileOut:
    """
    xlsx文件输出类
    """
    def __init__(self):
        pass

    @staticmethod
    def write_xlsx_file(filename, data):
        # 创建一个对象
        workbook = Workbook()
        worksheet = workbook.active
        for i in data:
            worksheet.appand(i)
        workbook.save(filename)
