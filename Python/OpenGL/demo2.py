# -*- coding: utf-8 -*-
# @Time    : 2018/1/22 23:14
# @Author  : play4fun
# @File    : demo2.py
# @Software: PyCharm

"""
demo2.py:
https://pycoders-weekly-chinese.readthedocs.io/en/latest/issue11/3D-Programming-in-Python.html
"""

# import pyglet
from pyglet.gl import *

win = pyglet.window.Window()


@win.event
def on_draw():
    # Clear buffers
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw some stuff
    glBegin(GL_POINTS)
    glVertex2i(50, 50)
    glVertex2i(75, 100)
    glVertex2i(100, 150)
    glEnd()


pyglet.app.run()
