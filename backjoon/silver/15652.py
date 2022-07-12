# n과 m(4) 실버3
# 중복순열
from itertools import product
n, m = map(int, input().split())
numLi = [i for i in range(1,n+1)]
pro = list(product(numLi,repeat=m))
for i in pro:
    print(*i)