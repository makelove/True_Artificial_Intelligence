# -*- coding: utf-8 -*-
# @Time    : 2017/12/26 11:43
# @Author  : play4fun
# @File    : 事件添加回调.py
# @Software: PyCharm

"""
事件添加回调.py:
"""

import simpy


def my_callback(event):
    print('Called back from', event)


env = simpy.Environment()
event = env.event()
event.callbacks.append(my_callback)
print(event.callbacks)

'''
触发事件
当事件被触发时，它们可以成功或失败。例如，如果一个事件在计算结束时被触发并且一切正常，事件就会成功。如果在计算过程中发生异常，则该事件将失败。

要触发事件并将其标记为成功，可以使用 Event.succeed(value=None)。您可以选择传递一个值（例如计算结果）。

要触发事件并将其标记为失败，请调用Event.fail(exception) 并传递一个Exception实例（例如，在计算失败时捕获的异常）。

还有一种触发事件的通用方法：Event.trigger(event)。这将传递给它的事件的价值和结果（成功或失败）。

所有这三个方法都返回它们绑定的事件实例。这允许你做类似的事情。yield Event(env).succeed()
'''