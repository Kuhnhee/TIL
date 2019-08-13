import itertools

def calc(nums,perm):
    current_num = nums[0]

    for idx,num in enumerate(nums[1:]):
        if perm[idx] == 0:
            current_num += num
        elif perm[idx] == 1:
            current_num -= num
        elif perm[idx] == 2:
            current_num *= num
        else:
            if current_num < 0:
                current_num *= -1
                current_num //= num
                current_num *= -1
            else:
                current_num //= num
    
    return current_num

N = int(input())
nums = list(map(int, input().split()))
calcs = list(map(int, input().split()))

adds = [0]*calcs[0]
subs = [1]*calcs[1]
muls = [2]*calcs[2]
divs = [3]*calcs[3]

choices = adds + subs + muls + divs

permutations = list(itertools.permutations(choices))
initial_sum = calc(nums, permutations[0])
current_max = initial_sum
current_min = initial_sum
for perm in permutations[1:]:
    current_sum = calc(nums,perm)
    if current_max < current_sum:
        current_max = current_sum
    if current_min > current_sum:
        current_min = current_sum

print(current_max)
print(current_min)