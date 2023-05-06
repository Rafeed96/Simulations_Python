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

plt.show()


S = 5
C_x = [50]
C_y = [50]

min_DistA = 10000000000
min_DistB = 10000000000






for t in range(20):
  
  if t < 10:
  
    distB = math.sqrt((B_x[t]-C_x[t])**2 + (B_y[t]-C_y[t])**2) 

    if distB < min_DistB:
      min_DistB = distB

    CosTheta = (B_x[t]- C_x[t]) / distB
    SineTheta = (B_y[t]- C_y[t]) / distB 

    x_new = C_x[t] + S * CosTheta
    y_new = C_y[t] + S * SineTheta

    C_x.append(x_new)
    C_y.append(y_new)

  else:

    distA = math.sqrt((A_x[t]-C_x[t])**2 + (A_y[t]-C_y[t])**2) 

    if distA < min_DistA:
      min_DistA = distA

    CosTheta = (A_x[t]- C_x[t]) / distA
    SineTheta = (A_y[t]- C_y[t]) / distA 

    x_new = C_x[t] + S * CosTheta
    y_new = C_y[t] + S * SineTheta

    C_x.append(x_new)
    C_y.append(y_new)



plt.scatter(A_x, A_y)
plt.plot(A_x, A_y)



plt.scatter(B_x, B_y)
plt.plot(B_x, B_y)



plt.scatter(C_x, C_y)
plt.plot(C_x, C_y)



if min_DistA < min_DistB:
  print("A had minimum distance ",min_DistA)
else:
  print("B had minimum distance ",min_DistB)


plt.show()