
def binary(arr, l, r, target, formal):
    global cnt

    m = (l+r)//2

    if arr[m] <= target:
        if arr[m] == target:
            cnt += 1
            return
        if formal == 'right':
            return
        binary(arr, m+1, r, target, 'right')

    elif arr[m] > target:
        if formal == 'left':
            return
        binary(arr, l, m-1, target, 'left')

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())

    ns = sorted(list(map(int, input().split())))
    ms = list(map(int, input().split()))

    cnt = 0
    for target in ms:
        binary(ns, 0, N-1, target, None)

    print('#{} {}'.format(t, cnt))