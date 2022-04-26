# 덩치 실버5
import sys
input = sys.stdin.readline
n = int(input())
Inf = []
result = []

for _ in range(n):
    kg, cm = map(int, input().split())
    Inf.append((kg, cm))

for i in Inf:
    cnt = 1
    for j in Inf:
        if i[0] < j[0] and i[1] < j[1]:
            cnt += 1
    result.append(cnt)      
print(*result)
