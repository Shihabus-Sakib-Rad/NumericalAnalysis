# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
import numpy



g = 9.8
m = 68
c = 12.5
t_delta= 0.01
end = 50
time =numpy.arange(0, end, t_delta)
velocity = []
v=0
velocity.append(v)

def find_first_dv(v):
    return g - (c/m)*v


def find_next_v(dv, v):
    return v + dv*t_delta

for i, t in enumerate(time):
    dv = find_first_dv(v)
    v_next = find_next_v(dv, v)
    velocity.append(v_next)
    v = v_next
    
time = numpy.append(time, end)
plt.plot(time, velocity)
plt.show()