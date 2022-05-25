# 가랏 ! rc 카!
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    now, result = 0, 0
    
    for _ in range(n):
        comand = list(map(int, input().split()))
        c = comand[0]
        # c가 0일때(유지)
        if c == 0:
            pass
        else:
            # 속도
            m = comand[1]
            # c가 1일때(속도 증가)
            if c == 1:
                now += m
            # c가 2일때(속도 감소)
            else:
                now -= m
                # 현재 속도가 0 미만이 되면 0 처리
                if now < 0:
                    now = 0
        # 속도 적용
        result += now
    # 출력
    print(f"#{tc} {result}")