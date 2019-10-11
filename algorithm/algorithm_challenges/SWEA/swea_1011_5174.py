from pprint import pprint
#subtree

def inorder(node):
    global answer
    if node != None:
        if node in tree:
            inorder(tree[node]['l'])
        answer += 1
        if node in tree:
            inorder(tree[node]['r'])
    return

T = int(input())
for t in range(1, T+1):
    E, N = map(int, input().split())
    edges = list(map(int,input().split()))

    tree = {}
    for i in range(1,max(edges)+1):
        tree[i] = {'l': None, 'r': None}

    for i in range(0, len(edges), 2):
        # print(edges[i], edges[i+1])
        if tree[edges[i]]['l'] == None:
            tree[edges[i]]['l'] = edges[i+1]
        elif tree[edges[i]]['l'] != None:
            tree[edges[i]]['r'] = edges[i+1]

        if edges[i+1] not in tree:
            tree[edges[i+1]] = {'l'}
            
    root = N
    answer = 0
    inorder(root)

    print('#{} {}'.format(t, answer))