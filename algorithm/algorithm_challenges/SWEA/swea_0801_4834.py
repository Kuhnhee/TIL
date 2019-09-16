T = int(input())
for t in range(1,T+1):
    n = int(input())
    nums = input()

    counter = [0]*10

    #current_max=[max number, max number count]
    current_max = [-1,-1]
    for num in nums:
        counter[int(num)] += 1

        if int(num) == current_max[0]:
            current_max[1] = counter[int(num)]
        elif current_max[1] < counter[int(num)]:
            current_max = [int(num), counter[int(num)]]
        elif current_max[1] == counter[int(num)]:
            if int(num)>current_max[0]:
                current_max = [int(num), counter[int(num)]]
        else:
            pass

    print('#{0} {1} {2}'.format(t, current_max[0], current_max[1]))