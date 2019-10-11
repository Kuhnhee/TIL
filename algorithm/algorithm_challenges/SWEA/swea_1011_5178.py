#노드의 합

for t in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    
    tree = [0] * (N+1)
    for m in range(M):
        num, val = map(int, input().split())
        tree[num] = val

    for i in range(len(tree)-1, -1, -1):
        if i//2 >= 1:
            tree[i//2] += tree[i]
    
    print('#{} {}'.format(t, tree[L]))