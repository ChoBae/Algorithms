# 평균값 구하기
# 입력
T = int(input())
for test_case in range(1, T + 1):
    numLi = list(map(int,input().split()))
    # 평균 계산 round(값, 반올림할 자리) -> 두번째 파라미터값 비우면 소수점 첫번째자리 반올림
    result = round(sum(numLi) / len(numLi))
    #출력
    print(f"#{test_case} {result}")