# -*- coding: utf-8 -*-
# @Time    : 2017/12/26 11:29
# @Author  : play4fun
# @File    : 返回值.py
# @Software: PyCharm

"""
返回值.py:
"""


def other_proc(env):
    ret_val = yield env.process(my_proc(env))
    assert ret_val == 41  # 42


def my_proc(env):
    yield env.timeout(1)
    env.exit(42)  # Py2 equivalent to "return 42"


import simpy

env = simpy.Environment()
# env.process(other_proc(env))
other_proc(env)

# ret_val = env.process(my_proc(env))
# assert ret_val == 42  # 42
