
def rotate(dice, action, current_pos, N, M):
    '''
    dice = [1,2,3,4,5,6]

    오른쪽으로 회전
    ->     [4,2,1,6,5,3]

    왼쪽으로 회전
    ->     [3,2,6,1,5,4]

    위쪽으로 회전
    ->     [5,1,3,4,6,2]

    아래쪽으로 회전
    ->     [2,6,3,4,1,5]

    '''
    moved = False
    new_dice = dice
    #오른쪽으로
    if action == 1:
        if current_pos[1]+1<M:
            current_pos[1]+=1
            new_dice = [dice[3],dice[1],dice[0],dice[5],dice[4],dice[2]]
            moved=True
    #왼쪽으로
    elif action == 2:
        if current_pos[1]-1>=0:
            current_pos[1]-=1
            new_dice = [dice[2],dice[1],dice[5],dice[0],dice[4],dice[3]]
            moved=True
    #위쪽으로
    elif action == 3:
        if current_pos[0]-1>=0:
            current_pos[0]-=1
            new_dice = [dice[4],dice[0],dice[2],dice[3],dice[5],dice[1]]
            moved=True
    #아래쪽으로
    elif action == 4:
        if current_pos[0]+1<N:
            current_pos[0]+=1
            new_dice = [dice[1],dice[5],dice[2],dice[3],dice[0],dice[4]]
            moved=True

    return new_dice, current_pos, moved


if __name__ == "__main__":
    N, M, x, y, K = map(int, input().split())

    field = []

    for n in range(N):
        field.append(list(map(int,input().split())))

    actions = list(map(int,input().split()))

    dice = [0]*6    #[0,0,0,0,0,0] 윗면=dice[0], 이외 인덱스는 문제 스펙상의 전개도를 따른다.

    current_pos = [x,y]

    for action in actions:

        #rotating dice
        dice, current_pos, moved = rotate(dice, action, current_pos, N, M)
        top = dice[0]
        bot = dice[-1]
        
        #checking field value
        if moved:
            if field[current_pos[0]][current_pos[1]] == 0:
                field[current_pos[0]][current_pos[1]] = bot
            else:
                dice[-1] = field[current_pos[0]][current_pos[1]]
                field[current_pos[0]][current_pos[1]] = 0

            # print("current act: ", action)
            # print("current pos: ", current_pos)
            # print("current dice: ", dice)
            # print("current field: ", field)
            print(top)
