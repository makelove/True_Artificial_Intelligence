# -*- coding: utf-8 -*-
# @Time    : 2017/12/26 18:38
# @Author  : play4fun
# @File    : Containers.py
# @Software: PyCharm

"""
Containers.py:
"""

import simpy

class GasStation:
    def __init__(self, env):
        self.fuel_dispensers = simpy.Resource(env, capacity=2)
        self.gas_tank = simpy.Container(env, init=100, capacity=1000)
        self.mon_proc = env.process(self.monitor_tank(env))

    def monitor_tank(self, env):
        while True:
            if self.gas_tank.level < 100:
                print('\tCalling tanker at %s' % env.now)
                env.process(tanker(env, self))
            yield env.timeout(15)


def tanker(env, gas_station):
    yield env.timeout(10)  # Need 10 Minutes to arrive
    print('\tTanker arriving at %s' % env.now)
    amount = gas_station.gas_tank.capacity - gas_station.gas_tank.level
    yield gas_station.gas_tank.put(amount)
    print('\tTanker finished at %s' % env.now)


def car(name, env, gas_station):
    print('Car %s arriving at %s' % (name, env.now))
    with gas_station.fuel_dispensers.request() as req:
        yield req
        print('Car %s starts refueling at %s' % (name, env.now))
        yield gas_station.gas_tank.get(40)
        yield env.timeout(5)
        print('Car %s done refueling at %s' % (name, env.now))


def car_generator(env, gas_station):
    for i in range(160):
        env.process(car(i, env, gas_station))
        yield env.timeout(5)


env = simpy.Environment()
gas_station = GasStation(env)
car_gen = env.process(car_generator(env, gas_station))
env.run(1135)
