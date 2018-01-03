# -*- coding: utf-8 -*-
# @Time    : 2018/1/3 13:00
# @Author  : play4fun
# @File    : py读取IMU_1.py
# @Software: PyCharm

"""
py读取IMU_1.py:
JSON
"""

import serial, json, pickle

ardu = serial.Serial('/dev/tty.usbmodem1411', 38400)
# ardu = serial.Serial('/dev/ttyACM0', 9600)#树莓派3

#
imu_list = []

try:
    while True:
        if ardu.isOpen():

            # data:bytes=ardu.readline()
            data = ardu.readline()

            try:
                strips = data.decode('utf-8').strip()
                js = json.loads(strips)
                print('js:', js)

                imu_list.append(js)
            except Exception as e:
                # print(e)
                print('data:', data)
except KeyboardInterrupt:
    # finally:
    #
    if len(imu_list) > 0:
        with open('imu_list', 'wb') as f:
            pickle.dump(imu_list, f)
