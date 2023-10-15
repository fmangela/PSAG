"""
@Project Description:The main function of this project is to generate arithmetic problems for children to practice
@项目描述：这个项目主要功能是生成算数题给小朋友做练习
"""
# import库
import tkinter as tk
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


# 主要执行程序
if __name__ == "__main__":
    # GUI部分的代码
    root = tk.Tk()
    root.title("PSAG")

    # 生成题目数量输入框
    num_questions = tk.IntVar()
    num_questions_label = tk.Label(root, text="Number of questions:")
    num_questions_label.grid(row=0, column=0)
    num_questions_entry = tk.Entry(root)
    num_questions_entry.grid(row=0, column=1)

    # 生成按钮来生成题目
    generate_questions_button = tk.Button(
        root,
        text="Generate Questions",
        command=lambda: generate_and_export_questions(num_questions.get())
    )
    generate_questions_button.grid(row=1, column=0, columnspan=2)

    root.mainloop()



