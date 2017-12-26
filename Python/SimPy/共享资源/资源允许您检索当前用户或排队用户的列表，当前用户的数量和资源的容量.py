# -*- coding: utf-8 -*-
# @Time    : 2017/12/26 12:36
# @Author  : play4fun
# @File    : 资源允许您检索当前用户或排队用户的列表，当前用户的数量和资源的容量.py
# @Software: PyCharm

"""
资源允许您检索当前用户或排队用户的列表，当前用户的数量和资源的容量.py:
"""
import simpy
env = simpy.Environment()
res = simpy.Resource(env, capacity=1)


def print_stats(res):
    print('%d of %d slots are allocated.' % (res.count, res.capacity))
    print('  Users:', res.users)
    print('  Queued events:', res.queue)


def user(res):
    print_stats(res)
    with res.request() as req:
        yield req
        print_stats(res)
    print_stats(res)


procs = [env.process(user(res)), env.process(user(res))]
env.run()
