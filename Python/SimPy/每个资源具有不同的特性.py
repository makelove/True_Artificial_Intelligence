# -*- coding: utf-8 -*-
# @Time    : 2017/12/25 23:01
# @Author  : play4fun
# @File    : 每个资源具有不同的特性.py
# @Software: PyCharm

"""
每个资源具有不同的特性.py:
https://ask.helplib.com/python/post_5296103
"""

import simpy


def user(machine):
    m = yield machine.get()
    print(m)
    yield machine.put(m)
    m = yield machine.get(lambda m: m['id'] == 1)
    print(m)
    yield machine.put(m)
    m = yield machine.get(lambda m: m['health'] > 98)
    print(m)
    yield machine.put(m)


env = simpy.Environment()
machine = simpy.FilterStore(env, 3)
machine.put({'id': 0, 'health': 100})
machine.put({'id': 1, 'health': 95})
machine.put({'id': 2, 'health': 97.2})
env.process(user(machine))
env.run()
