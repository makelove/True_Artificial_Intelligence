# -*- coding: utf-8 -*-
# @Time    : 2017/12/25 23:16
# @Author  : play4fun
# @File    : car_park.py
# @Software: PyCharm

"""
car_park.py:
停车场
"""


def car(env):
    while True:
        print('Start parking at %d' % env.now)
        parking_duration = 5
        yield env.timeout(parking_duration)

        print('Start driving at %d' % env.now)
        trip_duration = 2
        yield env.timeout(trip_duration)


import simpy

env = simpy.Environment()
env.process(car(env))
env.run(until=15)
