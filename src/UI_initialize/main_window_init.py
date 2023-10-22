"""
此为主窗口初始化包
"""
# import库
from functools import wraps
import tkinter as tk
from tkinter import ttk
import random
from . import tab1_init


class MainWindow:
    """
    MainWindow根类，包含窗口的建立方法
    使用MainWindow.run()方法运行窗口
    """

    def __init__(self, root_window):
        """
        初始化函数，将界面全部创建起来
        :param root_window:
        """
        self.root_window = root_window
        root_window.title("PSAG")
        # root_window.geometry("300x400")
        # 创建选项卡工作簿
        notebook = ttk.Notebook(self.root_window)
        self.tab1, self.tab2, self.tab3, self.tab4, self.tab5, self.tab6, self.settings_tab\
            = self.init_notebook(notebook)
        notebook.pack(expand=True, fill='both')
        # 初始化各选项卡内容
        # 创建选项卡1的类，并调用函数
        tab1_init.Tab1(self.tab1)
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
