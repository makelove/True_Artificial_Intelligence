# -*- coding: utf-8 -*-
# @Time    : 2018/1/22 23:15
# @Author  : play4fun
# @File    : demo3line.py
# @Software: PyCharm

"""
demo3line.py:
"""

import pyglet
from pyglet.gl import *

win = pyglet.window.Window()


@win.event
def on_draw():
    # Clear buffers
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw some stuff
    glBegin(GL_LINES)
    glVertex2i(50, 50)
    glVertex2i(75, 100)
    glVertex2i(100, 150)
    glVertex2i(200, 200)
    glEnd()


pyglet.app.run()
