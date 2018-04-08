# -*- coding: utf-8 -*-
# @Time    : 2017/12/29 17:49
# @Author  : play4fun
# @File    : test1.py
# @Software: PyCharm

"""
test1.py:
"""
import os

with open('test.log','a+') as f:
    f.write('helloworld')
    print(f)