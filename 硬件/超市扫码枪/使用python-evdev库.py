# -*- coding: utf-8 -*-
# @Time    : 2018/5/8 23:43
# @Author  : play4fun
# @File    : 使用python-evdev库.py
# @Software: PyCharm

"""
使用python-evdev库.py:树莓派 Linux


安装：pip install evdev
文档http://python-evdev.readthedocs.io/en/latest/tutorial.html
http://python-evdev.readthedocs.io/en/latest/usage.html

"""

from evdev import InputDevice
from select import select

dev = InputDevice('/dev/input/event0')

while True:
   r,w,x = select([dev], [], [])
   for event in dev.read():
       print(event)