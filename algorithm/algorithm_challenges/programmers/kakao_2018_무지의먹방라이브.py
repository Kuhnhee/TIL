def solution(food_times, k):
    food_times_dic = {}
    food_times_list = []
    totalTime = 0

    for i in range(0, len(food_times)):
        food_times_list.append([i, food_times[i]])
        totalTime+=food_times[i]

    if totalTime <= k:
        return -1

    food_times_list = sorted(food_times_list, key=lambda x:x[1])

    delTime = food_times_list[0][1]*len(food_times_list)
    i=1
    # print k
    # print delTime
    while delTime < k:
        k-=delTime
        delTime = (food_times_list[i][1]-food_times_list[i-1][1])*(len(food_times_list)-i)
        # print k, delTime
        i+=1

    print(food_times_list)
    food_times_list = sorted(food_times_list[i-1:], key=lambda x:x[0])
    # print food_times_list
    # print k
    print(i)
    print(food_times_list)
    print(k%len(food_times_list))
    return food_times_list[k%len(food_times_list)][0]+1

if __name__ == "__main__":
    # solution([3, 1, 2], 5)
    # solution([5,4,1], 200)
    # solution([7,3,4,2,5,6], 25)
    # solution([3,1,1,1,2,4,3],12)
    a = solution([4, 3, 5, 6, 2], 7)
    # a = solution([1000,500,750], 10000)
    print("answer was...", a)