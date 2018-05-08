# -*- coding: utf-8 -*-
# @Time    : 2018/5/8 21:58
# @Author  : play4fun
# @File    : demo2.py
# @Software: PyCharm

"""
demo2.py:扫描枪作为一个键盘输入
"""
try:
    while True:
        code = input('Scan:')
        print(code)
except KeyboardInterrupt:
    print('exit')
