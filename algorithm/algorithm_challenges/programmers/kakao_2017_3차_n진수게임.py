def adder(n, number):

    number.reverse()
    carry = 0
    for idx,digit in enumerate(number):
        # carry occur
        if (digit + 1) == n:
            carry = 1
            number[idx] = 0
        # no carry occurred
        else:
            digit += 1
            carry = 0
            number[idx] = digit
        if carry == 0:
            break
    # when final carry exists
    if carry == 1:
        number.append(1)
    number.reverse()
    return number

def solution(n, t, m, p):

    db = {
        10 : 'A',
        11 : 'B',
        12 : 'C',
        13 : 'D',
        14 : 'E',
        15 : 'F'
    }

    person = [0 for _ in range(m)] #튜브의 인덱스 : p-1
    num = [0]
    result = []
    initial, terminate = True, False
    idx = 0  # idx = 0 ~ m-1
    while True:

        if initial:
            initial = False
        else:
            num = adder(n, num)

        for digit in num:
            person[idx] = digit
            if idx == (p-1):
                if digit >= 10:
                    result.append(db[digit])
                else:
                    result.append(str(digit))
                if len(result) == t:
                    terminate = True
                    break
            idx = (idx+1)%m

        if terminate:
            break

    answer = ''.join(result)

    return answer

if __name__ == "__main__":
    solution(2,4,2,1)
    # a = [1]
    # a = adder(2, a)
    # print(a)