# -*- coding: utf-8 -*-
# @Time    : 2017/12/26 19:09
# @Author  : play4fun
# @File    : 实时模拟.py
# @Software: PyCharm

"""
实时模拟.py:

有时候，你可能不想尽可能快地进行模拟，但是与墙上时钟同步。这种模拟也被称为 实时模拟。

实时模拟可能是必要的

如果你有硬件在环，
如果有人与你的模拟交互，或者
如果你想分析一个算法的实时行为。
为了将模拟转换为实时模拟，您只需要将SimPy的默认值Environment替换为simpy.rt.RealtimeEnvironment。除了initial_time 说法，有两个附加参数：因子和严格的： 。RealtimeEnvironment(initial_time=0, factor=1.0, strict=True)

该因子定义了仿真时间的每一步实时传递的数量。默认情况下，这是一秒钟。如果你设定factor=0.1，一个模拟时间单位只需要十分之一秒。如果你设置factor=60，这将需要一分钟。

这里是一个简单的例子，用于将正常模拟转换为每个模拟时间单位十分之一秒的实时模拟：
"""

import time
import simpy


def example(env):
    start = time.perf_counter()
    yield env.timeout(1)
    end = time.perf_counter()
    print('Duration of one simulation time unit: %.2fs' % (end - start))


# env = simpy.Environment()
# proc = env.process(example(env))
# env.run(until=proc)
# Duration of one simulation time unit: 0.00s

import simpy.rt

env = simpy.rt.RealtimeEnvironment(factor=0.1)
proc = env.process(example(env))
# env.run(until=proc)
# Duration of one simulation time unit: 0.10s


#
import time
import simpy.rt


def slow_proc(env):
    time.sleep(0.02)  # Heavy computation :-)
    yield env.timeout(1)


# env = simpy.rt.RealtimeEnvironment(factor=0.01)
env = simpy.rt.RealtimeEnvironment(factor=0.01, strict=False)
proc = env.process(slow_proc(env))
try:
    env.run(until=proc)
    print('Everything is alright')
except RuntimeError:
    print('Simulation is too slow')
