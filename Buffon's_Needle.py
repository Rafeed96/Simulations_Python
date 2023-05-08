# Gap = d = 1
# Needle = l = 1 , (l<=d)!!!
# Distance of middle part of needle to nearest line = D = (0,d/2)
# 0 = Theta = 0 => (0, pi)
# h = l/2*sin0
# sin0 = h/(l/2)

# Hit Conditions
# h >= D
# D <= (l/2)sin0

# pi = (2*n)/hits

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(1)


n = 10000
hit = 0

hit_x = []
hit_y = []

miss_x = []
miss_y = []


for i in range(n):
    D = np.random.uniform(low=0.0, high=3.6)
    theta = np.random.uniform(low=0.0, high=np.pi)

    # Hit Condition
    if D <= 3.6*np.sin(theta):
        hit = hit + 1
        hit_x.append(theta)
        hit_y.append(D)
    else:
        miss_x.append(theta)
        miss_y.append(D)


estimated_pi = (2*n)/hit
area = (2**2)*estimated_pi
print(estimated_pi)


plt.scatter(hit_x, hit_y, c="red")
plt.scatter(miss_x, miss_y, c="green")


plt.show()