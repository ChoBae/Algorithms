# 수 정렬하기3
import sys
input = sys.stdin.readline
# 입력
n = int(input())

# 솔루션
# 인덱스 활용 풀이-> 평소 처럼 리스트를 활용하려 했으나 당연히 시간초과..
numidx = [0] * 10001
for _ in range(n):
    numidx[int(input())] += 1
    
# 출력
for i in range(10001):
    # 입력된 숫자일때
    if numidx[i] != 0:
        # 입력된만큼 출력
        for j in range(numidx[i]):
            print(i)