
import collections

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    row = list(map(int,input().split()))
    pizzas = collections.deque()
    for idx in range(N):
        pizzas.append([idx, row[idx]])

    idx = 0
    cnt = M
    while True:

        popped = False
        if pizzas[0][1] != 0:
            if cnt == 1:
                answer = pizzas[0][0]+1
                break

            pizzas[0][1] //= 2
            if pizzas[0][1] == 0:
                pizzas.popleft()
                if N+idx<M:
                    pizzas.append([N+idx, row[N+idx]])
                    idx+=1
                popped = True
                cnt -= 1

        if not popped:
            pizzas.rotate(-1)

    print('#{} {}'.format(t,answer))