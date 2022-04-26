# 체스판 다시칠하기 실버5
import sys
input = sys.stdin.readline
# 입력
n, m = map(int, input().split())
map = []
result = []
for _ in range(n):
    map.append(input())
# 솔루션
# 시작점
for x in range(n-7):# 3
    for y in range(m-7): # 6
        wCount = 0  # W로 시작한경우
        bCount = 0  # B로 시작한경우 
        # 시작점부터 8X8 부분 체크
        for i in range(x, x+8):
            for j in range(y, y+8):
                # 해당 위치의 대각선(항상 같아야함)
                if (i+j) % 2 == 0:
                    if map[i][j] != 'W':
                        wCount += 1
                    if map[i][j] != 'B':
                        bCount += 1
                # 해당 위치의 상하좌우(항상 달라야함)
                else:
                    if map[i][j] != 'B':
                        wCount += 1
                    if map[i][j] != 'W':
                        bCount += 1
        # 둘중 비교했을때 가장 작은값 넣어주기
        result.append(min(wCount, bCount))
# 출력
print(min(result))