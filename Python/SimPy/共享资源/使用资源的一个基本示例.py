# -*- coding: utf-8 -*-
# @Time    : 2017/12/26 12:33
# @Author  : play4fun
# @File    : 使用资源的一个基本示例.py
# @Software: PyCharm

"""
使用资源的一个基本示例.py:
"""

import simpy


def resource_user(env, resource):
    request = resource.request()  # Generate a request event
    yield request  # Wait for access
    yield env.timeout(1)  # Do something
    resource.release(request)  # Release the resource


env = simpy.Environment()
res = simpy.Resource(env, capacity=1)
user = env.process(resource_user(env, res))
env.run()
