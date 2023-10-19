"""
这是比较算术题生成器的算法核心
主要功能是：
    传入题目范围（起始，终止）、出题数量
    返回题目列表（字符串）
    返回答案列表（字符串）
"""
import abc
import random


class CompareCalculationGenerator(metaclass=abc.ABCMeta):
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


class Level1CompareGenerator(CompareCalculationGenerator):
    """
    一年级简答算术题生成器
    特点：
        没有负数
        没有小数点
        带0
    """
    def __init__(self, start, end, count):
        super().__init__(start, end, count)

    def generate(self, pl, mi, mu, di):
        """
        生成题目
        """
        n = 0
        questions = []
        answers = []
        while n < self.count:
            m = random.randint(1, 5)
            if m == 1 and pl:
                # 加法题
                a = random.randint(self.start, self.end)
                b = random.randint(self.start, self.end)
                c = random.randint(self.start, self.end)
                n += 1
                questions.append(f"{a} + {b} [ ] {c}")
                if a + b > c:
                    answers.append(f"{a} + {b} > {c}")
                elif a + b < c:
                    answers.append(f"{a} + {b} < {c}")
                else:
                    answers.append(f"{a} + {b} = {c}")
                continue
            elif m == 2 and mi:
                # 减法题
                a = random.randint(self.start, self.end)
                b = random.randint(self.start, a)
                c = random.randint(self.start, self.end)
                n += 1
                questions.append(f"{a} - {b} [ ] {c}")
                if a - b > c:
                    answers.append(f"{a} - {b} > {c}")
                elif a - b < c:
                    answers.append(f"{a} - {b} < {c}")
                else:
                    answers.append(f"{a} - {b} = {c}")
                continue
            elif m == 3 and mu:
                # 乘法题
                a = random.randint(self.start, self.end)
                b = random.randint(self.start, self.end)
                c = random.randint(self.start, self.end)
                n += 1
                questions.append(f"{a} × {b} [ ] {c}")
                if a * b > c:
                    answers.append(f"{a} × {b} > {c}")
                elif a * b < c:
                    answers.append(f"{a} × {b} < {c}")
                else:
                    answers.append(f"{a} × {b} = {c}")
                continue
            elif m == 4 and di:
                # 除法题
                a = random.randint(self.start, self.end)
                b = random.randint(1, a)
                c = random.randint(self.start, self.end)
                n += 1
                questions.append(f"{a} ÷ {b} [ ] {c}")
                if a / b > c:
                    answers.append(f"{a} ÷ {b} > {c}")
                elif a / b < c:
                    answers.append(f"{a} ÷ {b} < {c}")
                else:
                    answers.append(f"{a} ÷ {b} = {c}")
                continue
            elif m == 5:
                # 光比较
                a = random.randint(self.start, self.end)
                b = random.randint(self.start, self.end)
                n += 1
                questions.append(f"{a} [ ] {b} ")
                if a > b:
                    answers.append(f"{a} > {b}")
                elif a < b:
                    answers.append(f"{a} < {b}")
                else:
                    answers.append(f"{a} = {b}")
                continue

        return tuple(questions), tuple(answers)


if __name__ == "__main__":
    """
    本地测试函数
    """
    cls_A = Level1CompareGenerator(0, 100, 10000)
    import Calculation_Analyzer

    anal = Calculation_Analyzer.Analyzer(cls_A.generate(1, 0, 0, 0)[1])
    a, b, c = anal.str_to_chart()
    print_out = anal.print_out(a, b, c)
