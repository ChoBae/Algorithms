# N과 M (8)
# 중복 조합 문제 -> combinations_with_replacement
from itertools import combinations_with_replacement
n, m = map(int, input().split())
numLi = list(map(int, input().split())) # 1. 숫자 리스트 받아오기
numLi.sort()    # 2. 오름차순 정렬
res = list(combinations_with_replacement(numLi,m))  
# 출력
for i in res:
    print(*i)