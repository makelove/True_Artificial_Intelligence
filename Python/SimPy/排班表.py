# -*- coding: utf-8 -*-
# @Time    : 2017/12/20 20:05
# @Author  : play4fun
# @File    : 排班表.py
# @Software: PyCharm

"""
排班表.py:
"""

import simpy

PROCESS_TIME = 2

def put_item(env, store):
    for i in range(20):
        yield env.timeout(0.5)
        store.put(f"{i}_item")

def process(env, store, resource):
    while True:
        item = yield store.get()
        with resource.request() as req:
            yield req
            yield env.timeout(PROCESS_TIME)

def set_resource(env, resource, start_time, end_time):
    """占用资源，模拟资源减少的情况，
    end_time 会出现 np.inf 无穷大，
    simpy 只会用作为排序，可以放在timeout事件里。
    """
    duration = end_time - start_time
    yield env.timeout(start_time)
    with resource.request(priority=-1) as req:
        yield req
        yield env.timeout(duration)

env = simpy.Environment()
store = simpy.Store(env)
res = simpy.PriorityResource(env, 10)

res_time_table = [(10, 20, 5), (20, 30, 6)]
env.process(put_item(env, store))
env.process(process(env, store, res))

for start, end, target_num in res_time_table:
    place_holder = 10 - target_num
    for _ in range(place_holder):
        env.process(set_resource(env, res, start, end))

env.run()