## SimPy入门
- 参考
    - https://pypi.python.org/pypi/simpy
    - https://www.ibm.com/developerworks/cn/linux/l-simpy/index.html
    - [使用SimPY进行离散事件仿真](http://blog.csdn.net/bibade123/article/details/78388898)
    - https://zhuanlan.zhihu.com/p/31526894
    - https://zhuanlan.zhihu.com/p/32005127
    
- SimPY使用Environment，Process，Event，Resource四大概念来进行离散事件的仿真。
    - Environment就是整体仿真所在的时间，主要用于提取时间。 
    - Process就是仿真过程中的实体，如：顾客， 设备， 车辆等。 Process本质上也是一个event。源代码里面可以看到是继承Event的一个类。 
    - Event是仿真中触发的事件，可以理解为一个定时器。当定时器到时时，触发事件。 
    - Resource是仿真中的资源，如ATM机，服务器等。
    
    
>SimPy是基于标准Python的基于流程的离散事件仿真框架。它的事件调度器是基于Python的生成器，也可以用于异步网络或实现多代理系统（同时具有模拟和真实通信）。

>SimPy中的进程由Python生成器函数定义，例如，可以用来模拟客户，车辆或代理等活动组件。SimPy还提供各种类型的共享资源来模拟有限容量的拥塞点（如服务器，结账柜台和隧道）。

>模拟可以“实时”（挂钟时间）或通过手动步进事件来“尽可能快”地执行。

>虽然理论上可以用SimPy进行连续的模拟，但它没有帮助你的功能。此外，SimPy对于具有固定步长的模拟以及您的流程不会彼此交互或与共享资源交互的情况并不是必需的。

```
SimPy 中的进程是由 Python 生成器构成，生成器的特性可以模拟具有主动性的物件，比如客户、汽车、或者中介等等。
SimPy也提供多种类的共享资源（shared resource）来描述拥挤点（比如服务器、收银台和隧道）。

仿真运行速度非常快，仿真中的模拟时间长短不影响仿真运行效率，仿真中的模拟时间单位可以任意指定，
一秒、一年、一小时都是允许的。
```

- 安装
    - pip install -U simpy
    
- 例子
```python
import simpy
def clock(env, name, tick):
     while True:
         print(name, env.now)
         yield env.timeout(tick)
env=simpy.Environment()
env.process(clock(env,'Fast',0.5))
env.process(clock(env,'Slow',1))
env.run(until=3)
```    
```python
def speaker(env):
    yield env.timeout(30)
    return 'handout'
def moderator(env):
    for i in range(3):
        val=yield env.process(speaker(env))
        print(val)

env=simpy.Environment()
moderator(env)
```