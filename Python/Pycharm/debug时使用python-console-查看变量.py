# -*- coding: utf-8 -*-
# @Time    : 2018/4/30 13:54
# @Author  : play4fun
# @File    : debug时使用python-console-查看变量.py
# @Software: PyCharm

"""
debug时使用python-console-查看变量.py:
"""

from datetime import datetime
from time import sleep

now = datetime.now()

counter = 10
while True:
    print('\nnow', now)
    now = datetime.now()

    for x in range(20):
        y = x ^ 2
        print(y, end=',')
    print('counter:',counter)
    sleep(4)
    if counter == 0:
        break
    else:
        counter -= 1
