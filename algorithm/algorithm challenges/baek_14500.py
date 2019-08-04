from pprint import pprint

def summation(field, body):
    answer = 0
    for pos in body:
        answer += field[pos[0]][pos[1]]
    return answer

N, M = map(int, input().split())

# (i, j) = field[i][j], i<N, j<M
field = []
for n in range(N):
    field.append(list(map(int,input().split())))

body_list = []
for i in range(0,N):
    for j in range(0,M):
        body = set()
        body.add((i,j))
        body.add(field[i][j])
        body_list.append(body)
        
max_val = 0
count = 1
while True:
    new_body_list = []

    for body in body_list:
        #candidate list에는 현재 body에서 확장 가능한 칸의 좌표들을 적는다.
        candidate_list = set()
        former_sum = 0
        for pos in body:
            if type(pos) == type(int()):
                former_sum = pos
                continue
            if pos[0]+1<N:
                new_pos = (pos[0]+1, pos[1])
                # if (new_pos not in body) and (new_pos not in candidate_list):
                candidate_list.add(new_pos)
            if pos[0]-1>=0:
                new_pos = (pos[0]-1, pos[1])
                # if (new_pos not in body) and (new_pos not in candidate_list):
                candidate_list.add(new_pos)
            if pos[1]+1<M:
                new_pos = (pos[0], pos[1]+1)
                # if (new_pos not in body) and (new_pos not in candidate_list):
                candidate_list.add(new_pos)
            if pos[1]-1>=0:
                new_pos = (pos[0], pos[1]-1)
                # if (new_pos not in body) and (new_pos not in candidate_list):
                candidate_list.add(new_pos)

        for candidate in candidate_list:
            if candidate in body:
                continue
            temp_body = set(body)
            temp_body.add(candidate)
            new_sum = former_sum + field[candidate[0]][candidate[1]]
            temp_body.remove(former_sum)
            temp_body.add(new_sum)

            # body.add(candidate)
            # new_sum = former_sum + field[candidate[0]][candidate[1]]
            # print(former_sum, body, count)
            # body.remove(former_sum)
            # body.add(new_sum)

            if (temp_body not in new_body_list):
                new_body_list.append(temp_body)
                if count==3:
                    if new_sum > max_val:
                        max_val = new_sum

            # if (body not in new_body_list):
            #     new_body_list.append(body)
            #     if count==3:
            #         if new_sum > max_val:
            #             max_val = new_sum

    count += 1
    body_list = new_body_list

    print("-----------------------")
    pprint(body_list)

    # if len(body_list[0]) == 4:
    #     break
    if count == 4:
        break

# find maximum
# current_max = 0
# for body in body_list:
#     new_val = summation(field, body)
#     if new_val > current_max:
#         current_max=new_val
# print(current_max)
print(max_val)
