"""
traffic_sim.py  Version 2.0
http://phillipmfeldman.org/Python/discrete_event_simulation/



OVERVIEW

This Python script simulates automotive traffic arriving at a traffic light.
The script demonstrates the following:

(1) several basic principles of discrete-event simulation, including the
representation of system states, the connection between events and changes of
state, and the Poisson process,

(2) the use of the SimPy module,

(3) simulation of random deviates using NumPy, and

(4) the use of Python generator functions.


THE MODEL

Cars drive on a single-lane road and arrive at the intersection from one
direction only according to a Poisson process with specified rate.  Positions
and velocities of the cars are not modeled, and there is thus no coordinate
system.

The traffic light switches between green and red at regular intervals; there is
no yellow state.

When a car arrives at a green light with no cars queued, it passes immediately
through the intersection and departs the simulation.

When a car arrives at a red light or with one or more cars queued at the
intersection, it stops and joins the queue.

When the light turns green, if there is a queue, cars enter the intersection one
at a time.  Once a car has entered the intersection, it clears the intersection,
regardless of the state of the light, after a delay that is a random draw from a
triangular distribution.


INPUTS

All inputs are hardwired into the code.


OUTPUTS

The simulation generates a trace of events as it runs, and also reports
estimates of the average number of cars in the queue and the average waiting
time.


FUTURE WORK

This model might be extended in any of several directions.  Some possibilities
include the following:

(1) There are several sources of bias in the average waiting time: (a) The
simulation starts with a green light.  (b) The simulation starts with no cars
queued.  (c) Cars remaining in the queue at the end of the simulation do not
contribute to the estimated waiting time.  The effects of (a) and (b) might be
mitigated by eliminating the initial transient; this would involve collecting
and saving individual waiting times, choosing alternative values for the
duration of the initial transient, generating estimates using only the data
outside of the transient interval, and then selecting one of these results using
some statistical criteria. (We want the mean of the selected result to have no
statistically significant difference from results based on longer transient
intervals, but otherwise we want to discard as little of the data as possible).

(2) The delay of the driver at the head of the queue in responding to the change
of the light from red to green could be made somewhat longer than that of
drivers who are further back in the queue.  This would allow for greater realism
in the model without explicitly modeling positions and velocities of the cars.

(3) One might have some fraction of the cars make a right-turn at the light,
with the remaining cars going straight, and compare the capacity of a
single-lane road, a two-lane road with no turn restrictions, and a two-lane road
with a dedicated right-turn-only lane.


AUTHOR

Dr. Phillip M. Feldman
"""

# Section 1: Import from modules and define a utility class.

from collections import deque  # double-ended queue
from numpy import random
import simpy
from simpy.util import start_delayed


class Struct(object):
    """
    This simple class allows one to create an object whose attributes are
    initialized via keyword argument/value pairs.  One can update the attributes
    as needed later.
    """

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


# Section 2: Initializations.

random.seed([1, 2, 3])

# Total number of seconds to be simulated:
end_time = 200.0

# Cars cars arrive at the traffic light according to a Poisson process with an
# average rate of 0.2 per second:
arrival_rate = 0.2
t_interarrival_mean = 1.0 / arrival_rate

# Traffic light green and red durations:
t_green = 30.0;
t_red = 40.0

# The time for a car at the head of the queue to depart (clear the intersection)
# is modeled as a triangular distribution with specified minimum, maximum, and
# mode.
t_depart_left = 1.6;
t_depart_mode = 2.0;
t_depart_right = 2.4

# Initially, no cars are waiting at the light:
queue = deque()

# Track number of cars:
arrival_count = departure_count = 0

Q_stats = Struct(count=0, cars_waiting=0)
W_stats = Struct(count=0, waiting_time=0.0)


# Section 3: Arrival event.

def arrival():
    """
    This generator functions simulates the arrival of a car.  Cars arrive
    according to a Poisson process having rate `arrival_rate`.  The times between
    subsequent arrivals are i.i.d. exponential random variables with mean

       t_interarrival_mean= 1.0 / arrival_rate
    """
    global arrival_count, env, light, queue

    while True:
        arrival_count += 1

        if light == 'red' or len(queue):

            # The light is red or there is a queue of cars.  ==> The new car joins
            # the queue.  Append a tuple that contains the number of the car and
            # the time at which it arrived:
            queue.append((arrival_count, env.now))
            print("Car #%d arrived and joined the queue at position %d at time "
                  "%.3f." % (arrival_count, len(queue), env.now))

        else:

            # The light is green and no cars are waiting.  ==> The new car passes
            # through the intersection immediately.
            print("Car #%d arrived to a green light with no cars waiting at time "
                  "%.3f." % (arrival_count, env.now))

            # Record waiting time statistics.  (This car experienced zero waiting
            # time, so we increment the count of cars, but the cumulative waiting
            # time remains unchanged.
            W_stats.count += 1

        # Schedule next arrival:
        yield env.timeout(random.exponential(t_interarrival_mean))


# Section 4: Define event functions.

# Section 4.1: Departure event.

def departure():
    """
    This generator function simulates the 'departure' of a car, i.e., a car that
    previously entered the intersection clears the intersection.  Once a car has
    departed, we remove it from the queue, and we no longer track it in the
    simulation.
    """
    global env, queue

    while True:

        # The car that entered the intersection clears the intersection:
        car_number, t_arrival = queue.popleft()
        print("Car #%d departed at time %.3f, leaving %d cars in the queue."
              % (car_number, env.now, len(queue)))

        # Record waiting time statistics:
        W_stats.count += 1
        W_stats.waiting_time += env.now - t_arrival

        # If the light is red or the queue is empty, do not schedule the next
        # departure.  `departure` is a generator, so the `return` statement
        # terminates the iterator that the generator produces.
        if light == 'red' or len(queue) == 0:
            return

        # Generate departure delay as a random draw from triangular distribution:
        delay = random.triangular(left=t_depart_left, mode=t_depart_mode,
                                  right=t_depart_right)

        # Schedule next departure:
        yield env.timeout(delay)


# Section 4.2: Light change-of-state event.

def light():
    """
    This generator function simulates state changes of the traffic light.  For
    simplicity, the light is either green or red--there is no yellow state.
    """
    global env, light

    while True:

        # Section 4.2.1: Change the light to green.

        light = 'green'
        print("\nThe light turned green at time %.3f." % env.now)

        # If there are cars in the queue, schedule a departure event:
        if len(queue):
            # Generate departure delay as a random draw from triangular
            # distribution:
            delay = random.triangular(left=t_depart_left, mode=t_depart_mode,
                                      right=t_depart_right)

            start_delayed(env, departure(), delay=delay)

        # Schedule event that will turn the light red:
        yield env.timeout(t_green)

        # Section 4.2.2: Change the light to red.
        light = 'red'
        print("\nThe light turned red at time %.3f." % env.now)

        # Schedule event that will turn the light green:
        yield env.timeout(t_red)


# Section 4.3: Schedule event that collects Q_stats.

def monitor():
    """
    This generator function produces an interator that collects statistics on the
    state of the queue at regular intervals.  An alternative approach would be to
    apply the PASTA property of the Poisson process ('Poisson Arrivals See Time
    Averages') and sample the queue at instants immediately prior to arrivals.
    """
    global env, Q_stats

    while True:
        Q_stats.count += 1
        Q_stats.cars_waiting += len(queue)
        yield env.timeout(1.0)


# Section 5: Schedule initial events and run the simulation.  Note: The first
# change of the traffic light, first arrival of a car, and first statistical
# monitoring event are scheduled by invoking `env.process`.  Subsequent changes
# will be scheduled by invoking the `timeout` method.  With this scheme, there
# is only one event of each of these types scheduled at any time; this keeps the
# event queue short, which is good for both memory utilization and running time.

print("\nSimulation of Cars Arriving at Intersection Controlled by a Traffic "
      "Light\n\n")

# Initialize environment:
env = simpy.Environment()

# Schedule first change of the traffic light:
env.process(light())

# Schedule first arrival of a car:
t_first_arrival = random.exponential(t_interarrival_mean)
start_delayed(env, arrival(), delay=t_first_arrival)

# Schedule first statistical monitoring event:
env.process(monitor())

# Let the simulation run for specified time:
env.run(until=end_time)

# Section 6: Report statistics.

print("\n\n      *** Statistics ***\n\n")

print("Mean number of cars waiting: %.3f" % (Q_stats.cars_waiting / float(Q_stats.count)))

print("Mean waiting time (seconds): %.3f" % (W_stats.waiting_time / float(W_stats.count)))

'''
汽车到达交通灯控制交叉口的仿真

在时间0.000，灯变成绿色。
1号车到达绿灯，没有汽车在4.706时间等待。
2号车到达绿灯，没有汽车在15.595等候。
3号车到达绿灯，18.829时没有汽车等候。

光线在30.000时变成红色。
4号车到达并在30.226时在位置1排队。
5号车在30.376时到达，并在2号位加入排队。
6号车在42.595的时候到达了位置3的队列。
7号车到达，并在47.117时在位置4加入排队。
8号车在62.352时到达并且在5号位加入队列。
9号车在66.757时到达，并在6号位加入排队。

光线在70.000时变成绿色。
4号汽车在72.010时发车，排队等候5辆汽车。
5号车在74.265时离场，留下了4辆车。
6号车在76.161时发车，排队等候3辆车。
7号车在77.782点出发，留下了2辆车。
10号车在78.785时到达队列3。
8号车在79.802时离去，在队列中留下了2辆车。
11号车到达，并在80.976时在3号位加入排队。
12号车到达时间81.616，在第4位加入队列。
9号车离开时间81.918，排队等候3辆车。
10号车在83.558时离去，排队等候2辆车。
11号车在85.273时离去，排队等候1辆车。
13号车到达，并在85.427时在位置2排队。
12号汽车在87.101时离去，留下了1辆汽车。
13号车在88.765时离去，排队等候了0辆。
14号车到了绿灯，89.862时没有汽车在等待。
15号车到达绿灯，93.045时没有汽车在等待。

光线在100.000时变成红色。
16号车到达，并在103.176时在位置1排队。
＃17号车在106.408时到达，并在第2号位加入队列。
18号车在115.312时到达位置3的队列。
19号车在125.277的时候到达了位置4的队列。
20号车到达，并在127.870的时候在5号位加入排队。

光线在140.000时变成绿色。
16号汽车在141.863时离去，留下了4辆汽车。
21号车到达时间点142.561的位置5。
17号汽车在143.754时离去，留下了4辆汽车。
22号车在145.814时到达队伍5号位。
18号汽车在145.827时离去，留下了4辆汽车。
19号汽车在148.060时离去，留下了3辆汽车。
20号车在149.871时离去，留下了2辆车。
21号汽车在151.817时离去，在队列中留下了1辆汽车。
22号车在153.938时发车，排队等候0辆车。
23号车到达时间为156.028，没有汽车。
24号汽车抵达绿灯，没有汽车在时间157.470等待。
25号车到达绿灯，160.066时没有车辆在等待。
车＃26到达绿灯，没有汽车等待时间164.971。
27号车到达绿灯，165.049时没有车辆在等待。

光线在170.000时变成红色。
28号车在172.428时到达位置1的队列。
29号车到达，并在175.255时在位置2排队。
30号车到达，并在179.434时在3号位加入排队。
31号车到达，并在184.672时在位置4排队。
32号车在184.777时到达队伍5号位。


      ***统计***

平均等候车数：2.345
平均等待时间（秒）：13.671
'''