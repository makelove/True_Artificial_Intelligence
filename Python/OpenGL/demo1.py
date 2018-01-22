# -*- coding: utf-8 -*-
# @Time    : 2018/1/22 23:11
# @Author  : play4fun
# @File    : demo1.py
# @Software: PyCharm

"""
demo1.py:
https://pkuwwt.github.io/programming/2014-04-03-python-opengl-sample/
"""


from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def init():
    glClearColor(0, 0, 0, 1)
    gluOrtho2D(-1, 1, -1, 1)


def plotpoints():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 0, 0)
    glBegin(GL_TRIANGLES)
    glVertex2f(0, 0)
    glVertex2f(1, 0)
    glVertex2f(1, 1)
    glEnd()
    glFlush()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutCreateWindow("Plot Points")
    glutDisplayFunc(plotpoints)
    init()
    glutMainLoop()


if __name__ == '__main__':
    main()
