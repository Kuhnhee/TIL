
def grouper(groupA, groupB, depth):
    if len(groupA) + len(groupB) == len(persons):
        yield groupA, groupB
    else:
        for i in range(2):
            if i == 0:
                #go to A
                groupA.append(persons[depth])
                yield from grouper(groupA, groupB, depth+1)
                groupA.pop()
            else:
                #go to B
                groupB.append(persons[depth])
                yield from grouper(groupA, groupB, depth+1)
                groupB.pop()

def manhattan(coord1, coord2):
    return abs(coord1[0]-coord2[0]) + abs(coord1[1]-coord2[1])

def simulator(group, target):
    dists = []
    for coord in group:
        dists.append(manhattan(coord, target[:2]))
    dists.sort()

    timer, length, queue_limit = 0, target[2], 3
    queue, wait = [], []
    while (dists or queue or wait):
        timer += 1
        #계단 내려감
        for idx in range(len(queue)):
            queue[idx] -= 1
        while queue and queue[0] == 0:
            queue.pop(0)

        #대기열에 있는 사람 출발
        while wait and len(queue) < queue_limit:
            queue.append(wait.pop(0))

        #계단을 향해서 이동
        for idx in range(len(dists)):
            dists[idx] -= 1
            if dists[idx] == 0:
                wait.append(length)
        while dists and dists[0] == 0:
            dists.pop(0)
    return timer


T = int(input())
for t in range(1, T+1):
    N = int(input())
    persons = []
    stairs = []
    field = []
    for n in range(N):
        row = list(map(int, input().split()))
        field.append(row)
        for idx, val in enumerate(row):
            if val == 1:
                persons.append([n, idx])
            if val > 1:
                stairs.append([n, idx, val])

    current_min = 9999999999
    for case in grouper([], [], 0):
        groupA, groupB = case[0], case[1]
        groupA_time = simulator(groupA, stairs[0])
        groupB_time = simulator(groupB, stairs[1])
        if max(groupA_time, groupB_time) < current_min:
            current_min = max(groupA_time, groupB_time)

    print('#{} {}'.format(t, current_min))


'''
10
5
0 1 1 0 0
0 0 1 0 3
0 1 0 1 0
0 0 0 0 0
1 0 5 0 0
5
0 0 1 1 0
0 0 1 0 2
0 0 0 1 0
0 1 0 0 0
1 0 5 0 0
6
0 0 0 1 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 1 0 0 0 0
2 0 1 0 0 0
0 0 2 0 0 0
6
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
1 0 0 0 0 0
0 0 0 2 0 4
7
0 0 0 0 0 0 0
0 0 0 0 0 0 4
0 0 0 0 1 0 0
1 0 0 1 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 2 0 0 0 0 0
7
0 0 0 0 0 0 0
7 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
2 0 0 0 0 1 0
0 0 0 0 0 0 0
8
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0
2 0 0 0 0 0 0 0
0 0 0 0 0 1 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 0
0 0 0 0 1 0 0 0
8
3 0 0 0 0 0 5 0
0 0 0 0 0 0 0 0
1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
1 0 1 1 0 0 0 0
0 0 0 0 0 0 1 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
9
0 0 0 1 0 0 0 0 0
0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 8
7 0 0 0 0 1 0 0 0
0 0 0 0 0 1 1 0 0
0 0 0 0 0 0 0 0 0
1 0 0 0 0 1 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
10
0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 0 0 0 0 0
0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
3 0 1 0 1 0 0 0 0 2
1 1 0 0 1 0 1 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
'''