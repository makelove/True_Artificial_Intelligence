# -*- coding: utf-8 -*-
# @Time    : 2017/12/26 10:32
# @Author  : play4fun
# @File    : 共享资源-电动车.py
# @Software: PyCharm

"""
共享资源-电动车.py:
"""

def print_queue(env,bcs):#打印队列
    while True:
        print(f'\t{env.now }:{len(bcs.users)} ,{bcs.count}\t',end=',')
        for user_req in bcs.users:
            print('\t\t',user_req,user_req.proc)
        yield env.timeout(1)

def car(env, name, bcs, driving_time, charge_duration):
    # Simulate driving to the BCS
    yield env.timeout(driving_time)

    # Request one of its charging spots
    print('%s arriving at %d' % (name, env.now))
    with bcs.request() as req:  # 资源的request()方法会生成一个事件，让您等待资源再次可用。如果你被恢复，你将“拥有”资源，直到你释放它。
        yield req

        # Charge the battery
        print('%s starting to charge at %s' % (name, env.now))

        yield env.timeout(charge_duration)
        print('%s leaving the bcs at %s' % (name, env.now))
    # print(bcs.queue)


import simpy

env = simpy.Environment()
bcs = simpy.Resource(env, capacity=3)  # 电池充电站,可以同时给2辆车充电
env.process(print_queue(env,bcs))
for i in range(6):
    env.process(car(env, 'Car %d' % i, bcs, i * 2, 5))

env.run(until=25)
