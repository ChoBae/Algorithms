# 진기의 최고급 붕어빵
t = int(input())
for tc in range(1, t+1):
    n, m, k = map(int, input().split())
    numLi = list(map(int, input().split()))
    numLi.sort()    # 오름차순 정렬
    check = True    # 가능, 불가능 체크 boolean
    for i in range(n):
        # 해당 초의 빵의 개수
        bang = (numLi[i] // m ) * k - (i+1)
        if bang < 0:
            check = False
            break
    # 출력
    result ='Possible' if check else 'Impossible'
    print(f"{tc} {result}")