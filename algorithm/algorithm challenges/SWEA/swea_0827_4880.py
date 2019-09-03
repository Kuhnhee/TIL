'''
카드의 숫자는 각각 1은 가위, 2는 바위, 3은 보를 나타낸다.
1 < 2
2 < 3
3 < 1

9 
3 2 1 3 2 1 2 2 2

'''
def solver(players):
    l = len(players)

    if l == 1:
        return players
    elif l == 2:
        #승패결정
        if players[0][1] == players[1][1]:
            return [players[0]]
        elif players[0][1]%3 == (players[1][1]+1)%3:
            return [players[0]]
        elif players[1][1]%3 == (players[0][1]+1)%3:
            return [players[1]]
        
    else:
        # print("too large", players)
        return solver(solver(players[:(l+1)//2]) + solver(players[(l+1)//2:]))

T = int(input())

for t in range(1, T+1):
    N = int(input())
    temp = list(map(int, input().split()))

    players = []
    for idx,player in enumerate(temp):
        players.append([idx,player])

    winner = solver(players)
    print('#{} {}'.format(t, winner[0][0]+1))