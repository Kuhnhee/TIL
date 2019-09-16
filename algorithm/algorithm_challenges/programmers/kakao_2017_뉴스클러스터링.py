'''
두 집합 A, B 사이의 자카드 유사도 J(A, B)는 
두 집합의 교집합 크기를 두 집합의 합집합 크기로 나눈 값으로 정의된다.

'''


def solution(str1, str2):

    #str1, str2내에 알파벳이 아닐 경우 제외
    ns1, ns2 = '', ''
    a, b = [], []
    for i in range(len(str1)-1):
        target = str1[i:i+2].lower()
        to_next_flag = False
        for c in target:
            if not (c.islower() or c.isupper()):
                to_next_flag = True
                break
        if to_next_flag:
            continue
        a.append(target)

    for i in range(len(str2)-1):
        target = str2[i:i+2].lower()
        to_next_flag = False
        for c in target:
            if not (c.islower() or c.isupper()):
                to_next_flag = True
                break
        if to_next_flag:
            continue
        b.append(target)

    intersection, union = [], []
    a_del, b_del = [], []
    for idx, alpha in enumerate(a):
        
        for jdx, beta in enumerate(b):
            if alpha == beta and jdx not in b_del and idx not in a_del:
                a_del.append(idx)
                b_del.append(jdx)
                intersection.append(alpha)
                union.append(alpha)

    for i in a_del[::-1]:
        a.pop(i)
    for i in sorted(b_del, reverse=True):
        b.pop(i)

    if a:
        union += a
    if b:
        union += b

    if len(union) == 0:
        return 65536
    answer = int((len(intersection)/len(union))*65536)
    return answer