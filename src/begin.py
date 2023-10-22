"""
@Project Description:The main function of this project is to generate arithmetic problems for children to practice
@项目描述：这个项目主要功能是生成算数题给小朋友做练习
"""
import tkinter as tk
from UI_initialize import main_window_init


def get_path(relative_path):
    """
    get the absolute path of the relative path
    :param relative_path:
    :return: path
    """
    import os
    import sys
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.normpath(os.path.join(base_path, relative_path))


if __name__ == "__main__":
    """
    主要执行程序
    """
    root = tk.Tk()
    root.wm_iconbitmap(get_path('image/calcu.ico'))
    main_window = main_window_init.MainWindow(root)
    root.resizable(False, False)
    root.mainloop()
