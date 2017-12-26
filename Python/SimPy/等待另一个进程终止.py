# -*- coding: utf-8 -*-
# @Time    : 2017/12/26 12:18
# @Author  : play4fun
# @File    : 等待另一个进程终止.py
# @Software: PyCharm

"""
等待另一个进程终止.py:

上面的例子有一个问题：可能发生的情况是车辆要停放的时间比为电池充电所需要的时间短（如果充电和停车都需要60到90分钟，则是这种情况）。

要解决这个问题，我们必须稍微改变我们的模型。bat_ctrl() 每次电动汽车开始停车时，都会启动新功能。电动车然后等待，直到停车持续时间结束，直到停止充电：

"""
from random import seed, randint
import simpy

class EV:
    def __init__(self, env):
        self.env = env
        self.drive_proc = env.process(self.drive(env))

    def drive(self, env):
        while True:
            # Drive for 20-40 min
            yield env.timeout(randint(20, 40))

            # Park for 1–6 hours
            print('Start parking at', env.now)
            charging = env.process(self.bat_ctrl(env))
            parking = env.timeout(randint(60, 360))
            yield charging & parking
            print('Stop parking at', env.now)

    def bat_ctrl(self, env):
        print('Bat. ctrl. started at', env.now)
        # Intelligent charging behavior here …
        yield env.timeout(randint(30, 90))
        print('Bat. ctrl. done at', env.now)


env = simpy.Environment()
ev = EV(env)
env.run(until=410)
