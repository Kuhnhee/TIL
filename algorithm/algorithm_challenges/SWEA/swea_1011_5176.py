from pprint import pprint

#이진탐색
def inorder(node):
    global inputs
    if node != None:
        inorder(graph[node]['l'])
        inputs.append(node)
        inorder(graph[node]['r'])
    return
    
T = int(input())
for t in range(1, T+1):
    N = int(input())
    keys = list(range(1, N+1))
    
    graph = {}
    for i in range(1,N+1):
        if i not in graph:
            graph[i] = {'l':None, 'r':None}
        left = i*2
        right = i*2 + 1
        if i*2 <= N:
            graph[i]['l'] = left
        if i*2+1 <= N:
            graph[i]['r'] = right

    # pprint(graph)

    inputs = []
    inorder(1)
    # print(inputs)

    i = 1
    for num in inputs:
        graph[num]['val'] = i
        i += 1

    print('#{} {} {}'.format(t, graph[1]['val'], graph[N//2]['val']))