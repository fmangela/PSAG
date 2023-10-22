# PSAG/小学算数题生成器
Primary School Arithmetic Generator

## 项目介绍/Project Introduction
小学计算题生成器是一个用Python编写的简单工具，旨在帮助小学生练习他们的算术技能。这个项目可以随机生成各种小学阶段的算术题目，包括加法、减法、乘法和除法，供给小学生作为家庭作业或课后练习。

The primary school calculation question generator is a simple tool written in Python, which aims to help primary school students practice their arithmetic skills. This project can generate various 

通过使用这个工具，学生可以加强他们的数学技能，提高对数字和算术规则的理解。题目难度可以根据需要进行调整，以适应不同年级和能力水平的学生。

By using this tool, students can strengthen their mathematical skills and improve their understanding of numbers and arithmetic rules. The difficulty of the questions can be adjusted according to needs to adapt to students of different grades and ability levels.

这个项目的特点包括：/
The characteristics of this project include:
1. 简单易用：用户友好界面，方便教师和学生使用。/Easy to use: user-friendly interface, convenient for teachers and students.
2. 随机生成：可以根据需要生成各种类型的算术题目。/Random generation: various types of arithmetic questions can be generated as required.
3. 自定义难度：可以调整题目难度，以适应不同年级和能力水平的学生。/User defined difficulty: the difficulty of the questions can be adjusted to adapt to students of different grades and ability levels.
4. 保存和打印：生成的题目可以保存为文件或直接打印出来。/Save and print: the generated topic can be saved as a file or printed directly.
5. 统计分析：可以追踪学生的答题的情况，提供具有参考意义反馈和统计数据。/Statistical analysis: it can track students' answers and provide feedback and statistical data with reference significance.


## 使用方法/Usage
### python环境运行/Running in python environment
#### 环境需求/Environmental requirements
- python3.12+
- pip
#### 导包需求/Import package requirements
- pyinstaller *# 打包成可执行程序需要使用* /*# It needs to be used to package executable programs*
- openpyxl *# 输出为微软的xlsx文件使用，目前没用*/*# is output to Microsoft's xlsx file for use, but it is currently useless*
#### 运行程序/Run program
- pycharm
- vscode
- IDE
#### 可执行程序/Executable program
**1. 从release中下载打包好的可执行程序/Download the packaged executable program from release**

**2. 自己打包/Pack by yourself**

- 安装pyinstaller       /Install pyinstaller
- 定位目录/PSAG/src     /Locate directory/PSAG/src
- 在命令行中输入     /Enter on the command line
    ```
    pyinstaller begin.spec
    ```
- 相关配置已经写入begin.spec文件中了，可以直接打包/The relevant configuration has been written into the begin.spec file and can be packaged directly

## 功能介绍/Function introduction
### 选项卡1/Tab 1
- **出题答案的范围（大于等于0的整数）/Range of answers (integer greater than or equal to 0)**

- **算数题类型选择（加法，减法，乘法，除法，比较；除法带余数选项）/Arithmetic question type selection (addition, subtraction, multiplication, division, comparison; division with remainder option)**

- **出题数量（最多1000道题目）/Number of questions (up to 1000 questions)**

- **根据上面的参数，生成题目/Generate questions according to the above parameters**

- **生成题目和答案在主程序同目录下/The generated questions and answers are in the same directory as the main program**