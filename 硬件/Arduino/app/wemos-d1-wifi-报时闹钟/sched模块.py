# -*- coding: utf-8 -*-
# @Time    : 2018/1/22 15:51
# @Author  : play4fun
# @File    : sched模块.py
# @Software: PyCharm

"""
sched模块.py:
http://www.cnblogs.com/jhao/p/7123692.html
"""

import sched, time

s = sched.scheduler(time.time, time.sleep)  # 生成调度器


def print_time():
    print("From print_time", time.time())


def print_some_times():
    print(time.time())#隔5秒中执行第一个事件,隔10秒后执行第二个事件：
    s.enter(5, 1, print_time, ())
    # 加入调度事件
    # 四个参数分别是:
    # 间隔事件(具体值决定与delayfunc, 这里为秒);
    # 优先级(两个事件在同一时间到达的情况);
    # 触发的函数;
    # 函数参数；
    s.enter(10, 1, print_time, ())

    # 运行
    s.run()
    print(time.time())


if __name__ == '__main__':
    print_some_times()
