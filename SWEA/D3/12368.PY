# 24시간
# 입력
T = int(input())
for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    # 솔루션
    # 24시 기준이므로 24시간을 초과했을때 24의 나머지로 변환시켜줌.
    result = a + b
    if result >= 24:
        result = result % 24
    # 출력
    print(f"#{test_case} {result}")