# -*- coding: utf-8 -*-
# @Time    : 2017/12/26 12:37
# @Author  : play4fun
# @File    : PriorityResource优先等级资源.py
# @Software: PyCharm

"""
PriorityResource优先等级资源.py:
"""
import simpy


def resource_user(name, env, resource, wait, prio):
    yield env.timeout(wait)
    with resource.request(priority=prio) as req:
        print('%s requesting at %s with priority=%s' % (name, env.now, prio))
        yield req
        print('%s got resource at %s' % (name, env.now))
        yield env.timeout(3)


env = simpy.Environment()
res = simpy.PriorityResource(env, capacity=1)
p1 = env.process(resource_user(1, env, res, wait=0, prio=0))
p2 = env.process(resource_user(2, env, res, wait=1, prio=2))
p3 = env.process(resource_user(3, env, res, wait=2, prio=-1))
env.run()
