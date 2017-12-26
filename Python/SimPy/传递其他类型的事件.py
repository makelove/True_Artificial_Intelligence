# -*- coding: utf-8 -*-
# @Time    : 2017/12/26 11:19
# @Author  : play4fun
# @File    : 传递其他类型的事件.py
# @Software: PyCharm

"""
传递其他类型的事件.py:
"""

import simpy


def my_proc(env):
    yield env.timeout(1)
    return 'Monty Python’s Flying Circus'


env = simpy.Environment()
proc = env.process(my_proc(env))
rs = env.run(until=proc)
print(rs)
# 'Monty Python’s Flying Circus'
