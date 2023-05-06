Z0 = [7]
U = []
a = 3  # a = 2
c = 7  # c = 5
m = 17  # m = 16


while True:

    tmp = Z0[-1]
    Zi = (a*tmp + c) % m

    if Zi in Z0:
        break
    else:
        Z0.append(Zi)
        U.append(Zi/m)


print(len(Z0))
print(Z0)
print(len(U))
print(U)
