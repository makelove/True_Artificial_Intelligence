# -*- coding: utf-8 -*-
# @Time    : 2017/12/26 19:47
# @Author  : play4fun
# @File    : 将监视恰好适合一个用例.py
# @Software: PyCharm

"""
将监视恰好适合一个用例.py:
另一个极端是将监视恰好适合一个用例。想象一下，例如，您只想知道一次有多少个进程在等待Resource
"""

import simpy


class MonitoredResource(simpy.Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = []

    def request(self, *args, **kwargs):
        self.data.append((self._env.now, len(self.queue)))
        return super().request(*args, **kwargs)

    def release(self, *args, **kwargs):
        self.data.append((self._env.now, len(self.queue)))
        return super().release(*args, **kwargs)


def test_process(env, res):
    with res.request() as req:
        yield req
        yield env.timeout(1)


env = simpy.Environment()

res = MonitoredResource(env, capacity=1)
p1 = env.process(test_process(env, res))
p2 = env.process(test_process(env, res))
env.run()

print(res.data)
