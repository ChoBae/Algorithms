# 평범한 배낭
# combinations 모듈 활용 완전탐색 풀이 -> 메모리 초과
from itertools import combinations
n, k = map(int, input().split())
values = []
weights = []
for _ in range(n):
    w, v = map(int, input().split())
    values.append(v)
    weights.append(w)

# dp = [0] * (k+1)
# dp[0] = 1
result = -10e9
for i in range(1,len(values)+1):
    comb = list(combinations(weights,i))
    for com in comb:
        if k >= sum(com):
            tmp = 0 
            for c in com:
                tmp += values[weights.index(c)]
            result = max(result, tmp)

print(result)