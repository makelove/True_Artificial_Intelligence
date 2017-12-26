# -*- coding: utf-8 -*-
# @Time    : 2017/12/26 18:56
# @Author  : play4fun
# @File    : Stores.py
# @Software: PyCharm

"""
Stores.py:
"""

import simpy


def producer(env, store):
    for i in range(100):
        yield env.timeout(2)
        yield store.put('spam猪肉 %s' % i)
        print('商店 Produced spam猪肉 at', env.now)


def consumer(name, env, store):
    while True:
        yield env.timeout(1)
        print('客户', name, 'requesting spam猪肉 at t', env.now)
        item = yield store.get()
        print('客户', name, 'got', item, 'at t', env.now)


env = simpy.Environment()
store = simpy.Store(env, capacity=2)

prod = env.process(producer(env, store))
consumers = [env.process(consumer(i, env, store)) for i in range(2)]

# env.run(until=15)


# 可以使用FilterStore对机器具有不同属性的机器商店进行建模。如果资源的同类插槽不是您所需要的，这可能很有用
from collections import namedtuple

Machine = namedtuple('Machine', 'size, duration')
m1 = Machine(1, 2)  # Small and slow
m2 = Machine(2, 1)  # Big and fast

env = simpy.Environment()
machine_shop = simpy.FilterStore(env, capacity=2)
machine_shop.items = [m1, m2]  # Pre-populate the machine shop


def user(name, env, ms, size):
    machine = yield ms.get(lambda machine: machine.size == size)
    print(name, 'got', machine, 'at', env.now)
    yield env.timeout(machine.duration)
    yield ms.put(machine)
    print(name, 'released', machine, 'at', env.now)


users = [env.process(user(i, env, machine_shop, (i % 2) + 1))
         for i in range(3)]
# env.run()


#通过a PriorityStore，我们可以模拟不同优先级的项目。在以下示例中，检查员进程查找并记录单独维护人员进程按优先级顺序修复的问题。
env = simpy.Environment()
issues = simpy.PriorityStore(env)


def inspector(env, issues):
    for issue in [simpy.PriorityItem('P2', '#0000'),
                  simpy.PriorityItem('P0', '#0001'),
                  simpy.PriorityItem('P3', '#0002'),
                  simpy.PriorityItem('P1', '#0003')]:
        yield env.timeout(1)
        print(env.now, 'log', issue)
        yield issues.put(issue)


def maintainer(env, issues):
    while True:
        yield env.timeout(3)
        issue = yield issues.get()
        print(env.now, 'repair', issue)


_ = env.process(inspector(env, issues))
_ = env.process(maintainer(env, issues))
env.run()
