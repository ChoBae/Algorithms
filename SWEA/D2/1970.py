# 쉬운 거스름돈
t = int(input())
pay = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for tc in range(1, t+1):
    m = int(input())
    ans = [0]* 8    # 단위 별 리스트
    # 높은 거스름돈 순으로 계산
    for i in range(len(pay)):
        if m - pay[i] >= 0:
            ans[i] = m // pay[i]
            m = m % pay[i]
    # 출력
    print(f"#{tc}")
    print(*ans)
            