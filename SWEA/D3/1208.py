# Flatten 평탄화
# 입력
T = 10
for test_case in range(1, T + 1):
    n = int(input())
    boxLi = list(map(int, input().split()))
    while n != 0:
        # 덤프횟수 빼기
        n -= 1
        # 최대, 최소 높이의 박스 인덱스 찾아 옮겨주기
        maxidx = boxLi.index(max(boxLi))
        minidx = boxLi.index(min(boxLi))
        boxLi[maxidx] -= 1
        boxLi[minidx] += 1
    # 출력
    print(f"#{test_case} {max(boxLi) - min(boxLi)}")
