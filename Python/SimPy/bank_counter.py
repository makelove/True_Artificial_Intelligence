# -*- coding: utf-8 -*-
# @Time    : 2017/12/20 19:26
# @Author  : play4fun
# @File    : bank_counter.py
# @Software: PyCharm

"""
bank_counter.py:
"""

"""
银行柜台排队问题

知识点:
- 资源
- 条件事件

场景:
  A counter with a random service time and customers who renege. Based on the
  program bank08.py from TheBank tutorial of SimPy 2. (KGM)
  一个银行柜台，其服务耗时随机分布，客户会因费时长而离开。
"""
import random
import simpy

RANDOM_SEED = 42
NEW_CUSTOMERS = 15  # 总的客户人数
INTERVAL_CUSTOMERS = 10.0  # 新的客户每隔大约10秒钟出现一位
MIN_PATIENCE = 1  # 最低耐心值
MAX_PATIENCE = 3  # 最高耐心值


def source(env, number, interval, counter):
    """本函数随机生成客户"""
    for i in range(number):
        c = customer(env, 'Customer%02d' % i, counter, time_in_bank=12.0)
        env.process(c)
        t = random.expovariate(1.0 / interval)
        yield env.timeout(t)


def customer(env, name, counter, time_in_bank):
    """客户流程函数，客户到来，接受服务或者不耐烦，最后离开."""
    arrive = env.now
    print('%7.4f %s: Here I am我来了' % (arrive, name))

    with counter.request() as req:
        patience = random.uniform(MIN_PATIENCE, MAX_PATIENCE)
        # Wait for the counter or abort at the end of our tether
        results = yield req | env.timeout(patience)

        wait = env.now - arrive

        if req in results:
            # 得到服务
            print('%7.4f %s: Waited %6.3f 等啊等' % (env.now, name, wait))

            tib = random.expovariate(1.0 / time_in_bank)
            yield env.timeout(tib)
            print('%7.4f %s: Finished 完成' % (env.now, name))

        else:
            # 不耐烦离开
            print('%7.4f %s: RENEGED after %6.3f 不耐烦离开' % (env.now, name, wait))


# 初始化然后开始模拟
print('Bank renege开始模拟')
random.seed(RANDOM_SEED)
env = simpy.Environment()

# 开始流程函数并运行
counter = simpy.Resource(env, capacity=1)
env.process(source(env, NEW_CUSTOMERS, INTERVAL_CUSTOMERS, counter))
env.run()
