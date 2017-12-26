# -*- coding: utf-8 -*-
# @Time    : 2017/12/26 11:04
# @Author  : play4fun
# @File    : Timeout_delay.py
# @Software: PyCharm

"""
Timeout_delay.py:
"""

import simpy


def example(env):
    event = simpy.events.Timeout(env, delay=2, value=42)
    value = yield event
    print('now=%d, value=%d' % (env.now, value))  # now=2, value=42


env = simpy.Environment()
# example_gen = example(env)
# p = simpy.events.Process(env, example_gen)
p = env.process(example(env))
env.run()
