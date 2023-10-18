"""
@Project Description:The main function of this project is to generate arithmetic problems for children to practice
@项目描述：这个项目主要功能是生成算数题给小朋友做练习
"""
# import库
from functools import wraps
import tkinter as tk
from tkinter import ttk
# from tkinter import messagebox
import random
# import pandas as pd
# from openpyxl import Workbook
from Algorithm_Packet import (Plus_Calculation_Generator, Minus_Calculation_Generator, Multiply_Calculation_Generator,
                              Divide_Calculation_Generator, Compare_Calculation_Generator)
from IO_Stream import text_file_output


class MainWindow:
    """
    MainWindow根类，包含窗口的建立方法
    使用MainWindow.run()方法运行窗口
    """
    # 选项卡1的参数
    start_entry = None
    end_entry = None
    plus_check_var = None
    minus_check_var = None
    multiply_check_var = None
    divide_check_var = None
    compare_check_var = None
    remainder_check_var = None
    exercises_num_entry = None
    generate_button = None
    output_text1 = None
    remainder_check = None

    def __init__(self, root_window):
        """
        初始化函数，将界面全部创建起来
        :param root_window:
        """
        self.root_window = root_window
        root_window.title("PSAG")
        # root_window.geometry("300x400")
        # 创建选项卡
        notebook = ttk.Notebook(self.root_window)
        self.tab1, self.tab2, self.tab3, self.tab4, self.tab5, self.tab6, self.settings_tab\
            = self.init_notebook(notebook)
        notebook.pack(expand=True, fill='both')
        # 初始化各选项卡内容
        self.init_tab1(self.tab1)
        self.init_tab2(self.tab2)
        self.init_tab3(self.tab3)

    @staticmethod
    def init_notebook(notebook):
        """
        创建选项卡
        :return: tab1,tab2,tab3,tab4,tab5,tab6,settings_tab
        """
        tab1 = ttk.Frame(notebook)
        notebook.add(tab1, text="一年级")
        tab2 = ttk.Frame(notebook)
        notebook.add(tab2, text="二年级")
        tab3 = ttk.Frame(notebook)
        notebook.add(tab3, text="三年级")
        tab4 = ttk.Frame(notebook)
        notebook.add(tab4, text="四年级")
        tab5 = ttk.Frame(notebook)
        notebook.add(tab5, text="五年级")
        tab6 = ttk.Frame(notebook)
        notebook.add(tab6, text="六年级")
        settings_tab = ttk.Frame(notebook)
        notebook.add(settings_tab, text="设置")

        return tab1, tab2, tab3, tab4, tab5, tab6, settings_tab

    def init_tab1(self, tab1):
        """
        选项卡1的主要界面内容
        创建窗口中的各个模块和按钮
        self目前仅将函数generate_func传入
        """
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
        self.start_entry = tk.Entry(range_frame)
        self.start_entry.insert(0, "1")
        self.start_entry.grid(column=1, row=1, padx=3, pady=5)
        end_label = tk.Label(range_frame, text="终止数字：", font=("YaHei", 12))
        end_label.grid(column=0, row=2, sticky='we', padx=3, pady=5)
        self.end_entry = tk.Entry(range_frame)
        self.end_entry.insert(0, "10")
        self.end_entry.grid(column=1, row=2, sticky='we', padx=3, pady=5)

        # 生成一个出题参数的frame框，放入选项卡内
        parameter_frame = tk.Frame(tab1, borderwidth=1, relief="solid")
        parameter_frame.grid(column=0, row=1, sticky='we', padx=5, pady=5)

        # 生成一个label，名称为"出题参数"
        parameter_label = tk.Label(parameter_frame, text="出题参数", font=("YaHei", 12))
        parameter_label.grid(column=0, row=0, sticky='we', padx=3, pady=3)

        # 添加出题参数多选项
        # 加法运算选项
        self.plus_check_var = tk.IntVar()
        plus_check = tk.Checkbutton(
            parameter_frame,
            text="加法运算",
            variable=self.plus_check_var,
            onvalue=1,
            offvalue=0
        )
        self.plus_check_var.set(1)
        plus_check.grid(column=0, row=1, sticky='we', padx=3, pady=3)

        # 减法运算选项
        self.minus_check_var = tk.IntVar()
        minus_check = tk.Checkbutton(
            parameter_frame,
            text="减法运算",
            variable=self.minus_check_var,
            onvalue=1,
            offvalue=0
        )
        minus_check.grid(column=1, row=1, sticky='we', padx=3, pady=3)

        # 乘法运算选项
        self.multiply_check_var = tk.IntVar()
        multiply_check = tk.Checkbutton(
            parameter_frame,
            text="乘法运算",
            variable=self.multiply_check_var,
            onvalue=1,
            offvalue=0
        )
        multiply_check.grid(column=0, row=2, sticky='we', padx=3, pady=3)

        # 除法运算选项
        self.divide_check_var = tk.IntVar()
        divide_check = tk.Checkbutton(
            parameter_frame,
            text="除法运算",
            variable=self.divide_check_var,
            onvalue=1,
            offvalue=0,
            command=self.checkbutton_state_change
        )
        divide_check.grid(column=1, row=2, sticky='we', padx=3, pady=3)

        # 比较运算选项
        self.compare_check_var = tk.IntVar()
        compare_check = tk.Checkbutton(
            parameter_frame,
            text="比较运算",
            variable=self.compare_check_var,
            onvalue=1,
            offvalue=0
        )
        compare_check.grid(column=2, row=1, sticky='we', padx=3, pady=3)

        # 除法运算是否要留余数
        self.remainder_check_var = tk.IntVar()
        self.remainder_check = tk.Checkbutton(
            parameter_frame,
            text="余数运算",
            variable=self.remainder_check_var,
            onvalue=1,
            offvalue=0,
            state="disabled"
        )
        self.remainder_check.grid(column=2, row=2, sticky='we', padx=3, pady=3)

        # 生成一个出题数量的frame框，放入选项卡内
        exercises_num_frame = tk.Frame(tab1, borderwidth=1, relief="solid")
        exercises_num_frame.grid(column=0, row=2, sticky='we', padx=5, pady=5)
        # 生成一个label，名称为"出题数量"
        exercises_num_label = tk.Label(exercises_num_frame, text="出题数量", font=("YaHei", 12))
        exercises_num_label.grid(column=0, row=0, sticky='we', padx=3, pady=3)
        # 添加出题数量
        self.exercises_num_entry = tk.Entry(exercises_num_frame)
        self.exercises_num_entry.insert(0, "10")
        self.exercises_num_entry.grid(column=1, row=0, sticky='we', padx=3, pady=3)

        # 生成按钮
        self.generate_button = tk.Button(tab1, text="生成题目", command=self.generate_func)
        self.generate_button.grid(column=0, row=3, sticky='sew', padx=5, pady=5)

        # 输出对话框
        text_frame = tk.Frame(tab1, borderwidth=1, relief="solid")
        text_frame.grid(column=0, row=4, sticky='we', padx=5, pady=5)
        self.output_text1 = tk.Text(text_frame, width=30, height=5, state='disabled')
        self.output_text1.grid(column=0, row=1, sticky='we', padx=5, pady=5)
        output_scrollbar = tk.Scrollbar(text_frame, command=self.output_text1.yview)
        output_scrollbar.grid(row=1, column=1, sticky='ns')
        self.output_text1['yscrollcommand'] = output_scrollbar.set

    def init_tab2(self, tab2):
        """
        选项卡2的主要界面内容
        创建窗口中的各个模块和按钮
        """
        pass

    def init_tab3(self, tab3):
        pass

    def init_tab4(self, tab4):
        pass

    def init_tab5(self, tab5):
        pass

    def init_tab6(self, tab6):
        pass

    def init_settings_tab(self, settings_tab):
        pass

    # 快速函数传入text对象和需要输出的字
    @staticmethod
    def text_output_func(text, output_str):
        text.configure(state='normal')
        text.insert('end', output_str)
        text.configure(state='disabled')

    # 装饰函数，用于按下按钮后将按钮置不可操作状态
    def disable_button_during_generation(func):
        """
        一个类内的装饰器函数，需要import wraps装饰器函数
        功能: 装饰一个按钮，在工作的之后将按钮变为不可按状态，工作结束后放开
        :param func: 装饰的函数
        :return: 装饰后的函数
        """
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            self.generate_button.configure(state='disabled')
            result = func(self, *args, **kwargs)
            self.generate_button.configure(state='normal')
            return result
        return wrapper

    @disable_button_during_generation
    def generate_func(self):
        """
        该函数用于根据用户输入的参数生成题目，并将题目写入xlsx文件中
        :return:
        """
        # 开始运行
        self.text_output_func(self.output_text1, "----------\n")
        # 获取参数
        self.text_output_func(self.output_text1, "正在获取参数\n")
        start_num = self.start_entry.get()
        end_num = self.end_entry.get()
        choose_plus = self.plus_check_var.get()
        choose_minus = self.minus_check_var.get()
        choose_multiply = self.multiply_check_var.get()
        choose_divide = self.divide_check_var.get()
        choose_compare = self.compare_check_var.get()
        choose_remainder = self.remainder_check_var.get()
        exercises_num = self.exercises_num_entry.get()

        # 验证参数正确性
        self.text_output_func(self.output_text1, "正在验证参数准确性\n")
        if start_num.isdigit():
            start_num = int(start_num)
            if start_num < 0:
                self.text_output_func(self.output_text1, "起始数字请输入大于0的数\n")
                return
        else:
            self.text_output_func(self.output_text1, "起始数字输入错误，请重新输入\n")
            return
        if end_num.isdigit():
            end_num = int(end_num)
        else:
            self.text_output_func(self.output_text1, "终止数字输入错误，请重新输入\n")
            return
        if start_num > end_num:
            self.text_output_func(self.output_text1, "起始数字必须小于终止数字，请重新输入\n")
            return
        if exercises_num.isdigit():
            exercises_num = int(exercises_num)
            if exercises_num < 1 or exercises_num > 1000:
                self.text_output_func(self.output_text1, "出题数量输入错误，请重新输入\n")
                return
        else:
            self.text_output_func(self.output_text1, "出题数量输入错误，请重新输入\n")
            return
        if choose_plus != 1 and choose_plus != 0:
            self.text_output_func(self.output_text1, "内部错误，请联系管理员\n")
            return
        if choose_minus != 1 and choose_minus != 0:
            self.text_output_func(self.output_text1, "内部错误，请联系管理员\n")
            return
        if choose_multiply != 1 and choose_multiply != 0:
            self.text_output_func(self.output_text1, "内部错误，请联系管理员\n")
            return
        if choose_divide != 1 and choose_divide != 0:
            self.text_output_func(self.output_text1, "内部错误，请联系管理员\n")
            return
        if choose_compare != 1 and choose_compare != 0:
            self.text_output_func(self.output_text1, "内部错误，请联系管理员\n")
            return
        if choose_remainder != 1 and choose_remainder != 0:
            self.text_output_func(self.output_text1, "内部错误，请联系管理员\n")
            return
        # 一定要勾选算法题目
        if not(choose_plus or choose_minus or choose_multiply or choose_divide or choose_compare):
            self.text_output_func(self.output_text1, "请至少选择一项算法\n")
            return

        # 生成题目
        self.text_output_func(self.output_text1, "正在生成题目\n")
        # 选择参数做成数学运算字典
        method_dict = {"plus": choose_plus, "minus": choose_minus, "multiply": choose_multiply, "divide": choose_divide,
                       "compare": choose_compare}

        # 平均分配题目数量
        method_count = sum(method_dict.values())
        base_counts = exercises_num // method_count
        base_counts_remain = exercises_num % method_count
        filtered_method_dict = {k: v for k, v in method_dict.items() if v == 1}
        # 算数方法都赋值基础的出题数量
        filtered_method_count_dict = {key: base_counts for key in filtered_method_dict}
        # get做法可能会有None值出来
        plus_method_count = filtered_method_count_dict.get("plus")
        if plus_method_count is None:
            plus_method_count = 0
        minus_method_count = filtered_method_count_dict.get("minus")
        if minus_method_count is None:
            minus_method_count = 0
        multiply_method_count = filtered_method_count_dict.get("multiply")
        if multiply_method_count is None:
            multiply_method_count = 0
        divide_method_count = filtered_method_count_dict.get("divide")
        if divide_method_count is None:
            divide_method_count = 0
        compare_method_count = filtered_method_count_dict.get("compare")
        if compare_method_count is None:
            compare_method_count = 0
        # 随机抽取中余数匹配算法数量
        if len(filtered_method_count_dict) >= base_counts_remain:
            remain_method_lst = random.sample(filtered_method_count_dict.keys(), base_counts_remain)
        else:
            self.text_output_func(self.output_text1, "算法错误，请联系管理员\n")
            return
        for i in remain_method_lst:
            if i == "plus":
                plus_method_count += 1
            elif i == "minus":
                minus_method_count += 1
            elif i == "multiply":
                multiply_method_count += 1
            elif i == "divide":
                divide_method_count += 1
            elif i == "compare":
                compare_method_count += 1
        # 平均出题数量算法验证
        if not(exercises_num == sum([plus_method_count, minus_method_count,
                                     multiply_method_count, divide_method_count, compare_method_count])):
            self.text_output_func(self.output_text1, "算法错误，请联系管理员\n")
            return

        # 送算法生成器生成题目
        if plus_method_count > 0:
            plus_g = Plus_Calculation_Generator.Level1PlusGenerator(start_num, end_num, plus_method_count)
            plus_questions, plus_answers = plus_g.generate()
        else:
            plus_questions = ()
            plus_answers = ()
        if minus_method_count > 0:
            minus_g = Minus_Calculation_Generator.Level1MinusGenerator(start_num, end_num, minus_method_count)
            minus_questions, minus_answers = minus_g.generate()
        else:
            minus_questions = ()
            minus_answers = ()
        if multiply_method_count > 0:
            multi_g = Multiply_Calculation_Generator.Level1MultiplyGenerator(start_num, end_num, multiply_method_count)
            multi_questions, multi_answers = multi_g.generate()
        else:
            multi_questions = ()
            multi_answers = ()
        if divide_method_count > 0:
            divide_g = Divide_Calculation_Generator.Level1DivideGenerator(start_num, end_num, divide_method_count)
            divide_questions, divide_answers = divide_g.generate(choose_remainder)
        else:
            divide_questions = ()
            divide_answers = ()
        if compare_method_count > 0:
            compare_g = Compare_Calculation_Generator.Level1CompareGenerator(start_num, end_num, compare_method_count)
            compare_questions, compare_answers = compare_g.generate(choose_plus, choose_minus, choose_multiply,
                                                                    choose_divide)
        else:
            compare_questions = ()
            compare_answers = ()

        # 整形
        questions = (list(plus_questions) + list(minus_questions) + list(multi_questions) +
                     list(divide_questions) + list(compare_questions))
        random.shuffle(questions)
        answers = (list(plus_answers) + list(minus_answers) + list(multi_answers) +
                   list(divide_answers) + list(compare_answers))
        random.shuffle(answers)

        # 输出题目与答案
        self.text_output_func(self.output_text1, "正在生成文件\n")
        q_out = text_file_output.TxtFileOut()
        q_out.write_txt_file(filename="题目.txt", data=questions)
        a_out = text_file_output.TxtFileOut()
        a_out.write_txt_file(filename="答案.txt", data=answers)
        self.text_output_func(self.output_text1, "题目答案生成成功，请在程序目录下查阅\n")
        self.text_output_func(self.output_text1, "----------\n")
        return

    def checkbutton_state_change(self):
        if self.divide_check_var.get() == 0:
            self.remainder_check.configure(state="disabled")
        else:
            self.remainder_check.configure(state="normal")

if __name__ == "__main__":
    """
    主要执行程序
    """
    root = tk.Tk()
    main_window = MainWindow(root)
    root.mainloop()
