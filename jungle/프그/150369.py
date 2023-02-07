def solution(cap, n, deliveries, pickups):
    answer = 0

    while sum(deliveries) != 0 and sum(pickups) != 0:
        check = 0
        가져온택배 = cap
        여유공간 = cap - 가져온택배
        for i in range(n-1, -1, -1):
            # 남은 공간이 0일 떄
            if (가져온택배 == 0 and 여유공간 == 0):
                print("1사이클 끝")

                break
            elif deliveries[i] != 0 or pickups[i] != 0:
                print(i)
                if i > check:
                    check = i+1
                # 배달 먼저.
                if deliveries[i] <= 가져온택배:
                    가져온택배 -= deliveries[i]
                    여유공간 += deliveries[i]
                    deliveries[i] = 0
                else:
                    deliveries[i] -= 가져온택배
                    여유공간 = 가져온택배
                    가져온택배 = 0
                print("배달 끝", 가져온택배, 여유공간)
                # 다음 수거
                if pickups[i] <= 여유공간:
                    여유공간 -= pickups[i]
                    pickups[i] = 0

                elif pickups[i] <= 여유공간+가져온택배:
                    print("?")
                    여유공간 -= pickups[i]
                    가져온택배 += 여유공간
                    여유공간 = 0
                    pickups[i] = 0
                else:
                    pickups[i] -= 여유공간
                    여유공간 = 0
                print("수거 끝", 가져온택배, 여유공간)
        answer += check*2
    print(answer)
    return answer


if __name__ == '__main__':
    cap = 2
    n = 7
    deliveries = [1, 0, 2, 0, 1, 0, 2]
    pickups = [0, 2, 0, 1, 0, 2, 0]
    # cap = 4
    # n = 5
    # deliveries = [1, 0, 3, 1, 2]
    # pickups = [0, 3, 0, 4, 0]
    solution(cap, n, deliveries, pickups)
