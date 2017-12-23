# -*- coding: utf-8 -*-
# @Time    : 2017/12/20 16:41
# @Author  : play4fun
# @File    : traffic_light_demo1.py
# @Software: PyCharm

"""
traffic_light_demo1.py:
视频https://www.youtube.com/watch?v=0osGrraoCX0
"""

import simpy


def main():
    env = simpy.Environment()
    env.process(traffic_light(env))
    env.run(until=300)
    print("Simulation complete")


def traffic_light(env):
    while True:
        print("Light turned GRN绿 at t= " + str(env.now))
        yield env.timeout(30)
        print("Light turned YEL黄 at t= " + str(env.now))
        yield env.timeout(5)
        print("Light turned RED红 at t= " + str(env.now))
        yield env.timeout(20)


if __name__ == '__main__':
    main()
