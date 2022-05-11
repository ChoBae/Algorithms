# 복제한 수열의 인버전 수
t = int(input())
for _ in range(t):
    n, k = map(int,input().split())
    numLi = list(map(int,input().split()))
    if k == 1:
        print(0)
    else:
        result = sum(numLi)* k // k
        print(result % (10**9 + 7) )        
        