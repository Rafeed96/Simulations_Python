import math
import matplotlib.pyplot as plt

A_x = [0]
A_y = [0]

B_x = [0]
B_y = [0]


xa = 0
ya = 0

xb = 0
yb = 0
for t in range(20):
  xa = xa+4
  ya = 0
  
  A_x.append(xa)
  A_y.append(ya)

  xb = 0
  yb = yb+3

  B_x.append(xb)
  B_y.append(yb)


print(len(A_x))
print(A_x)
print(A_y)

plt.scatter(A_x, A_y)
plt.plot(A_x, A_y)

print(len(B_x))
print(B_x)
print(B_y)

plt.scatter(B_x, B_y)
plt.plot(B_x, B_y)

