T = int(input())

for t in range(1,T+1):
    K, N, M = map(int, input().split())
    bats = list(map(int, input().split()))
    bats.append(N)

    charge_count = 0
    power = K
    for i in range(N+1):
        if i == N:
            break

        # i+power의 범위 이내에 배터리 있는지 여부 확인 필요
        if i in bats:
            for j in range(1,power+1):
                if i+j in bats:
                    break
            else:
                power = K
                charge_count += 1

        if power == 0:
            charge_count = 0
            break

        power -= 1
    print('#{0} {1}'.format(t,charge_count))