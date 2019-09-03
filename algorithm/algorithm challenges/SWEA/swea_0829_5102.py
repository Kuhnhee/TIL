
import collections

T = int(input())

for t in range(1, T+1):
    V, E = map(int, input().split())

    db = {}
    for e in range(E):
        x, y = map(int, input().split())
        if x not in db:
            db[x] = [y]
        else:
            db[x].append(y)

        if y not in db:
            db[y] = [x]
        else:
            db[y].append(x)
    
    s, g = map(int, input().split())

    answer = 0
    #DFS
    visited = []
    q = collections.deque([[s,0]])
    while q:
        pos = q.popleft()
        if pos[0] == g:
            answer = pos[1]
            break

        if pos[0] in db:
            for target in db[pos[0]]:
                if target not in visited:
                    q.append([target,pos[1]+1])
                    visited.append(target)

    print('#{} {}'.format(t,answer))