# 수찾기 실버4

answers = []
n = int(input())
nLi = list(map(int, input().split()))
m = int(input())
mLi = list(map(int, input().split()))

for i in range(len(mLi)):
    if mLi[i] in nLi:
        mLi[i] = 1
    else:
        mLi[i] = 0

for answer in mLi:
    print(answer)