

'''
진행방향 = [0, 1, 2, 3]
0 1
3 2

시계의 경우: 2 - (2or3) - 3 - (3or0) - 0 - (0or1) - 1
반시계의 경우: 3- (3or2) - 2 - (2or1) - 1 - (1or0) - 0  
'''

def pathfinder(N, field, start, path, former, deserts, initial=True, turn_cnt=0 ):
    head = path[-1][0]
    dx = [-1,1,1,-1]
    dy = [-1,-1,1,1]

    if head[0]==start[0]+1 and head[1]==start[1]-1 and turn_cnt <= 3:
        yield path

    else:
        if initial:
            qustn = 1
        else:
            qustn = 2

        for i in range(qustn):
            i = (former + i)%4

            if initial:
                initial = False

            target = (head[0]+dy[i],head[1]+dx[i])
            if (target[0]<0) or (target[0]>=N) or (target[1]<0) or (target[1]>=N):
                continue
            
            targetval = field[target[0]][target[1]]
            if deserts[targetval] != 0:
                continue
                
            path.append([(head[0]+dy[i],head[1]+dx[i]), field[head[0]+dy[i]][head[1]+dx[i]]])
            deserts[field[head[0]+dy[i]][head[1]+dx[i]]] += 1
            yield from pathfinder(N, field, start, path, i, deserts, initial, turn_cnt+bool(former-i))
            deserts[field[head[0]+dy[i]][head[1]+dx[i]]] -= 1
            path.pop()


T = int(input())
for t in range(1, T+1):
    field = []
    N = int(input())
    for n in range(N):
        row = list(map(int, input().split()))
        field.append(row)
    
    maxlength = 0
    deserts = [0]*101
    for i in range(N-2):
        for j in range(1,N-1):

            deserts[field[i][j]] += 1
            for path in pathfinder(N,field,(i,j),[ [(i,j),field[i][j]] ],2,deserts):
                if len(path) > maxlength:
                    maxlength = len(path)
                
            deserts[field[i][j]] -= 1

    if maxlength==0:
        maxlength-=1

    print('#{} {}'.format(t,maxlength))

   