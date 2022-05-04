# 비밀번호 찾기 실버 4
import sys
input = sys.stdin.readline
# 입력
memo = {}
n , m = map(int, input().split())
for _ in range(n):
    site, pwd = map(str ,input().split())
    memo[site] = pwd
# 솔루션 
for _ in range(m):
    find = input().strip()
    print(memo[find])
            
            
            