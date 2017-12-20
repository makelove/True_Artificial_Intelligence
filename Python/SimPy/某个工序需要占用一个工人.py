# -*- coding: utf-8 -*-
# @Time    : 2017/12/20 20:12
# @Author  : play4fun
# @File    : 某个工序需要占用一个工人.py
# @Software: PyCharm

"""
某个工序需要占用一个工人.py:
https://zhuanlan.zhihu.com/p/32005127

"""

import simpy
import random

WORKERNUM = 10  # 工人数
PROCESS_TIME = 30 * 60  # 工序耗时, 使用秒作为单位
MEAN_ = 4 * 60  # 平均物件生成时间


def process(env, workers, store):
    """工序"""
    while True:
        with workers.request() as req:
            yield req
            item = yield store.get()
            print(f"{env.now} - {item} - start")
            yield env.timeout(PROCESS_TIME)
            print(f"{env.now} - {item} - done")


def put_item(env, store):
    """每隔一段时间生成一个物品"""
    for i in range(100):
        item = f"{i}_item"
        store.put(item)
        yield env.timeout(random.expovariate(1 / MEAN_))


env = simpy.Environment()
workers = simpy.Resource(env, 10)
store = simpy.Store(env)

env.process(process(env, workers, store))
env.process(put_item(env, store))
env.run()
