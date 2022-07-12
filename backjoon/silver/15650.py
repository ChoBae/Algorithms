# n과 M(2) 실버3
from itertools import combinations
n, m = map(int, input().split())
numLi = [i for i in range(1,n+1)]
comb = list(combinations(numLi,m))
for i in comb:
    print(*i)