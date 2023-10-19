"""
此包功能为数据分析生成的算术式，其数字分布情况，并做出分析
为了微调加减乘除算法
"""


class Analyzer:
    """
    分析器类
    """
    answers = None

    def __init__(self, answers):
        self.answers = answers

    def str_to_chart(self):
        import re
        a = []
        b = []
        c = []
        for i in self.answers:
            digits = re.findall(r'\d+', i)
            for j in range(len(digits)):
                if j % 3 == 0:
                    a.append(int(digits[j]))
                elif j % 3 == 1:
                    b.append(int(digits[j]))
                elif j % 3 == 2:
                    c.append(int(digits[j]))
        return a, b, c

    def print_out(self, a, b, c):
        print(f"总计题目{len(a)}道")
        print(f"a值分布：")
        count_dict = self.count_duplicates(a)
        for item, count in count_dict.items():
            print(f"元素 {item} 占比 {100 * count / len(a)}%")
        print(f"b值分布：")
        count_dict = self.count_duplicates(b)
        for item, count in count_dict.items():
            print(f"元素 {item} 占比 {100 * count / len(b)}%")
        print(f"c值分布：")
        count_dict = self.count_duplicates(c)
        for item, count in count_dict.items():
            print(f"元素 {item} 占比 {100 * count / len(c)}%")

    @staticmethod
    def count_duplicates(sequence):
        count_dict = {}
        for item in sequence:
            if item in count_dict:
                count_dict[item] += 1
            else:
                count_dict[item] = 1
        return count_dict
