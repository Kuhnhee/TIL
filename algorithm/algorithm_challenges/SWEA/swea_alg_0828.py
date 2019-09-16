T = int(input())
for t in range(1, T+1):
    S = input()
    cards = []
    for i in range(0,len(S),3):
        cards.append(S[i:i+3])

    db = {
        'S' : [0 for _ in range(14)],
        'D' : [0 for _ in range(14)],
        'H' : [0 for _ in range(14)],
        'C' : [0 for _ in range(14)],
    }
    answer = 0
    for card in cards:
        if db[card[0]][int(card[1:])] != 0:
            answer = 'ERROR'
            break

        else:
            db[card[0]][int(card[1:])] = 1
            db[card[0]][0] += 1 #card count
        
    if answer != 'ERROR':
        answer = ' '.join(map(str,[13-db['S'][0], 13-db['D'][0], 13-db['H'][0], 13-db['C'][0]]))

    print('#{} {}'.format(t, answer))
'''
3
S01D02H03H04
H02H10S11H02
S10D10H10C01

'''
