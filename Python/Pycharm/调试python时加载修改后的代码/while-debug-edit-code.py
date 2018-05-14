# -*- coding: utf-8 -*-
# @Time    : 2018/5/7 14:18
# @Author  : play4fun
# @File    : while-debug-edit-code.py
# @Software: PyCharm

"""
while-debug-edit-code.py:
"""

test_value = [10,54,2,8,7,6,4,3,2,1]
# test_value = [10,54,2,8,7,6,4,3,2,1]

for i in range(0,10):
    if test_value[i] == i:
        print ("found the value: " + i)