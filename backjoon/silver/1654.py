# 랜선 자르기 이분탐색 공부하자
from sys import stdin
k, n = map(int,stdin.readline().split())    # k(현재 랜선의 개수), n(필요한 랜선의 개수)
answer = 0
lanLi = [int(input()) for _ in range(k)]
lanLi.sort()
start, end = 1, sum(lanLi)//n

while end-start>= 0:
    mid = (end - start) // 2 
    tmp = 0
    
    for lan in lanLi:
        tmp += lan // mid
    
   
    if tmp >= n:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)