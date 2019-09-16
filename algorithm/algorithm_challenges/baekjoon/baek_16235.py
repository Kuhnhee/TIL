
'''
tree_field[x][y] = [
    age,
    age,
    age,
    ...
]
'''

N, M, K = map(int, input().split())

tree_field = [[0]*N for i in range(N)]
nut_field = [[5]*N for i in range(N)]

supply = []
for n in range(N):
    supply.append(list(map(int, input().split())))

for m in range(M):
    x, y, age = map(int, input().split())
    x -= 1
    y -= 1
    if tree_field[x][y] != 0:
        tree_field[x][y].append(age)
        tree_field[x][y].sort()
    else:
        tree_field[x][y] = [age]

action = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

tree_count = M
for k in range(1,K+1):
    # 봄, 여룸
    for i in range(N):
        for j in range(N):
            # in case there is no tree in current position, skip.
            if not tree_field[i][j]:
                continue

            dead_list = []

            for idx, tree in enumerate(tree_field[i][j]):
                if tree<= nut_field[i][j]:
                    nut_field[i][j] -= tree
                    tree_field[i][j][idx] += 1
                else:
                    dead_list.append(tree)
                    tree_count -= 1
            
            #delete dead trees from tree_field
            #여름
            add_nut = 0

            if dead_list:
                for dead in dead_list:
                    add_nut += dead//2
                    tree_field[i][j].pop()
                nut_field[i][j] += add_nut

    # 가을, 겨울
    for i in range(N):
        for j in range(N):
            #겨울
            nut_field[i][j] += supply[i][j]

            # in case there is no tree in current position, skip.
            if not tree_field[i][j]:
                continue

            for tree in tree_field[i][j]:
                if tree%5 == 0:
                    for l in range(8):
                        tx, ty = i+action[l][0], j+action[l][1]
                        if tx<0 or tx>=N or ty<0 or ty>=N:
                            continue

                        if tree_field[tx][ty] != 0:
                            tree_field[tx][ty].insert(0,1)
                        else:
                            tree_field[tx][ty] = [1]
                        tree_count += 1
print(tree_count)
