def DFS(base):
    global cnt, result

    if base >= nums[0]:
        if result > cnt:
            result = cnt
        return

    if cnt > result:
        return

    life = nums[base]

    for i in range(base+life, base, -1):
        cnt += 1
        DFS(i)
        cnt -= 1


T = int(input())
for t in range(1,T+1):
    nums = list(map(int, input().split()))
    result = 10000000
    cnt = -1
    DFS(1)
    print('#{} {}'.format(t, result))