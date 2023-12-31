"""
这是除法算术题生成器的算法核心
主要功能是：
    传入题目范围（起始，终止）、出题数量
    返回题目列表（字符串）
    返回答案列表（字符串）
"""
import abc
import random


class DivideCalculationGenerator(metaclass=abc.ABCMeta):
    """
    父类
    """
    def __init__(self, start, end, count):
        self.start = start
        self.end = end
        self.count = count

    @abc.abstractmethod
    def generate(self, *args):
        pass


class Level1DivideGenerator(DivideCalculationGenerator):
    """
    一年级简单算术题生成器
    特点：
        没有负数
        没有小数点
        带0
    """
    def __init__(self, start, end, count):
        super().__init__(start, end, count)

    def generate(self, remainder):
        """
        生成题目
        """
        n = 0
        questions = []
        answers = []
        if remainder:  # 带余数的算式题
            while n < self.count:
                a = random.randint(self.start, self.end)
                b = random.randint(1, self.end)
                if a > b*2:
                    c = int(a // b)
                    re = int(a % b)
                    n += 1
                    questions.append(f"{a} ÷ {b} = ")
                    answers.append(f"{a} ÷ {b} = {c}...{re}")
            return tuple(questions), tuple(answers)
        else:  # 不带余数的算式题
            while n < self.count:
                a = random.randint(self.start, self.end)
                divisors = []
                for j in range(2, a):
                    if a % j == 0:
                        divisors.append(j)
                if divisors:
                    b = random.choice(divisors)
                    c = int(a / b)
                    n += 1
                    questions.append(f"{a} ÷ {b} = ")
                    answers.append(f"{a} ÷ {b} = {c}")
            return tuple(questions), tuple(answers)


if __name__ == "__main__":
    """
    本地测试函数
    """
    cls_A = Level1DivideGenerator(0, 100, 10000)
    import Calculation_Analyzer

    anal = Calculation_Analyzer.Analyzer(cls_A.generate(remainder=0)[1])
    a, b, c = anal.str_to_chart()
    print_out = anal.print_out(a, b, c)