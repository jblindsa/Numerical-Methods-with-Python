# -*- coding: utf-8 -*-
"""
Created on Wed Dec  3 21:51:56 2014

@author: james
"""
plt.close('all')
#import 
import numpy as np
import matplotlib.pyplot as plt

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
    

for i, time in enumerate(t[0:-1]):
    if time<5.: 
        Mp_dot = 20. #rate of propellant use
    else:
        Mp_dot = 0.0
   # instead of solving a vector I just solved three separate equations
    m_p[i+1] = m_p[i]-Mp_dot*dt
    h[i+1] = h[i]+dt*v[i]
    v[i+1] = v[i]+dt*(-g+(Mp_dot*v_e-0.5*rho*v[i]*abs(v[i])*A*Cd)/(m_s+m_p[i]))
    if h[i+1]<0:
        break
        
print h[i+1]
print "the time of crashdown is approximately ", time, " seconds"
print "velocity is ", v[i], " m/s"
  
#print some basic figures of height, velocity, and propellant mass vs. time  
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




