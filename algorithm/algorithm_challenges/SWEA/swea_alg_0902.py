T = int(input())
for t in range(1, T+1):
    N = int(input())

    stops = [0 for _ in range(5000)]

    for n in range(N):
        a, b = map(int, input().split())
        for num in range(a-1, b):
            stops[num] += 1

    targets = []
    P = int(input())
    for p in range(P):
        c = int(input())
        targets.append(str(stops[c-1]))

    answer = ' '.join(targets)
    print('#{} {}'.format(t, answer))