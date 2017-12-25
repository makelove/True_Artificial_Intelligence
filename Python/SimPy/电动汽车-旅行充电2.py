# -*- coding: utf-8 -*-
# @Time    : 2017/12/25 23:28
# @Author  : play4fun
# @File    : 电动汽车-旅行充电.py
# @Software: PyCharm

"""
电动汽车-旅行充电.py:中断interrupt()
你不想等到你的电动汽车充满电，而是想中断充电过程，而开始驾驶。

SimPy允许您通过调用其interrupt()方法来中断正在运行的进程
"""


class Car(object):
    def __init__(self, env):
        self.env = env
        # Start the run process everytime an instance is created.
        self.action = env.process(self.run())

    def run(self):
        while True:
            print('Start parking and charging at %d' % self.env.now)
            charge_duration = 5
            # We may get interrupted while charging the battery

            try:

                yield self.env.process(self.charge(charge_duration))
            except simpy.Interrupt:
                # When we received an interrupt, we stop charging and
                # switch to the "driving" state
                print('Was interrupted. Hope, the battery is full enough ')

            print('Start driving at %d' % self.env.now)
            trip_duration = 2
            yield self.env.timeout(trip_duration)

    def charge(self, duration):
        yield self.env.timeout(duration)


def driver(env, car):
    while True:
        yield env.timeout(3)
        car.action.interrupt()


import simpy

# env = simpy.Environment()
# car = Car(env)
# env.run(until=35)

env = simpy.Environment()
car = Car(env)
env.process(driver(env, car))
env.run(until=35)
