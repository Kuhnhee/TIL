import math

if __name__ == "__main__":
    n = int(input())
    A = list(map(int,input().split()))
    b, c = list(map(int,input().split()))

    '''
    각 반의 인원 ai - B 의 인원을 부 감독관으로 커버해야함.
    올림(ai-b / c) = i반의 부 감독관 인원 
    '''
    answer = n
    for a in A:
        if a - b > 0:
            answer += math.ceil((a-b)/c)

    print(answer)