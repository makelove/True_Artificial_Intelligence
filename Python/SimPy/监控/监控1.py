# -*- coding: utf-8 -*-
# @Time    : 2017/12/26 19:33
# @Author  : play4fun
# @File    : 监控1.py
# @Software: PyCharm

"""
监控1.py:
监控是一个相对复杂的主题，有许多不同的用例和许多变化。

本指南提供了一些更常见和更有趣的内容。它的目的是给你一些提示和想法，你可以如何实现针对你的用例量身定制的模拟监控。

所以，在你开始之前，你需要定义它们：

什么，你想要做监控？

你的流程？
资源使用情况？
跟踪模拟的所有事件？
当你想监听？

定期按定义的时间间隔？
什么时候发生？
如何你想存储所收集的数据？

将它存储在一个简单的列表中？
记录到一个文件？
把它写入数据库？
"""

import simpy

data = []  # This list will hold all collected data


def test_process(env, data):
    val = 0
    for i in range(5):
        val += env.now
        data.append(val)  # Collect data
        yield env.timeout(1)


env = simpy.Environment()
p = env.process(test_process(env, data))
env.run(p)
print('Collected', data)  # Lets see what we got
#如果要将数据存储在NumPy数组或数据库中，那么如果您在纯Python列表中缓冲数据，并且只向数据库写入较大的块（或完整的数据集），则通常可以提高性能。