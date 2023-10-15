"""
@Project Description:The main function of this project is to generate arithmetic problems for children to practice
@项目描述：这个项目主要功能是生成算数题给小朋友做练习
"""
# import库
import tkinter as tk
from tkinter import ttk
import random
import pandas as pd
# from openpyxl import Workbook


# 生成随机数的函数
def generate_random_numbers():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    return num1, num2


# 生成加法题目的函数
def generate_addition_question():
    num1, num2 = generate_random_numbers()
    question = f"What is {num1} + {num2}?"
    answer = num1 + num2
    return question, answer


# 将题目和答案保存到DataFrame，然后导出到xlsx文件的函数
def export_to_xlsx(questions, answers):
    df = pd.DataFrame(questions, columns=["Question"])
    df["Answer"] = answers
    df.to_excel("math_questions.xlsx", index=False)


# 生成题目并导出的函数
def generate_and_export_questions(num_questions):
    questions = []
    answers = []
    for _ in range(num_questions):
        question, answer = generate_addition_question()
        questions.append(question)
        answers.append(answer)
    export_to_xlsx(questions, answers)


class MainWindow:
    """
    MainWindow根类，包含窗口的建立方法
    使用MainWindow.run()方法运行窗口
    """
    # def __init__(self):
    #     pass

    # @staticmethod
    def run(self):
        """
        运行窗口函数，调用tkinter中的各种方法
        创建窗口中的各个模块和按钮
        不返回值
        """
        # 创建窗口
        root_window = tk.Tk()
        root_window.title("PSAG")
        # 定义窗口大小
        root_window.geometry("300x400")

        # 创建选项卡窗口
        notebook = ttk.Notebook(root_window)
        # 添加一个选项卡，名称为"一年级"
        tab1 = ttk.Frame(notebook)
        notebook.add(tab1, text='一年级')
        # 放入主窗口中
        notebook.pack(expand=True, fill='both')

        # 生成一个出题范围的frame框，放入选项卡内
        range_frame = tk.Frame(tab1, borderwidth=1, relief="solid")
        # range_frame.pack(side='top', fill="x")
        range_frame.grid(column=0, row=0, sticky='we', padx=5, pady=5)
        # 生成一个label，名称为"出题范围"
        range_label = tk.Label(range_frame, text="出题范围",  font=("YaHei", 12))
        range_label.grid(column=0, row=0, sticky='we', padx=3, pady=5)
        # 生成两个entry，名称分别为起始和终止，放在同一行
        start_label = tk.Label(range_frame, text="起始数字：", font=("YaHei", 12))
        start_label.grid(column=0, row=1, sticky='we', padx=3, pady=5)
        start_entry = tk.Entry(range_frame)
        start_entry.grid(column=1, row=1, padx=3, pady=5)
        end_label = tk.Label(range_frame, text="终止数字：", font=("YaHei", 12))
        end_label.grid(column=0, row=2, sticky='we', padx=3, pady=5)
        end_entry = tk.Entry(range_frame)
        end_entry.grid(column=1, row=2, sticky='we', padx=3, pady=5)

        # 生成一个出题参数的frame框，放入选项卡内
        parameter_frame = tk.Frame(tab1, borderwidth=1, relief="solid")
        parameter_frame.grid(column=0, row=1, sticky='we', padx=5, pady=5)
        # 生成一个label，名称为"出题参数"
        parameter_label = tk.Label(parameter_frame, text="出题参数", font=("YaHei", 12))
        parameter_label.grid(column=0, row=0, sticky='we', padx=3, pady=3)
        # 添加出题参数多选项
        # 加法运算选项
        plus_check_var = tk.IntVar()
        plus_check = tk.Checkbutton(
            parameter_frame,
            text="加法运算",
            variable=plus_check_var,
            onvalue=1,
            offvalue=0
        )
        plus_check.grid(column=0, row=1, sticky='we', padx=3, pady=3)
        # 减法运算选项
        minus_check_var = tk.IntVar()
        minus_check = tk.Checkbutton(
            parameter_frame,
            text="减法运算",
            variable=minus_check_var,
            onvalue=1,
            offvalue=0
        )
        minus_check.grid(column=1, row=1, sticky='we', padx=3, pady=3)
        # 乘法运算选项
        multiply_check_var = tk.IntVar()
        multiply_check = tk.Checkbutton(
            parameter_frame,
            text="乘法运算",
            variable=multiply_check_var,
            onvalue=1,
            offvalue=0
        )
        multiply_check.grid(column=0, row=2, sticky='we', padx=3, pady=3)
        # 除法运算选项
        divide_check_var = tk.IntVar()
        divide_check = tk.Checkbutton(
            parameter_frame,
            text="除法运算",
            variable=divide_check_var,
            onvalue=1,
            offvalue=0
        )
        divide_check.grid(column=1, row=2, sticky='we', padx=3, pady=3)
        # 比较运算选项
        compare_check_var = tk.IntVar()
        compare_check = tk.Checkbutton(
            parameter_frame,
            text="比较运算",
            variable=compare_check_var,
            onvalue=1,
            offvalue=0
        )
        compare_check.grid(column=2, row=1, sticky='we', padx=3, pady=3)

        # 生成一个出题数量的frame框，放入选项卡内
        exercises_num_frame = tk.Frame(tab1, borderwidth=1, relief="solid")
        exercises_num_frame.grid(column=0, row=2, sticky='we', padx=5, pady=5)
        # 生成一个label，名称为"出题参数"
        exercises_num_label = tk.Label(exercises_num_frame, text="出题数量", font=("YaHei", 12))
        exercises_num_label.grid(column=0, row=0, sticky='we', padx=3, pady=3)
        # 添加出题数量
        exercises_num_entry = tk.Entry(exercises_num_frame)
        exercises_num_entry.grid(column=1, row=0, sticky='we', padx=3, pady=3)

        # 生成按钮
        generate_button = tk.Button(tab1, text="生成题目", command=self.generate_func)
        generate_button.grid(column=0, row=3, sticky='sew', padx=5, pady=5)

        # 使窗口保持运营
        root_window.mainloop()

    def generate_func(self):
        pass


if __name__ == "__main__":
    """
    主要执行程序
    """
    main_window = MainWindow()
    main_window.run()
