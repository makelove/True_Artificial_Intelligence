# -*- coding: utf-8 -*-
# @Time    : 2017/12/26 12:21
# @Author  : play4fun
# @File    : 中断另一个进程.py
# @Software: PyCharm

"""
中断另一个进程.py:

像往常一样，我们现在还有另外一个问题：想象一下，一趟是非常紧急的，但是在目前的实施中，我们总是需要等到电池充满电。如果我们能以某种方式打断

幸运的巧合，确实有办法做到这一点。你可以打电话 interrupt()给一个Process。这将会抛出 Interrupt异常，立即恢复：

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

            # Park for 1 hour
            print('Start parking at', env.now)
            charging = env.process(self.bat_ctrl(env))
            parking = env.timeout(60)
            yield charging | parking
            if not charging.triggered:
                # Interrupt charging if not already done.
                charging.interrupt('Need to go!')
            print('Stop parking at', env.now)

    def bat_ctrl(self, env):
        print('Bat. ctrl. started at', env.now)
        try:
            yield env.timeout(randint(60, 90))
            print('Bat. ctrl. done at', env.now)
        except simpy.Interrupt as i:
            # Onoes! Got interrupted before the charging was done.
            print('Bat. ctrl. interrupted at', env.now, 'msg:',
                  i.cause)


env = simpy.Environment()
ev = EV(env)
env.run(until=100)
