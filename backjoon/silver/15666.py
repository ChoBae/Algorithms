# N과 M (12)
# 중복되는 수 + 중복조합 문제  -> set 으로 중복 제거
from itertools import combinations_with_replacement
n, m = map(int, input().split())
numLi = list(map(int, input().split())) # 1. 숫자 리스트 받아오기
numLi.sort()    # 1-1 숫자리스트 오름차순 정렬
res = list(combinations_with_replacement(numLi,m))  
res = list(set(res))    # 2. set 으로 중복제거
res.sort()# 3. 오름차순 정렬
# 출력
for i in res:
    print(*i)