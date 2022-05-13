# 구구단 2
# 입력
T = int(input())
for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    # 출력
    print(f"#{test_case}", end=" ")
    if a > 9 or b > 9:
        print(-1)
    else:
        print(a*b)