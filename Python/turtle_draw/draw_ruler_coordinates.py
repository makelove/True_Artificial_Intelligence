# -*- coding: utf-8 -*-
# @Time    : 2018/1/8 16:16
# @Author  : play4fun
# @File    : draw_ruler_coordinates.py
# @Software: PyCharm

"""
draw_ruler_coordinates.py:
https://teamtreehouse.com/community/coordinates-plane-python
"""

import turtle
import math

wn = turtle.Screen()  # setup screen and its attributes
tess = turtle.Turtle()  # sets tess
wn.title("Coordinate axis")
tess.speed(10)


def draw_axis(s):
    # draws x, y axis
    tess.setpos(0, 0)
    tess.color("black")
    tess.pensize(5)
    for i in range(4):
        tess.fd(s)
        tess.pu()
        tess.goto(0, 0)
        tess.pd()
        tess.lt(90)
    tess.ht()


def horizontal_lines(s):
    # draw horizontal lines
    x = -300
    for y in range(-300, 300 + 1, 25):
        tess.pu()
        turtle.pu()
        turtle.goto(x, y)
        turtle.pd()
        turtle.color("lightblue")
        turtle.pensize(3)
        turtle.fd(s)


def vertical_lines(s):
    # draw vertical lines
    y = 300
    turtle.right(90)
    for x in range(-300, 300 + 1, 25):
        turtle.pu()
        turtle.goto(x, y)
        turtle.pd()
        turtle.color("lightblue")
        turtle.pensize(3)
        turtle.fd(s)


draw_axis(300)
horizontal_lines(600)
vertical_lines(600)
