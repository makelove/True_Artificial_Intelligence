## SimPy入门
- 参考
    - https://pypi.python.org/pypi/simpy
    - https://www.ibm.com/developerworks/cn/linux/l-simpy/index.html
    - http://blog.csdn.net/bibade123/article/details/78388898
    
>SimPy是基于标准Python的基于流程的离散事件仿真框架。它的事件调度器是基于Python的生成器，也可以用于异步网络或实现多代理系统（同时具有模拟和真实通信）。

>SimPy中的进程由Python生成器函数定义，例如，可以用来模拟客户，车辆或代理等活动组件。SimPy还提供各种类型的共享资源来模拟有限容量的拥塞点（如服务器，结账柜台和隧道）。

>模拟可以“实时”（挂钟时间）或通过手动步进事件来“尽可能快”地执行。

>虽然理论上可以用SimPy进行连续的模拟，但它没有帮助你的功能。此外，SimPy对于具有固定步长的模拟以及您的流程不会彼此交互或与共享资源交互的情况并不是必需的。

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