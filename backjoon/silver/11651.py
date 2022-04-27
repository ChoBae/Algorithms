# 좌표 정렬하기 2
import sys
input = sys.stdin.readline
# 입력
n = int(input())
testLi = []
for _ in range(n):
    x, y = map(int, input().split())
    testLi.append((x, y))
    
# 솔루션 
# 람다식으로 y를 우선으로 정렬하고 같을시 x로 정렬
testLi.sort(key=lambda x:(x[1],x[0]))

# 출력
for test in testLi:
    print(test[0], test[1])