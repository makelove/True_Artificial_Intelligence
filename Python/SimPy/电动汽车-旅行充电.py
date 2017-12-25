# -*- coding: utf-8 -*-
# @Time    : 2017/12/25 23:28
# @Author  : play4fun
# @File    : 电动汽车-旅行充电.py
# @Software: PyCharm

"""
电动汽车-旅行充电.py:
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
            # We yield the process that process() returns
            # to wait for it to finish
            yield self.env.process(self.charge(charge_duration))

            # The charge process has finished and
            # we can start driving again.
            print('Start driving at %d' % self.env.now)
            trip_duration = 2
            yield self.env.timeout(trip_duration)

    def charge(self, duration):
        yield self.env.timeout(duration)


import simpy

env = simpy.Environment()
car = Car(env)
env.run(until=35)
