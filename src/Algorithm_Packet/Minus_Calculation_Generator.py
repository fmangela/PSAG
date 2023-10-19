"""
这是减法算术题生成器的算法核心
主要功能是：
    传入题目范围（起始，终止）、出题数量
    返回题目列表（字符串）
    返回答案列表（字符串）
"""
import abc
import random


class MinusCalculationGenerator(metaclass=abc.ABCMeta):
    """
    父类
    """
    def __init__(self, start, end, count):
        self.start = start
        self.end = end
        self.count = count

    @abc.abstractmethod
    def generate(self):
        pass


class Level1MinusGenerator(MinusCalculationGenerator):
    """
    一年级简单算术题生成器
    特点：
        没有负数
        没有小数点
        带0
    """
    def __init__(self, start, end, count):
        super().__init__(start, end, count)

    def generate(self):
        """
        生成题目
        """
        n = 0
        questions = []
        answers = []
        while n < self.count:
            c = random.randint(self.start, self.end)
            a = random.randint(c, self.end)
            b = a - c
            n += 1
            questions.append(f"{a} - {b} = ")
            answers.append(f"{a} - {b} = {c}")
        return tuple(questions), tuple(answers)


if __name__ == "__main__":
    """
    本地测试函数
    """
    cls_A = Level1MinusGenerator(10, 100, 10000)
    import Calculation_Analyzer
    anal = Calculation_Analyzer.Analyzer(cls_A.generate()[1])
    a, b, c = anal.str_to_chart()
    print_out = anal.print_out(a, b, c)
