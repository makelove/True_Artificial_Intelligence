# -*- coding: utf-8 -*-
# @Time    : 2018/1/3 13:00
# @Author  : play4fun
# @File    : py读取IMU_1.py
# @Software: PyCharm

"""
py读取IMU_1.py:
JSON
"""

import serial,json

ardu = serial.Serial('/dev/tty.usbmodem1421', 38400)
# ardu = serial.Serial('/dev/ttyACM0', 9600)#树莓派3
while True:
    if ardu.isOpen():
        # data:bytes=ardu.readline()
        data = ardu.readline()
        strips = data.decode('utf-8').strip()
        js=json.loads(strips)
        print('data:', js)


