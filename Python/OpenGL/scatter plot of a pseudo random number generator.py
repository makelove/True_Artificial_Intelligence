# -*- coding: utf-8 -*-
# @Time    : 2018/1/25 20:20
# @Author  : play4fun
# @File    : scatter plot of a pseudo random number generator.py
# @Software: PyCharm

"""
scatter plot of a pseudo random number generator.py:
"""

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import random


def initFun():
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glColor3f(0.0, 0.0, 0.0)
    glPointSize(1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, 400.0, 0.0, 400.0)


def getRandom(mode):
    """
    Wrapper around several RNG's. If mode is 0 random.randint() is used, if
    mode is one a guassian distribution is used.
    """
    if mode == 0:
        return random.randint(0, 400)
    elif mode == 1:
        return random.gauss(200, 40) % 400


def displayFun():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POINTS)

    randMode = 1
    a = getRandom(randMode)
    b = getRandom(randMode)
    for i in range(0, 500000):
        glVertex2f(a, b)
        a = b
        b = getRandom(randMode)
    glEnd()
    glFlush()


if __name__ == '__main__':
    glutInit()
    glutInitWindowSize(400, 400)
    glutCreateWindow("Scatter")
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutDisplayFunc(displayFun)
    initFun()
    glutMainLoop()
