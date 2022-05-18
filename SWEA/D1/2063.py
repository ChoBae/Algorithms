# 중간값 찾기
N = int(input())
numLi = list(map(int, input().split()))
numLi.sort()
print(numLi[len(numLi)//2])