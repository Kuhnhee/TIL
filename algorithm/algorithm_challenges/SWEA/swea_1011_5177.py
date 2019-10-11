#이진 힙

T = int(input())
for t in range(1, T+1):
    N = int (input())
    nums = list(map(int, input().split()))

    tree = [0] * (N+1)

    node = 1
    for num in nums:
        tree[node] = num
        temp = node
        #reHeap
        while tree[temp] < tree[temp//2]:
            tree[temp], tree[temp//2] = tree[temp//2], tree[temp]
            temp //= 2

        node += 1

    #summation
    answer = 0
    start = N
    while start!=0:
        if start == N:
            pass
        else:
            answer += tree[start]
        start //= 2
    

    print('#{} {}'.format(t, answer))