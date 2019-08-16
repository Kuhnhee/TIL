# SWEA 4837 부분집합의 합

T = int(input())
for t in range(1, T+1):
    n, k = map(int, input().split())
    
    arr =range(1,13)
    N = len(arr)
    answers = []
    for i in range(1<<N):
        summation = 0
        temp = []
        for j in range(N+1):
            if i&(1<<j):
                summation+=arr[j]
                temp.append(arr[j])
    
        if summation==k and len(temp)==n:
            answers.append(temp)

    print('#{} {}'.format(t, len(answers)))