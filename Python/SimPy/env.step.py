# -*- coding: utf-8 -*-
# @Time    : 2017/12/26 11:25
# @Author  : play4fun
# @File    : env.step.py
# @Software: PyCharm

"""
env.step.py:
"""
import simpy


def subfunc(env):
    print(env.active_process)  # will print "p1"


def my_proc(env):
    while True:
        print(env.active_process)  # will print "p1"
        subfunc(env)
        yield env.timeout(1)


env = simpy.Environment()
p1 = env.process(my_proc(env))
print(env.active_process,env.now)  # None
print(env.step(),env.now)
# <Process(my_proc) object at 0x>
# <Process(my_proc) object at 0x>
print(env.active_process,env.now)  # None
