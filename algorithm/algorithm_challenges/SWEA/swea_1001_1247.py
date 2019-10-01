def distCalculator(tuple1, tuple2):
    return abs(tuple1[0]-tuple2[0]) + abs(tuple1[1]-tuple2[1])

def DFS(pos):
    global answer, current

    if current >= answer:
        return
    elif pos == home:
        answer = current
        return
    else:
        if len(visited) != N:
            for target in customers:
                if target not in visited:
                    d = distMap[pos][target]
                    visited[target] = 1
                    current += d
                    DFS(target)
                    visited.pop(target)
                    current -= d
        else:
            #go home
            d = distMap[pos][home]
            current += d
            DFS(home)
            current -= d

T = int(input())

for t in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    datas = [ (data[i],data[i+1]) for i in range(0, len(data), 2) ]
    co, home, customers = 0, 1, list(range(2,2+N))

    distMap = [[0]*(N+2) for _ in range(N+2)]
    for i in range(N+2):
        for j in range(N+2):
            if i == j or distMap[i][j] != 0:
                continue
            distMap[i][j] = distCalculator(datas[i], datas[j])

    answer, current = 1000000, 0
    visited = {}
    DFS(co)

    print('#{} {}'.format(t, answer))




'''

10
5
0 0 100 100 70 40 30 10 10 5 90 70 50 20
6
88 81 85 80 19 22 31 15 27 29 30 10 20 26 5 14
7
22 47 72 42 61 93 8 31 72 54 0 64 26 71 93 87 84 83
8
30 20 43 14 58 5 91 51 55 87 40 91 14 55 28 80 75 24 74 63
9
3 9 100 100 16 52 18 19 35 67 42 29 47 68 59 38 68 81 80 37 94 92
10
39 9 97 61 35 93 62 64 96 39 36 36 9 59 59 96 61 7 64 43 43 58 1 36
10
26 100 72 2 71 100 29 48 74 51 27 0 58 0 35 2 43 47 50 49 44 100 66 96
10
46 25 16 6 48 82 80 21 49 34 60 25 93 90 26 96 12 100 44 69 28 15 57 63
10
94 83 72 42 43 36 59 44 52 57 34 49 65 79 14 20 41 9 0 39 100 94 53 3
10
32 79 0 0 69 58 100 31 67 67 58 66 83 22 44 24 68 3 76 85 63 87 7 86
'''