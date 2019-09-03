T = int(input())
for t in range(T):
    N = int (input())
    nums = list(map(int,input().split()))
    
    current_max = nums[0]
    current_min = nums[0]
    for n in nums:
        if n > current_max:
            current_max = n

        if n < current_min:
            current_min = n
        
    sol = current_max-current_min

    print('#{0} {1}'.format(t+1, sol))
