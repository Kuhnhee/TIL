T = int(input())

for t in range(1, T+1):
    N = input()
    M = input()

    # create dict
    db = {}
    for n in N:
        if n in db:
            pass
        else:
            db[n] = 0

    for m in M:
        if m in db:
            db[m] += 1

    cmax = 0
    for k, v in db.items():
        if v > cmax:
            cmax = v

    print('#{} {}'.format(t, cmax))