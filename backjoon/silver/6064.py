# 카잉 달력 실버1
t = int(input())
for _ in range(t):
    # 입력
    m, n, x, y = map(int, input().split())
    result = 0 # 결과값
    # m * n까지 검색
    while x <= m * n:
        if x % n == y % n:
            result = x
            break
        # x에 m을 더해도 같은 수임.
        x += m
    # 출력
    if result:
        print(result)
    else:
        print(-1)        