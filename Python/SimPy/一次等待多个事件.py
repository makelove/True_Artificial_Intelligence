# -*- coding: utf-8 -*-
# @Time    : 2017/12/26 11:54
# @Author  : play4fun
# @File    : 一次等待多个事件.py
# @Software: PyCharm

"""
一次等待多个事件.py:
有时候，你想同时等待多个事件。例如，您可能需要等待资源，但不是无限次的。或者你可能要等到所有的一系列事件发生。

因此SimPy中提供了AnyOf与AllOf事件，都是一个Condition事件。

两者都以事件列表作为参数，如果它们中的至少一个或全部被触发，则被触发。

"""

import simpy
from simpy.events import AnyOf, AllOf, Event

env = simpy.Environment()

events = [Event(env) for i in range(3)]
a = AnyOf(env, events)  # Triggers if at least one of "events" is triggered.
b = AllOf(env, events)  # Triggers if all each of "events" is triggered.

# '''
def test_condition(env):
    t1, t2 = env.timeout(1, value='spam'), env.timeout(2, value='eggs')
    ret = yield t1 | t2
    assert ret == {t1: 'spam'}

    t1, t2 = env.timeout(1, value='spam'), env.timeout(2, value='eggs')
    ret = yield t1 & t2
    assert ret == {t1: 'spam', t2: 'eggs'}

    # You can also concatenate & and |
    e1, e2, e3 = [env.timeout(i) for i in range(3)]
    yield (e1 | e2) & e3
    assert all(e.processed for e in [e1, e2, e3])


proc = env.process(test_condition(env))
env.run()

# '''
#条件结果的顺序与指定条件事件的顺序相同。这允许以下习惯用法方便地获取在和条件（包括AllOf）中指定的多个事件的值：
def fetch_values_of_multiple_events(env):
    t1, t2 = env.timeout(1, value='spam'), env.timeout(2, value='eggs')
    r1, r2 = (yield t1 & t2).values()
    assert r1 == 'spam' and r2 == 'eggs'


proc = env.process(fetch_values_of_multiple_events(env))
env.run()
