T = int(input())

for t in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    print('#{} {}'.format(t, nums[N//2]))