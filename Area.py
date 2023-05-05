import matplotlib.pyplot as plt
import numpy as np

np.random.seed(1)

x_min = 0
y_min = 0

x_max = 2
y_max = 1

n = 1000000

hit = 0

hit_X = []
hit_Y = []

miss_X = []
miss_Y = []


for i in range(n):
    x = np.random.uniform(low=x_min, high=x_max)
    y = np.random.uniform(low=y_min, high=y_max)

    if x <= 1:
        # Triangle Check
        if y <= x:
            hit = hit + 1
            hit_X.append(x)
            hit_Y.append(y)
        else:
            miss_X.append(x)
            miss_Y.append(y)

    else:
        # Circle Check
        if (x-1)**2 + y**2 <= 1:
            hit = hit + 1
            hit_X.append(x)
            hit_Y.append(y)
        else:
            miss_X.append(x)
            miss_Y.append(y)


area = hit*2/n

print(area)

plt.scatter(hit_X, hit_Y, c="red")
plt.scatter(miss_X, miss_Y, c="green")
