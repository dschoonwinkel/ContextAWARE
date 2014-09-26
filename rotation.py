import numpy as np
from matplotlib import pyplot as plt

fig1 = plt.figure()
plt.hold(True)

data = np.genfromtxt('./csv/rotation.csv', delimiter=',', dtype='str')
data = data[1:,:]

time = np.array(data[:,2], dtype=np.float)
x_angle = data[:,4]
y_angle = data[:,5]
z_angle = data[:,6]

# Normalize to start time, change to [s] 
time = (time - min(time))/1000

plt.plot(time,x_angle, label='X-angle')
plt.plot(time,y_angle, 'r', label='Y-angle')
plt.plot(time,z_angle, 'g', label='Z-angle')
plt.legend()
plt.xlabel('[s]')
plt.ylabel('Radians')

plt.show()