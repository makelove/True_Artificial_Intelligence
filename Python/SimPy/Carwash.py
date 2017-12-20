# -*- coding: utf-8 -*-
# @Time    : 2017/12/20 19:33
# @Author  : play4fun
# @File    : Carwash.py
# @Software: PyCharm

"""
Carwash.py:
"""

"""
洗车问题示例.

知识点:
- 等待其它流程
- 资源

场景介绍:
  一个有特定洗车机的洗车房，并且洗车流程会消耗随机长度的时间。
  Car流程为，车到达洗车房，如果有空闲的洗车机，就立刻开始洗车，如果没有，就等待直到
  有洗车机空闲下来。
"""
import random
import simpy

RANDOM_SEED = 42
NUM_MACHINES = 3  # 洗车房中洗车机的数量
WASHTIME = 5  # 使用洗车机洗车所需的时间，分钟
T_INTER = 3  # 来车的间隔时间，约7分钟
SIM_TIME = 30  # 总的模拟时间


class Carwash(object):
    """
    一个洗车房，拥有特定数量的洗车机。 一个车首先申请洗车机。当来车申请到洗车机后
    就可以开始洗车流程，并且在等待指定的洗车时间后完成洗车。
    """

    def __init__(self, env, num_machines, washtime):
        self.env = env
        self.machine = simpy.Resource(env, num_machines)
        self.washtime = washtime

    def wash(self, car):
        """洗车流程。它使用一个car流程并试着清洗它。"""
        yield self.env.timeout(WASHTIME)
        print("正在洗车Carwash removed %d%% of %s's dirt." %
              (random.randint(50, 99), car))


def car(env, name, cw):
    """
    洗车 流程 (每辆车都有一个名字) 每辆车会到达洗车房(``cw``) 并申请洗车机.
    然后开始洗车流程，等待洗车的完成然后离开再不回来...
    """
    print('%s arrives at the carwash at %.2f.到达' % (name, env.now))
    with cw.machine.request() as request:
        yield request

        print('%s enters the carwash at %.2f.进入' % (name, env.now))
        yield env.process(cw.wash(name))

        print('%s leaves the carwash at %.2f.离开' % (name, env.now))


def setup(env, num_machines, washtime, t_inter):
    """创建一个洗车房，几个初始车辆，然后持续创建车辆到达. 每隔``t_inter`` 分钟."""
    # 创建洗车房
    carwash = Carwash(env, num_machines, washtime)

    # 创建4个初始车辆
    for i in range(4):
        env.process(car(env, 'Car %d' % i, carwash))

    # 在仿真过程中持续创建车辆
    while True:
        yield env.timeout(random.randint(t_inter - 2, t_inter + 2))
        i += 1
        env.process(car(env, 'Car %d' % i, carwash))


# 初始化并开始仿真
print('Carwash开始仿真')
print('Check out http://youtu.be/fXXmeP9TvBg while simulating ... ;-)')
random.seed(RANDOM_SEED)  # This helps reproducing the results

# 创建一个环境并开始仿真
env = simpy.Environment()
env.process(setup(env, NUM_MACHINES, WASHTIME, T_INTER))

# 开始执行!
env.run(until=SIM_TIME)
