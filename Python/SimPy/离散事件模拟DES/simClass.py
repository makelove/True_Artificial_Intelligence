# -*- coding: utf-8 -*-
# @Time    : 2017/12/25 15:05
# @Author  : play4fun
# @File    : simClass.py.py
# @Software: PyCharm

"""
simClass.py:
"""
from simpy import Process


class ClerkClass(Process):
    ServiceRate = 1 / 1.2  # reciprocal of mean service tim
    MaxQueueLength = 0
    Queue = []
    Idle = []
    Busy = []
    NumDone = 0

    def __init__(self):
        Process.__init__(self)
        ClerkClass.Idle.append(self)  # Initially idle

    def Run(self):
        # Clerk Process
        while 1:
            yield passivate, self  # wait until awaken by customers
            ClerkClass.Idle.remove(self)
            ClerkClass.Busy.append(self)  # going to be busy
            while ClerkClass.Queue != []:
                C = ClerkClass.Queue.pop()  # call next customer in line
                if len(ClerkClass.Queue) > ClerkClass.MaxQueueLength:
                    ClerkClass.MaxQueueLength = len(ClerkClass.Queue)
                # Start service the customer
                ServiceTime = G.Rnd.expovariate(ClerkClass.ServiceRate)
                yield hold, self, ServiceTime
                C.endService()
                G.TotalWaitingTime += C.WaitingTime
                ClerkClass.NumDone += 1
                del C
            ClerkClass.Busy.remove(self)
            ClerkClass.Idle.append(self)


class ArrivalClass(Process):
    ArrivalRate = 1 / 1.0  # reciprocal of mean arrival time

    def __init__(self):
        Process.__init__(self)

    def Run(self):
        while 1:
            InterArrivalTime = G.Rnd.expovariate(ArrivalClass.ArrivalRate)
            yield hold, self, InterArrivalTime
            C = Customer()
            ClerkClass.Queue.append(C)  # a customer arrives
            G.NumCustomers += 1
            if ClerkClass.Idle != []:  ## reciprocal of mean arrival time
                reactivate(ClerkClass.Idle[0])  # Yes , wake him/her up
