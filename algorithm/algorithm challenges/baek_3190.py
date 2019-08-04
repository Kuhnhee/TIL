def appleCheck(apple_pos, snake, head):
    flag = False

    if head in apple_pos:
        flag = True
        apple_pos.remove(head)

    return flag


if __name__ == "__main__":

    #######################################################

    N = int(input())    # board size
    K = int(input())    # number of apples

    apple_pos = []
    for k in range(K):
        x,y = list(map(int,input().split()))
        apple_pos.append([y,x])

    L = int(input())    # snake's rotate number
    rotate_info = []
    for l in range(L):
        x, y = input().split()
        x = int(x)
        rotate_info.append([x,y])

    #######################################################

    snake = [[1,1]]
    current_dir = "r"   # 'r', 'l', 'u', 'd'

    time = 1
    while True:

        head = snake[-1]

        if current_dir == 'r':
            if head[0]+1 <= N:
                next_coord = [head[0]+1, head[1]]

                if next_coord in snake:
                    break

                snake.append(next_coord)
                head = snake[-1]

                if not appleCheck(apple_pos, snake, head):
                    snake = snake[1:]
            else:
                break

        elif current_dir == 'l':
            if head[0]-1 > 0:
                next_coord = [head[0]-1, head[1]]

                if next_coord in snake:
                    break

                snake.append(next_coord)
                head = snake[-1]

                if not appleCheck(apple_pos, snake, head):
                    snake = snake[1:]
            else:
                break

        elif current_dir == 'u':
            if head[1]-1 > 0:
                next_coord = [head[0], head[1]-1]
                
                if next_coord in snake:
                    break

                snake.append(next_coord)
                head = snake[-1]

                if not appleCheck(apple_pos, snake, head):
                    snake = snake[1:]
            else:
                break

        elif current_dir == 'd':
            if head[1]+1 <= N:
                next_coord = [head[0], head[1]+1]

                if next_coord in snake:
                    break

                snake.append(next_coord)
                head = snake[-1]

                if not appleCheck(apple_pos, snake, head):
                    snake = snake[1:]
            else:
                break

        if rotate_info:
            # rotate worm
            current_rotate = rotate_info[0]
            if time == current_rotate[0]:
                rotate_dir = current_rotate[1]

                if rotate_dir == 'L':
                    if current_dir =='r':
                        current_dir = 'u'
                    elif current_dir == 'l':
                        current_dir = 'd'
                    elif current_dir == 'u':
                        current_dir = 'l'
                    elif current_dir == 'd':
                        current_dir = 'r'

                else:   #rotate_dir = 'R'
                    if current_dir =='r':
                        current_dir = 'd'
                    elif current_dir == 'l':
                        current_dir = 'u'
                    elif current_dir == 'u':
                        current_dir = 'r'
                    elif current_dir == 'd':
                        current_dir = 'l'

                rotate_info = rotate_info[1:]

        time += 1

    print(time)