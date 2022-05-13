# 조별과제
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    count = 0
    while n != 0:
        if n % 3 == 0:            
            count += n // 3
            n = n % 3
            continue
        n -= 4
        count += 1
    print(f"#{test_case} {count}")