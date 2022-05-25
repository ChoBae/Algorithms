# 홀수만 더하기
# 홀수 체크 함수
def oddNum(num):
    if num % 2 == 0:
        return False
    return True


# 입력
T = int(input())
for test_case in range(1, T+1):
    numLi = list(map(int, input().split()))
    result = 0
    # numLi 체크
    for num in numLi:
        if oddNum(num):
            result += num
    # 출력
    print(f"#{test_case} {result}")
