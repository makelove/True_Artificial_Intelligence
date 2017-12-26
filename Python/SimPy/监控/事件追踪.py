# -*- coding: utf-8 -*-
# @Time    : 2017/12/26 19:54
# @Author  : play4fun
# @File    : 事件追踪.py
# @Software: PyCharm

"""
事件追踪.py:

为了调试或可视化模拟，您可能需要跟踪创建，触发和处理事件的时间。也许你也想跟踪哪个进程创建了一个事件，哪个进程等待了一个事件。

对于这些用例来说Environment.step()，最有趣的两个功能就是 处理所有事件，并将 Environment.schedule()所有事件调度并插入到SimPy的事件队列中。
"""

from functools import partial, wraps
import simpy


def trace(env, callback):
    """Replace the ``step()`` method of *env* with a tracing function
    that calls *callbacks* with an events time, priority, ID and its
    instance just before it is processed.

    """

    def get_wrapper(env_step, callback):
        """Generate the wrapper for env.step()."""

        @wraps(env_step)
        def tracing_step():
            """Call *callback* for the next event if one exist before
            calling ``env.step()``."""
            if len(env._queue):
                t, prio, eid, event = env._queue[0]
                callback(t, prio, eid, event)
            return env_step()

        return tracing_step

    env.step = get_wrapper(env.step, callback)


def monitor(data, t, prio, eid, event):
    data.append((t, eid, type(event)))


def test_process(env):
    yield env.timeout(1)


data = []
# Bind *data* as first argument to monitor()
# see https://docs.python.org/3/library/functools.html#functools.partial
monitor = partial(monitor, data)

env = simpy.Environment()
trace(env, monitor)

p = env.process(test_process(env))
env.run(until=p)

for d in data:
    print(d)
