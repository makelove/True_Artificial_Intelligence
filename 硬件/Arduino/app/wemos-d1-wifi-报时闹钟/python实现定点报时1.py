# -*- coding: utf-8 -*-
# @Time    : 2018/1/22 12:11
# @Author  : play4fun
# @File    : python实现定点报时.py
# @Software: PyCharm

"""
python实现定点报时1.py:
播放wav文件，beep哔哔
"""

# import winsound
from time import sleep, localtime

import time
import sys


def beep(h, m):
    # if m == 59:
    if m == 53:
        # winsound.Beep(1000, 500)  # one long beep
        for i in range(1, h + 1):
            # sys.stdout.write('\r\a{i}'.format(i=i))
            # sys.stdout.flush()
            print('\a')
            time.sleep(1)
    elif m == 29:
        # for i in range(1, 6):
        # sys.stdout.write('\r\a{i}'.format(i=1))
        # sys.stdout.flush()
        print('\a')
        time.sleep(1)

        # winsound.Beep(1000, 200)  # two short beep
        # winsound.Beep(1000, 200)  # two short beep


if __name__ == "__main__":
    while True:
        now = localtime()
        h = now.tm_hour
        m = now.tm_min
        s = now.tm_sec
        beep(h, m)
        sleep(60 - s)  # refresh every minute.这个不行，不够准时
