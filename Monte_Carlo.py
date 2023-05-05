import numpy as np
import math


np.random.seed(1)

#equation = exp(x)

n = 1000000

f_sum = 0
f_sq_sum = 0

x_min = 3
x_max = 5

b = 2
a = 0


for i in range(n):
    x = np.random.uniform(low=a, high=b)

    y = math.exp(x)  # OR np.exp(x)

    f_sum = f_sum + y

    f_sq_sum = f_sq_sum + y**2


f_bar = f_sum/n
f_sq_bar = f_sq_sum/n
area = f_bar*(b-a)

error = ((b-a)/n**0.5)*(f_sq_bar - f_bar**2)**0.5

print(area)
print(error)
