# 최대수 구하기
t = int(input())
for tc in range(1,t+1):
    numLi = list(map(int, input().split()))
    print(f"#{tc} {max(numLi)}")