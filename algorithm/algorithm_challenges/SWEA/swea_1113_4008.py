
def dfs(val, depth, p, s, m, d):
    global cmax, cmin

    if (p+s+m+d) == 0:
        if val > cmax:
            cmax = val
        if val < cmin:
            cmin = val

    else:
        for i in range(4):
            #p
            if i == 0 and p != 0:
                dfs(val+nums[depth+1], depth+1, p-1, s, m, d)
            #s
            elif i == 1 and s != 0:
                dfs(val-nums[depth+1], depth+1, p, s-1, m, d)
            #m
            elif i == 2 and m != 0:
                dfs(val*nums[depth+1], depth+1, p, s, m-1, d)
            #d
            elif i == 3 and d != 0:
                dfs(int(val/nums[depth+1]), depth+1, p, s, m, d-1)

#숫자 만들기
T = int(input())
for t in range(1, T+1):
    N = int(input())
    p,s,m,d = map(int, input().split())
    nums = list(map(int, input().split()))
    cmax = -9999999999
    cmin = 9999999999
    dfs(nums[0], 0, p, s, m, d)
    print('#{} {}'.format(t, cmax-cmin))
'''
10
5
2 1 0 1
3 5 3 7 9
6
4 1 0 0
1 2 3 4 5 6 
5
1 1 1 1
9 9 9 9 9 
6
1 4 0 0
1 2 3 4 5 6 
4
0 2 1 0
1 9 8 6
6
2 1 1 1
7 4 4 1 9 3 
7
1 4 1 0
2 1 6 7 6 5 8 
8
1 1 3 2
9 2 5 3 4 9 5 6 
10
1 1 5 2
8 5 6 8 9 2 6 4 3 2 
12
2 1 6 2
2 3 7 9 4 5 1 9 2 5 6 4 
'''