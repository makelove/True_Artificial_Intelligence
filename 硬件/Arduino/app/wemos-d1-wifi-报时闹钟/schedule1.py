# -*- coding: utf-8 -*-
# @Time    : 2018/1/22 13:00
# @Author  : play4fun
# @File    : schedule1.py
# @Software: PyCharm

"""
schedule1.py:
文档https://schedule.readthedocs.io/en/stable/

"""

import schedule
import time


def job():
    print("I'm working...")


schedule.every(1).minutes.do(job)
schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
schedule.every().day.at("13:04").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)
