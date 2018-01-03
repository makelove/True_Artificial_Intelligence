# -*- coding: utf-8 -*-
# @Time    : 2018/1/3 13:05
# @Author  : play4fun
# @File    : py读取IMU_2.py
# @Software: PyCharm

"""
py读取IMU_2.py:
根据[某个字的不同笔划]来记录IMU,横竖撇捺
"""

import serial, json

ardu = serial.Serial('/dev/tty.usbmodem1421', 38400)
# ardu = serial.Serial('/dev/ttyACM0', 9600)#树莓派3
while True:
    if ardu.isOpen():
        # data:bytes=ardu.readline()
        data = ardu.readline()
        strips = data.decode('utf-8').strip()
        js = json.loads(strips)
        print('data:', js)
