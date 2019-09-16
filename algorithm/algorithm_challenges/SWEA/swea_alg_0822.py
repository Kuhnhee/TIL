from pprint import pprint
for t in range(1,11):
    V, E = map(int, input().split())
    chunk = list(map(int, input().split()))
    edges = [chunk[i:i+2] for i in range(0, len(chunk), 2)]
    vertices, adj, answer = list(range(1,V+1)), {}, []
    # adj[A]=B  -> A에 방문하기 전에 선행방문해야 할 목록 B
    for edge in edges:
        if edge[1] not in adj:
            adj[edge[1]] = [edge[0]]
        else:
            adj[edge[1]].append(edge[0])

    while len(answer)<V:
        deletes = []
        for v in vertices:
            if (v not in adj) or len(adj[v]) == 0:
                answer.append(str(v))
                deletes.append(v)
        
        for v in deletes:
            for key in adj:
                if v in adj[key]:
                    adj[key].remove(v)
            try:
                adj.pop(v)
            except:
                pass
            vertices.remove(v)

    print('#{} {}'.format(t, ' '.join(answer)))
