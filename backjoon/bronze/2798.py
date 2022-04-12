# 블랙잭 브론즈2
from itertools import combinations
# 입력
# n(숫자의 개수), m(타겟 수)
n, m = map(int, input().split())
numLi = list(map(int, input().split())) # 숫자 리스트
comNum = list(combinations(numLi,3))    # 숫자 경우의 수
answer = 0 # 답안

# 솔루션-> 3개의 수 조합을 구해서 타겟값 이하의 값만 갱신
for com in comNum:
    tmp = sum(com)
    if tmp <= m:
        answer = max(answer, tmp)
        
# 출력
print(answer)