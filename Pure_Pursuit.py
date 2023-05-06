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

    if dist < 10:
        print("Target Destroyed !!")

    CosTheta = (T_x[t] - P_x[t]) / dist
    SineTheta = (T_y[t] - P_y[t]) / dist

    x_new = P_x[t] + S * CosTheta
    y_new = P_y[t] + S * SineTheta

    P_x.append(x_new)
    P_y.append(y_new)

print(len(P_x))

plt.scatter(T_x, T_y)
plt.plot(T_x, T_y)

plt.scatter(P_x, P_y)
plt.plot(P_x, P_y)


plt.show()