# N과 M (9)
# 중복되는 수를 허용하는 순열 문제 -> set으로 솔루션
from itertools import permutations
n, m = map(int, input().split())
numLi = list(map(int, input().split())) # 1. 숫자 리스트 받아오기
res = list(permutations(numLi,m))  
res = list(set(res))    # 솔루션 2. set으로 중복 제거
res.sort()# 3. 오름차순 정렬
# 출력
for i in res:
    print(*i)