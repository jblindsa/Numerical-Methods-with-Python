# -*- coding: utf-8 -*-
"""
Created on Wed Dec  3 21:51:56 2014

@author: james
"""
plt.close('all')
#import 
import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, log, ceil, pi

# set model parameters
g = 9.81      # acceleration of gravity
m_s = 50.     # weight of rocket shell
rho = 1.091   # average air density (assumed constant)
r = 0.5       # radius of rocket
A = pi*r**2   # max cross-sectional area of rocket
Cd = 0.15     # drag coefficient
v_e = 325.    # exhaust speed

# set time parameters
dt = 0.1
T = 100.
t = np.arange(0.0,T,dt)
N = int(T/dt)

#set initial conditions
m_p = np.zeros(len(t))
h = np.zeros(len(t))
v = np.zeros(len(t))
m_p[0] = 100.    # initial mass of rocket propellant
h[0] = 0.0        # starting height (ground level)
v[0] = 0.0        # initial velocity

    
#def f(u):
#    if t < 20:
#        m_p = m_p0 u[0]
#    h = u[1]
#    v = u[2]
#    return np.array([])
    
#some non-zero value that will be overwritten
H=0    
for i, time in enumerate(t[0:-1]):
    if time<5.:
        Mp_dot = 20.
    else:
        Mp_dot = 0.0
    m_p[i+1] = m_p[i]-Mp_dot*dt
    h[i+1] = h[i]+dt*v[i]
    v[i+1] = v[i]+dt*(-g+(Mp_dot*v_e-0.5*rho*v[i]*abs(v[i])*A*Cd)/(m_s+m_p[i]))
    H=h[i+1]
    if H<0:
        break
        
print H
print "the time of crashdown is ", time
print "velocity is ", v[i]
    
plt.figure(1) 
plt.plot(t,h)
plt.xlabel('time [s]')
plt.ylabel('height [m]')
plt.figure(2) 
plt.plot(t,v)
plt.xlabel('time [s]')
plt.ylabel('velocity [m/s]')
plt.figure(3) 
plt.plot(t,m_p)
plt.xlabel('time [s]')
plt.ylabel('mass of propellant [kg]')
plt.show()




