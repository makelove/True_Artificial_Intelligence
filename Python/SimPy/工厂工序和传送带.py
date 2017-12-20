# -*- coding: utf-8 -*-
# @Time    : 2017/12/20 19:46
# @Author  : play4fun
# @File    : 工厂工序和传送带.py
# @Software: PyCharm

"""
工厂工序和传送带.py:
https://zhuanlan.zhihu.com/p/31526894
"""

"""

工厂工序和传送带

情景:
    一个机器处理物件, 处理完毕后放上传送带, 传送带传送一段时间后到达下个一个机器设备.
    [last_q][machine1] ----[con_belt]----> [next_q][machine2]
"""

import simpy
import random

PROCESS_TIME = 0.5  # 处理时间
CON_BELT_TIME = 3  # 传送带时间
WORKER_NUM = 2  # 每个机器的工人数/资源数
MACHINE_NUM = 2  # 机器数
MEAN_TIME = 0.2  # 平均每个物件的到达时间间距


def con_belt_process(env,
                     con_belt_time,
                     package,
                     next_q):
    """模拟传送带的行为"""
    while True:
        print(f"{round(env.now, 2)} - item: {package} - start moving 开始移动")
        yield env.timeout(con_belt_time)  # 传送带传送时间
        next_q.put(package)
        print(f"{round(env.now, 2)} - item: {package} - end moving结束移动")
        env.exit()


def machine(env: simpy.Environment,
            last_q: simpy.Store,
            next_q: simpy.Store,
            machine_id: str):
    """模拟一个机器, 一个机器就可以同时处理多少物件 取决资源数(工人数)"""

    workers = simpy.Resource(env, capacity=WORKER_NUM)

    def process(item):
        """模拟一个工人的工作进程"""

        with workers.request() as req:
            yield req
            yield env.timeout(PROCESS_TIME)
            env.process(con_belt_process(env, CON_BELT_TIME, item, next_q))
            print(f'{round(env.now, 2)} - item: {item} - machine工人: {machine_id} - processed正在处理')

    while True:
        item = yield last_q.get()
        env.process(process(item))


def generate_item(env,
                  last_q: simpy.Store,
                  item_num: int = 100):
    """模拟物件的到达"""

    for i in range(item_num):
        print(f'{round(env.now, 2)} - item: item_{i} - created创建')
        last_q.put(f'item_{i}')
        t = random.expovariate(1 / MEAN_TIME)
        yield env.timeout(round(t, 1))


if __name__ == '__main__':

    # 实例环境
    env = simpy.Environment()
    # 设备前的物件队列
    last_q = simpy.Store(env)
    next_q = simpy.Store(env)

    env.process(generate_item(env, last_q))

    for i in range(MACHINE_NUM):
        env.process(machine(env, last_q, next_q, machine_id=f'm_{i}'))

    env.run()
