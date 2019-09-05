def solution(food_times, k):

    foods = [[food, idx+1] for idx, food in enumerate(food_times)]

    idx = 0
    while k>0:
        #eat
        foods[idx][0] -= 1
        if foods[idx][0] == 0:
            foods.remove(foods[idx])
            if idx == len(foods):
                idx = 0
        else:
            idx = (idx+1)%len(foods)

        if not foods:
            return -1

        k-=1

    answer = foods[idx][1]
    return answer

if __name__ == "__main__":
    solution([3, 1, 2], 5)