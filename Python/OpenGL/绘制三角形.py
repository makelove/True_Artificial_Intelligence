# -*- coding: utf-8 -*-
# @Time    : 2018/1/22 23:17
# @Author  : play4fun
# @File    : 绘制三角形.py
# @Software: PyCharm

"""
绘制三角形.py:
https://pycoders-weekly-chinese.readthedocs.io/en/latest/issue11/3D-Programming-in-Python.html
"""

import pyglet
from pyglet.gl import *

win = pyglet.window.Window()


@win.event
def on_draw():
    # Clear buffers
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw outlines only
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

    # Draw some stuff
    glBegin(GL_TRIANGLE_FAN)
    glVertex2i(200, 200)
    glVertex2i(200, 300)
    glVertex2i(250, 250)
    glVertex2i(300, 200)
    glVertex2i(250, 150)
    glVertex2i(200, 100)
    glEnd()


pyglet.app.run()
