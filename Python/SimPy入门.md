## SimPy入门
- 参考
    - https://pypi.python.org/pypi/simpy
    

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