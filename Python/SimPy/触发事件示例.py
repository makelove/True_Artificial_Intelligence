# -*- coding: utf-8 -*-
# @Time    : 2017/12/26 11:45
# @Author  : play4fun
# @File    : 触发事件示例.py
# @Software: PyCharm

"""
触发事件示例.py:
"""


class School:
    def __init__(self, env):
        self.env = env
        self.class_ends = env.event()
        self.pupil_procs = [env.process(self.pupil()) for i in range(3)]
        self.bell_proc = env.process(self.bell())

    def bell(self):
        for i in range(2):
            yield self.env.timeout(45)
            self.class_ends.succeed()
            self.class_ends = self.env.event()
            print('bell rings')

    def pupil(self):
        for i in range(2):
            print(' \o/', end='\t')
            yield self.class_ends


import simpy

env = simpy.Environment()
school = School(env)
env.run()

'''
def sub(env):
    yield env.timeout(1)
    return 23


def parent(env):
    ret = yield env.process(sub(env))
    return ret


env.run(env.process(parent(env)))
'''
