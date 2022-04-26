# 좌표 정렬하기 실버5
import sys
input = sys.stdin.readline
results = []

# 입력
n = int(input())    
for _ in range(n):
    x, y = map(int, input().split())
    results.append((x,y))
    
# 솔루션
# x부터 정렬하고 같을때 y로 정렬
results.sort(key=lambda x:(x[0],x[1]))

# 출력
for result in results:
    print(result[0], result[1])
