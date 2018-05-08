# -*- coding: utf-8 -*-
# @Time    : 2018/5/8 23:22
# @Author  : play4fun
# @File    : demo3.py
# @Software: PyCharm

"""
demo3.py:树莓派 Linux
http://tongxinmao.com/Article/Detail/id/223

"""

import struct
import time
import sys

infile_path = "/dev/input/event" + (sys.argv[1] if len(sys.argv) > 1 else "0")

#long int, long int, unsigned short, unsigned short, unsigned int
FORMAT = 'llHHI'
EVENT_SIZE = struct.calcsize(FORMAT)

#open file in binary mode
in_file = open(infile_path, "rb")

event = in_file.read(EVENT_SIZE)

while event:
    (tv_sec, tv_usec, type, code, value) = struct.unpack(FORMAT, event)

    if type != 0 or code != 0 or value != 0:
        print("Event type %u, code %u, value %u at %d.%d" % \
            (type, code, value, tv_sec, tv_usec))
    else:
        # Events with code, type and value == 0 are "separator" events
        print("===========================================")

    event = in_file.read(EVENT_SIZE)

in_file.close()