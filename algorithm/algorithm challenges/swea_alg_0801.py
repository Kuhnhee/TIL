'''
정렬 문제

'''
# def my_count_sort(data):
#     num = len(data)
#     acc = []
#     result = [0]*num

#     #counting step
#     count_dict = {}
#     max_num = 0
#     for d in data:
#         if d > max_num:
#             max_num = d

    

# using sorting
for t in range(1,11):
    n = int(input())
    data = list(map(int,input().split()))
    data.sort(reverse=True)

    for i in range(n):
        data[0] -= 1
        data[-1] += 1
        data.sort(reverse=True)
        if data[0]-data[-1] <= 1:
            break
        
        
    result = data[0]-data[-1]
    print('#{0} {1}'.format(t, result))