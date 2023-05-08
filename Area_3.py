
import numpy as np
import matplotlib.pyplot as plt

# domain and range for random number
X_min = -2
Y_min = -2

X_max = 3
Y_max = 4

# Random generation
# higher number makes plot look better but question says 1000

n = 100000

hit = 0

# Storing hits and miss for plot

hit_X = []
hit_Y = []

miss_X = []
miss_Y = []

# Code to simulate 

for i in range(n):
  #create random num from within x and y max,min
  x = np.random.uniform(low=X_min, high=X_max)
  y = np.random.uniform(low=Y_min, high=Y_max)

  # check if within circle or not
  # radius = 2
  if x**2 + y**2 <= 2**2:
    hit = hit + 1
    hit_X.append(x)
    hit_Y.append(y)
  else:
    miss_X.append(x)
    miss_Y.append(y)

# Plot witinh circle as red and outer as green

plt.scatter(hit_X, hit_Y, c="red")
plt.scatter(miss_X, miss_Y, c="green")

plt.show()