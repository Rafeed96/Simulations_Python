import math
import matplotlib.pyplot as plt

T_x = []
T_y = []

for t in range(21):
    x = 1 + t**2
    y = t*2

    T_x.append(x)
    T_y.append(y)

print(len(T_x))
print(T_x)
print(T_y)

plt.scatter(T_x, T_y)
plt.plot(T_x, T_y)


S = 10

P_x = [100]
P_y = [100]

for t in range(20):
    dist = math.sqrt((T_x[t]-P_x[t])**2 + (T_y[t]-P_y[t])**2)
