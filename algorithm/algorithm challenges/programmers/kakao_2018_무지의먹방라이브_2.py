from collections import deque

def solution(food_times, k):

    sorted_foods = sorted(food_times)
    minimum = sorted_foods.pop(0)
    while k > len(sorted_foods)*minimum:

        for idx in range(len(food_times)):
            if food_times[idx] > 0:
                food_times[idx] -= minimum
            if idx < len(sorted_foods):
                if sorted_foods[idx] > 0:
                    sorted_foods[idx] -= minimum

        k -= len(sorted_foods)*minimum

        # find new minimun
        # print(sorted_foods, food_times, minimum, k)
        for idx,num in enumerate(sorted_foods):
            if num != 0:
                minimum = num
                sorted_foods = sorted_foods[idx:]
                break
        
    # print(food_times, sorted_foods, "remaining:", k)

    start_idx = 0
    for idx, num in enumerate(food_times):
        if num != 0:
            start_idx = idx
            break

    idx = (start_idx+k)%(len(sorted_foods))

    answer = idx+1
    return answer

if __name__ == "__main__":
    solution([3, 1, 2], 5)