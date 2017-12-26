# -*- coding: utf-8 -*-
# @Time    : 2017/12/26 19:35
# @Author  : play4fun
# @File    : 资源使用情况.py
# @Software: PyCharm

"""
资源使用情况.py:
资源监视的用例很多，例如，您可能想要监视：

随着时间和平均资源的利用，也就是说，

一次使用资源的进程的数量
一个容器的水平
商店中物品的数量
这可以在不连续的时间步骤中进行监控，也可以在每次进行更改时进行监控。

（put | get）队列中的进程数量（和平均值）。再次，这可以在不连续的时间步骤或每次变化时进行监控。

对于PreemptiveResource，您可能需要测量随着时间的推移发生抢先的频率。

与您的流程不同，您无法直接访问内置资源类的代码。但这并不妨碍你监视它们。

猴子修补一些资源的方法可以让你收集所有你需要的数据。

"""

from functools import partial, wraps
import simpy


def patch_resource(resource, pre=None, post=None):
    """Patch *resource* so that it calls the callable *pre* before each
    put/get/request/release operation and the callable *post* after each
    operation.  The only argument to these functions is the resource
    instance.
    """

    def get_wrapper(func):
        # Generate a wrapper for put/get/request/release
        @wraps(func)
        def wrapper(*args, **kwargs):
            # This is the actual wrapper
            # Call "pre" callback
            if pre:
                pre(resource)

            # Perform actual operation
            ret = func(*args, **kwargs)

            # Call "post" callback
            if post:
                post(resource)

            return ret

        return wrapper

    # Replace the original operations with our wrapper
    for name in ['put', 'get', 'request', 'release']:
        if hasattr(resource, name):
            setattr(resource, name, get_wrapper(getattr(resource, name)))


def monitor(data, resource):
    """This is our monitoring callback."""
    item = (
        resource._env.now,  # The current simulation time
        resource.count,  # The number of users
        len(resource.queue),  # The number of queued processes
    )
    data.append(item)


def test_process(env, res):
    with res.request() as req:
        yield req
        yield env.timeout(1)


env = simpy.Environment()

res = simpy.Resource(env, capacity=1)
data = []
# Bind *data* as first argument to monitor()
# see https://docs.python.org/3/library/functools.html#functools.partial
monitor = partial(monitor, data)
patch_resource(res, post=monitor)  # Patches (only) this resource instance

p = env.process(test_process(env, res))
env.run(p)

print(data)
#[(0, 1, 0), (1, 0, 0)]
