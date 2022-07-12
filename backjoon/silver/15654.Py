# n과 m(5) 실버3
# 순열 문제 -> permutatuis
from itertools import permutations
n, m = map(int, input().split())
numLi = list(map(int, input().split())) # 1. 숫자 리스트 받아오기
numLi.sort()    # 2. 오름차순 정렬
res = list(permutations(numLi,m))  
# 출력
for i in res:
    print(*i)