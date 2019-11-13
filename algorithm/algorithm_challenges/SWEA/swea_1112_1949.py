from pprint import pprint

def movable(pos, val, digged):
    for i in range(4):
        target = [pos[0]+dr[i],pos[1]+dc[i]]

        if (not len(field)>target[0]>=0) or (not len(field)>target[1]>=0):
            continue

        if field[target[0]][target[1]] < val:
            return True
        else:
            if not digged and field[target[0]][target[1]]-K < val:
                return True
    return False

def dfs(path, digged):
    # 더 이상 갈 곳이 없는 경우 리턴
    if not movable(path[-1][:2], path[-1][2], digged):
        yield path

    else:
        pos = path[-1]
        for i in range(4):
            target = [pos[0]+dr[i],pos[1]+dc[i]]
            if (not len(field)>target[0]>=0) or (not len(field)>target[1]>=0):
                continue

            #경로 겹치는지 확인
            to_next_case = False
            for coord in path:
                if coord[:2] == target:
                    to_next_case = True
                    break
            if to_next_case:
                continue

            if field[target[0]][target[1]] < pos[2]:
                new_pos = [target[0], target[1], field[target[0]][target[1]]]
                path.append(new_pos)
                yield from dfs(path, digged)
                path.pop()
            else:
                #is it possible to dig?
                if digged or field[target[0]][target[1]]-K >= pos[2]:
                    continue 

                #decide, dig? or not?
                for j in range(2):
                    if j == 0:
                        #dig
                        new_pos = [target[0], target[1], pos[2]-1]
                        path.append(new_pos)
                        yield from dfs(path, True)
                        path.pop()
                    else:
                        #don't
                        pass

#상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    field = []
    maximum = 0
    maximums = []
    for n in range(N):
        row = list(map(int, input().split()))
        if maximum < max(row):
            maximum = max(row)
            maximums = []

        for idx, val in enumerate(row):
            if val == maximum:
                maximums.append([n, idx])

        field.append(row)

    max_length = 0
    for coord in maximums:
        for case in dfs([[coord[0], coord[1], maximum]], False):
            if len(case) > max_length:
                max_length = len(case)

    print('#{} {}'.format(t, max_length))

'''
10
5 1
9 3 2 3 2
6 3 1 7 5
3 4 8 9 9
2 3 7 7 7
7 6 5 5 8
3 2
1 2 1
2 1 2
1 2 1
5 2
9 3 2 3 2
6 3 1 7 5
3 4 8 9 9
2 3 7 7 7
7 6 5 5 8
4 4
8 3 9 5
4 6 8 5
8 1 5 1
4 9 5 5
4 1
6 6 1 7
3 6 6 1
2 4 2 4
7 1 3 4
5 5
18 18 1 8 18
17 7 2 7 2
17 8 7 4 3
17 9 6 5 16
18 10 17 13 18
6 4
12 3 12 10 2 2
13 7 13 3 11 6
2 2 6 5 13 9
1 12 5 4 10 5
11 10 12 8 2 6
13 13 7 4 11 7
7 3
16 10 14 14 15 14 14
15 7 12 2 6 4 9
10 4 11 4 6 1 1
16 4 1 1 13 9 14
3 12 16 14 8 13 9
3 4 17 15 12 15 1
6 6 13 6 6 17 12
8 5
2 3 4 5 4 3 2 1
3 4 5 6 5 4 3 2
4 5 6 7 6 5 4 3
5 6 7 8 7 6 5 4
6 7 8 9 8 7 6 5
5 6 7 8 7 6 5 4
4 5 6 7 6 5 4 3
3 4 5 6 5 4 3 2
8 2
5 20 15 11 1 17 10 14
1 1 11 16 1 14 7 5
17 2 3 4 5 13 19 20
6 18 5 16 6 7 8 5
10 4 5 4 9 2 10 16
2 7 16 5 8 9 10 11
12 19 18 8 7 11 15 12
1 20 18 17 16 15 14 13

'''