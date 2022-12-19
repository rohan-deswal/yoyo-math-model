'''
This is the code for the Yo-Yo
Simulated Model written by
Rohan Deswal, 20202UMP1071, MPAE, NSUT Delhi
based on the work of Koichi Hashimoto and Toshiro Noritsugu
of Okayama University.
'''

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

m = 1 # mass of the Yo-Yo
r = 0.1 # radius of the Yo-Yo
l = 1 # lenght of the complete string
e_friction = 0.15 # approx coefficent of friction between common plastics and cotton strings
I = 0.5*m*(r**2) # inertia fo the Yo-Yo
g = 9.801 # gravitational acceleration

dt = np.pi/100 # Time Interval
time_axis = np.arange(0,10,0.1)
theta = np.arange(0,np.pi,dt) # Input of Various Angular Positions
theta_d1 = np.gradient(np.sin(theta),dt) # Velocity profile for a sinusoidal input rotation
theta_d2 = np.gradient(theta_d1,dt) # corresponding angular acceleration

def linear_acceleration(theta_d1_val, theta_d2_val):
    '''
    This function is used to calculate the instantaneous
    linear acceleration of the Yo-Yo given the angular
    acceleration and angular velocity of the Yo-Yo based on
    the analysis given in the document.
    '''
    return (((I+m*(r**2))*theta_d2_val + r*e_friction*theta_d1_val)/(m*r)) - g

h_d2 = [-linear_acceleration(theta_d1[i],theta_d2[i]) for i in range(len(theta_d1))]
h_d1 = [0]
h = [0] 

# Calculation of Integral to find Height of the Yo-Yo
for a in h_d2:
    h_d1.append(h_d2[-1] + a*dt)
    h.append(100*(h_d1[-1] + 0.5*a*dt**2) % 1000)

fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(time_axis, theta)
axs[0, 0].set_title('Input Angles or Value of Rotation')
axs[0, 1].plot(time_axis, theta_d1, 'tab:orange')
axs[0, 1].set_title('Angular Velocity or the first derivative of θ')
axs[1, 0].plot(time_axis, theta_d2, 'tab:green')
axs[1, 0].set_title('Angular Acceleration or the second derivative of θ')
axs[1, 1].plot(time_axis, h[1:], 'tab:red')
axs[1, 1].set_title('Value height of the Yo-Yo in cm')

fig.tight_layout()

for ax in axs.flat:
    ax.set(xlabel='time in seconds')

plt.legend(loc="best")
plt.show()

