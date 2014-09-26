import numpy as np
from matplotlib import pyplot as plt

data = np.genfromtxt('./csv/locations.csv', delimiter=',', dtype='str')
data = data[1:,:]

time = np.array(data[:,1], dtype=np.float)
latitude = data[:,4]
longitude = data[:,5]

# Normalize to start time, change to [s] 
time = (time - min(time))/1000

plt.plot(longitude, latitude, 'r*-', label='GPS trace')
plt.axis('equal')
plt.legend()
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend()
plt.show()