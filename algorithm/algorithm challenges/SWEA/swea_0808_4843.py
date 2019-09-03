# SWEA 4843 특별한 정렬

def my_bubble_sort(data):
    size = len(data)

    for i in range(size-1):
        for j in range(size-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data

T = int(input())
for t in range(1,T+1):
    N = int(input())
    data = list(map(int, input().split()))
    
    sorted_data = my_bubble_sort(data)

    large_five = sorted_data[-5:][::-1]
    small_five = sorted_data[:5]

    special = []
    for i in range(5):
        special.append(large_five[i])
        special.append(small_five[i])

    answer = ''
    for num in special:
        answer += str(num)
        answer += ' '
    answer = answer[:-1]

    print('#{} {}'.format(t, answer))
    