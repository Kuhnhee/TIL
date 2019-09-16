from pprint import pprint

def solution(n, arr1, arr2):
    field = [[' ' for _ in range(n)] for _ in range(n)]
    num1, num2 = [], []
    targets = [arr1, arr2]
    results = [num1, num2]
    for choice in range(2):
        for num in targets[choice]:
            row = []
            for i in range(n-1, -1, -1):
                if num//2**i == 1:
                    row.append(1)
                    num = num%(2**i)
                else:
                    row.append(0)
            results[choice].append(row)

    for r in range(n):
        for c in range(n):
            if num1[r][c] != 0 or num2[r][c] != 0:
                field[r][c] = '#'

    answer = [''.join(i) for i in field]
    # print(answer)
    return answer

if __name__ == "__main__":
    # 5, [9, 20, 28, 18, 11], 	[30, 1, 21, 17, 28]
    solution(5, [9, 20, 28, 18, 11], 	[30, 1, 21, 17, 28])