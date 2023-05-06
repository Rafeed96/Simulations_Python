Z = [71823456]
U = []

while True:

    tmp = Z[-1]
    tmp_square = tmp**2
    last_six = tmp_square % 1000000000000
    mid_four = int(last_six / 10000)

    if mid_four in Z:
        break
    else:
        Z.append(mid_four)
        U.append(mid_four/10000)

    print(U)
    print(Z)
    print(len(Z))
