# 새샘이의 7-3-5 게임
from itertools import combinations
t = int(input())
for tc in range(1, t+1):
    # 입력
    numLi = list(map(int, input().split()))
    comb = list(combinations(numLi,3))
    result = []
    # 경우의수 연산과정
    for com in comb:
        if sum(com) not in result: 
            result.append(sum(com))
    result.sort()
    # 출력
    print(f"#{tc} {result[-4]}")