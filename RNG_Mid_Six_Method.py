Z = [718234]
U = []

while True:

    tmp = Z[-1]
    tmp_square = tmp**2
    last_six = tmp_square % 1000000000
    mid_six = int(last_six / 1000)

    if mid_six in Z:
        break
    else:
        Z.append(mid_six)
        U.append(mid_six/1000000)

    print(U)
    print(Z)
    print(len(Z))
