# Succeptible Exposed Infected Recovered ==> SEIR Model

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


# 0 = No social distancing
# 0.1 = Masks
# 0.2 = Masks and hybrid classes
# 0.3 = Masks and hybrid classes and online classes

u = 0.1   # Social Distancing Rate = (0-1)
t_incubation = 5.1
t_infective = 3.3
R0 = 2.4  #
N = 33517  # student population


# initial number of infected and recovered individual
e0 = 1/N
i0 = 0.00
r0 = 0.00
s0 = 1 - e0 - i0 - r0
x0 = [s0, e0, i0, r0]

alpha = 1/t_incubation
gamma = 1/t_infective
beta = R0*gamma


def covid(x, t):
    s, e, i, r = x
    dx = np.zeros(4)
    dx[0] = -(1-u)*beta * s * i
    dx[1] = (1-u)*beta * s * i - alpha * e
    dx[2] = alpha * e - gamma * i
    dx[3] = gamma * i
    return dx


t = np.linspace(0, 200, 101)
x = odeint(covid, x0, t)
s = x[:, 0]
e = x[:, 1]
i = x[:, 2]
r = x[:, 3]


# plot the data
plt.figure(figsize=(8, 5))

plt.subplot(2, 1, 1)
plt.title('Social Distancing = '+str(u*100)+'%')
plt.plot(t, s, color='blue', lw=3, label='Susceptible')
plt.plot(t, r, color='red', lw=3, label='Recovered')
plt.ylabel('Fraction')
plt.legend()

plt.show()


plt.subplot(2, 1, 1)
plt.plot(t, i, color='orange', lw=3, label='Infected')
plt.plot(t, e, color='purple', lw=3, label='Exposed')
plt.ylim(0, 0.2)
plt.xlabel('Time (days)')
plt.ylabel('Fraction')
plt.legend()

plt.show()
