# -*- coding: utf-8 -*-
# @Time    : 2017/12/25 22:48
# @Author  : play4fun
# @File    : car_go.py
# @Software: PyCharm

"""
car_go.py:
https://pythonhosted.org/SimPy/Manuals/SManual.html
不对!
"""
from SimPy.Simulation import *


class Car(Process):
  def __init__(self,name,cc):
     Process.__init__(self,name=name)
     self.cc = cc

  def go(self):
     print now( ), self.name, "Starting"
     yield hold,self,100.0
     print now( ), self.name, "Arrived"

initialize( )
c1  = Car("Car1",2000)       # a new car
activate(c1,c1.go( ),at=6.0) # activate at time 6.0
c2  = Car("Car2",1600)       # another new car
activate(c2,c2.go( ))        # activate at time 0
simulate(until=200)
print 'Current time is ',now( ) # will print 106.0