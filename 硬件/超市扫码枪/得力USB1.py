# -*- coding: utf-8 -*-
# @Time    : 2018/5/8 10:21
# @Author  : play4fun
# @File    : 得力USB1.py
# @Software: PyCharm

"""
得力USB1.py: 不行
"""

from serial import Serial

com='/dev/input/event0'
ser=Serial(com,port=9600)


def recv(serial):
    data = ''
    while serial.inWaiting() > 0:
        data += serial.read(1)

    return data

try:
    while True:
        data=recv(ser).strip()
        if data !='':
            print(data)
except KeyboardInterrupt as e:
    print(e)