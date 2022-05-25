# 거듭제곱
t = 10
for _ in range(1, t+1):
    #입력
    tc = int(input())
    n, k = map(int, input().split())
    # 거듭제곱 연산
    result = n ** k
    # 출력
    print(f"#{tc} {result}")