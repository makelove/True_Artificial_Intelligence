# -*- coding: utf-8 -*-
# @Time    : 2017/12/26 12:39
# @Author  : play4fun
# @File    : PreemptiveResource抢占资源.py
# @Software: PyCharm

"""
PreemptiveResource抢占资源.py:
"""
import simpy


def resource_user(name, env, resource, wait, prio):
    yield env.timeout(wait)
    with resource.request(priority=prio) as req:
        print('%s requesting at %s with priority=%s' % (name, env.now, prio))
        yield req
        print('%s got resource at %s' % (name, env.now))
        try:
            yield env.timeout(3)
        except simpy.Interrupt as interrupt:
            by = interrupt.cause.by
            usage = env.now - interrupt.cause.usage_since
            print('%s got preempted by %s at %s after %s' %
                  (name, by, env.now, usage))


env = simpy.Environment()
res = simpy.PreemptiveResource(env, capacity=1)
p1 = env.process(resource_user(1, env, res, wait=0, prio=0))
p2 = env.process(resource_user(2, env, res, wait=1, prio=2))
p3 = env.process(resource_user(3, env, res, wait=2, prio=-1))
# env.run()


#

def user(name, env, res, prio, preempt):
    with res.request(priority=prio, preempt=preempt) as req:
        try:
            print('%s requesting at %d' % (name, env.now))
            yield req
            print('%s got resource at %d' % (name, env.now))
            yield env.timeout(3)
        except simpy.Interrupt:
            print('%s got preempted at %d' % (name, env.now))


env = simpy.Environment()
res = simpy.PreemptiveResource(env, capacity=1)
# A = env.process(user('A', env, res, prio=0, preempt=True))
# env.run(until=1)  # Give A a head start

#
B = env.process(user('B', env, res, prio=-2, preempt=False))
C = env.process(user('C', env, res, prio=-1, preempt=True))
env.run()
