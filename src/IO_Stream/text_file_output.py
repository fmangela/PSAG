"""
文档文件输出生成包
"""
# import abc
# import pandas as pd


class TxtFileOut:
    """
    txt文件输出类
    """
    def __init__(self):
        pass

    @staticmethod
    def write_txt_file(filename, data):
        # 创建一个对象
        f = open(filename, 'w')
        # 写入数据
        for i in data:
            f.write(f"{i}\n")
        # 关闭文件
        f.close()
