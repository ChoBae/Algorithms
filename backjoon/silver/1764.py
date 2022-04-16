# 듣보잡
import sys
# 입력
n, m = map(int, sys.stdin.readline().split())
nLi = [sys.stdin.readline().strip() for i in range(n)]
mLi = [sys.stdin.readline().strip() for i in range(m)]
# set 자료형으로 중복 찾기
result = list(set(nLi) & set(mLi))
# 출력
print(len(result))
for results in sorted(result):
    print(results)