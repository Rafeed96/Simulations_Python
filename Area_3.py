
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(1)

x_min = 0
y_min = 0

x_max = 3
y_max = 2

n = 1000000

hit = 0

hit_X = []
hit_Y = []

miss_X = []
miss_Y = []


for i in range(n):
    x = np.random.uniform(low=x_min, high=x_max)
    y = np.random.uniform(low=y_min, high=y_max)

    if x <= 1 and y <= 1:
        # Paralellogram
        # Triangle Check
        if y <= x:
            hit = hit + 1
            hit_X.append(x)
            hit_Y.append(y)
        else:
            miss_X.append(x)
            miss_Y.append(y)

    elif x > 1 and x <= 2 and y <= 1:
        # Square Check
        if y <= 1:
            hit = hit + 1
            hit_X.append(x)
            hit_Y.append(y)
        else:
            miss_X.append(x)
            miss_Y.append(y)
    elif x >= 2 and x <= 3 and y <= 1:
        if y >= (x-2) and y <= 1:
            hit = hit + 1
            hit_X.append(x)
            hit_Y.append(y)
        else:
            miss_X.append(x)
            miss_Y.append(y)

    if y <= 1 and x <= 3:
        # Circle Check
        if (x-1)**2 + (y)**2 <= 1:
            hit = hit + 1
            hit_X.append(x+1)
            hit_Y.append(y+1)
        else:
            if x <= 2:
                miss_X.append(x+1)
                miss_Y.append(y+1)
            else:
                miss_X.append(x-2)
                miss_Y.append(y+1)
