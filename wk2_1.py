#!/usr/bin/python
# -*- coding: utf-8 -*-

from pythymiodw import *

def print_temp(t_celcius):
    """ calculate t_fahrenheit and print both
    """
    tf = t_celcius * 9/5 + 32
    return t_celcius, tf

def forward(speed, duration):
    """ move both wheels for that duration, and stop
    """
    robot.wheels(speed, speed)
    robot.sleep(duration)
    robot.wheels(0,0)
    return

robot = ThymioReal() # create an object

############### Start writing your code here ################ 

# Prompt user to enter speed and duration of movement

# Move according to the specified speed and duration

# Read temperature in celcius from the sensor and print it

########################## end ############################## 
s = int(input('speed'))
d = int(input('duration'))
forward(s,d)
t = robot.temperature
out = print_temp(t)
print(out)
robot.quit() # disconnect the communication

