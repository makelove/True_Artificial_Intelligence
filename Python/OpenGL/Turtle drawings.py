# -*- coding: utf-8 -*-
# @Time    : 2018/1/25 20:26
# @Author  : play4fun
# @File    : Turtle drawings.py
# @Software: PyCharm

"""
Turtle drawings.py:
http://www.de-brauwer.be/wiki/wikka.php?wakka=PyOpenGLTurtle
"""

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import math

curX = 0.0
curY = 0.0
angle = 0.0


def reset():
    """ Reset the position to the origin """
    global curX
    global curY
    global angle

    curX = 0.0
    curY = 0.0
    angle = 0.0


def turnTo(deg):
    """ Turn to a certain angle """
    global angle
    angle = deg


def turn(deg):
    """ Turn a certain number of degrees """
    global angle
    angle += deg


def forw(len, visible):
    """ Move forward over a certain distance """
    global curX
    global curY
    tmpX = curX
    tmpY = curY
    curX = curX + len * math.cos(math.radians(angle))
    curY = curY + len * math.sin(math.radians(angle))
    if visible:
        glBegin(GL_LINE_STRIP)
        glVertex2f(tmpX, tmpY)
        glVertex2f(curX, curY)
        glEnd()


def initFun():
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glColor3f(0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-100, 100, -100, 100)


def reshapeFun(w, h):
    if w > h:
        glViewport((w - h) / 2, 0, h, h)
    else:
        glViewport(0, (h - w) / 2, w, w)


def displayFun():
    glClear(GL_COLOR_BUFFER_BIT)
    reset()
    glColor3f(0.0, 0.0, 1.0)
    L = 30
    turnTo(0)
    for i in range(0, 4):
        forw(3 * L, True)
        turn(90)
        forw(L, True)
        turn(90)
        forw(L, True)
        turn(90)
    glFlush()

def displayFun2():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,0.0,1.0)
    reset()
    length=0
    increment = 1
    for i in range(0,100):
        forw(length,True)
        turn(60)
        length+=increment
    glFlush()

if __name__ == '__main__':
    glutInit()
    glutInitWindowSize(400, 400)
    glutCreateWindow("Turtle1")
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    # glutDisplayFunc(displayFun)
    glutDisplayFunc(displayFun2)
    glutReshapeFunc(reshapeFun)
    initFun()
    glutMainLoop()