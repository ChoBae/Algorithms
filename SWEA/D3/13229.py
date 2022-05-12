# 일요일
import sys
input = sys.stdin.readline
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
days = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
for test_case in range(1, T + 1):
    day = input().strip()
    result = 6 - days.index(day)
    if result == 0:
        result = 7
    print(f"#{test_case} {result}")