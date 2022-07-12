# n과 m(4) 실버3
# 중복 조합 문제였다.
from itertools import combinations_with_replacement
n, m = map(int, input().split())
numLi = [i for i in range(1,n+1)]
res = list(combinations_with_replacement(numLi,m))
for i in res:
    print(*i)