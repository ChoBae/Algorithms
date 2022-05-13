# 교환학생 -> 75점
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    schedule = list(map(int, input().split()))
    count = 0
    while count != n:
        for i in range(len(schedule)):
            if schedule[i] == 1:
                if count == 0:
                    days = 1
                count += 1
                if count == n:
                    break
            try:
                days += 1
            
            except NameError as e:
                pass
            
    print(f"#{test_case} {days}")