# -*- coding: utf-8 -*-
# @Time    : 2018/1/25 20:33
# @Author  : play4fun
# @File    : 双显示器上运行GameMode.py
# @Software: PyCharm

"""
双显示器上运行GameMode.py:
小心不能关闭程序，全屏

http://excid3.com/blog/python-and-opengl-game-mode-on-dual-monitors-tutorial
"""

import sys

from OpenGL.GL import *
from OpenGL.GLUT import *


def main():

    # Initialize OpenGL
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)

    # Configure the display output
    glutGameModeString("2560x1024:24@60")
    glutEnterGameMode()

    # Setup callbacks
    glutKeyboardFunc(keyboard)
    glutDisplayFunc(display)

    # Begin!
    glutMainLoop()


def keyboard(key, x, y):
    if key == b'q':
        sys.exit(0)


def display():

    glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_LINES)
    glVertex2f(1.0, 1.0)
    glVertex2f(-1.0, -1.0)
    glEnd()

    glutSwapBuffers()

if __name__ == "__main__":
    main()