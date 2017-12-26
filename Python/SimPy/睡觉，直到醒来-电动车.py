# -*- coding: utf-8 -*-
# @Time    : 2017/12/26 12:11
# @Author  : play4fun
# @File    : 睡觉，直到醒来-电动车.py
# @Software: PyCharm

"""
睡觉，直到醒来-电动车.py:
想象一下，你想要一个智能电池充电控制器的电动汽车模型。当车辆行驶时，控制器可以是被动的，但是一旦车辆连接到电网以便对电池充电，则需要重新激活。

"""
from random import seed, randint
import simpy

seed(23)


class EV:
    def __init__(self, env):
        self.env = env
        self.drive_proc = env.process(self.drive(env))
        self.bat_ctrl_proc = env.process(self.bat_ctrl(env))
        self.bat_ctrl_reactivate = env.event()

    def drive(self, env):
        while True:
            print('\t开车 at', env.now)
            # Drive for 20-40 min #随机
            yield env.timeout(randint(20, 40))

            # Park for 1–6 hours
            print('\tStart parking at', env.now)
            self.bat_ctrl_reactivate.succeed()  # "reactivate"
            self.bat_ctrl_reactivate = env.event()
            yield env.timeout(randint(60, 360))#停车
            print('\tStop parking at', env.now)

    def bat_ctrl(self, env):
        while True:
            print('Bat. ctrl. passivating钝化 at', env.now)
            yield self.bat_ctrl_reactivate  # "passivate"
            print('Bat. ctrl. reactivated再生 at', env.now)

            # Intelligent charging behavior here …
            yield env.timeout(randint(30, 90))


env = simpy.Environment()
ev = EV(env)
env.run(until=550)
