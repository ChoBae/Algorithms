# 종이의 개수 실버2
import sys
input = sys.stdin.readline
# 종이 체크 함수
def colorCheck(row, col, n):
    global minusCnt, zeroCnt, plusCnt
    preColor = maps[row][col]
    
    for i in range(row, row + n):
        for j in range(col, col + n):
            # 색깔이 다를때마다 종이를 자름-> n//3
            if maps[i][j] != preColor:
                nextN = n // 3
                colorCheck(row, col, nextN) # 1사분면
                colorCheck(row, col + nextN, nextN) # 2사분면
                colorCheck(row, col + (2*nextN), nextN) # 3사분면
                colorCheck(row + nextN, col, nextN) # 4사분면
                colorCheck(row + nextN, col + nextN, nextN) # 5사분면
                colorCheck(row + nextN, col + (2*nextN), nextN) # 6사분면
                colorCheck(row + (2 * nextN), col, nextN) # 7사분면
                colorCheck(row + (2 * nextN), col + nextN, nextN) # 8사분면
                colorCheck(row + (2 * nextN), col + (2*nextN), nextN) # 9사분면
                return
    # 종이 추가
    if preColor == -1:
        minusCnt += 1
    elif preColor == 0:
        zeroCnt += 1
    else:
        plusCnt += 1
    return
    
#입력
maps = []
n = int(input())
minusCnt, zeroCnt, plusCnt = 0, 0, 0
visited = [[False]* n for _ in range(n)]
answers = [0, 0, 0]
for _ in range(n):
    maps.append(list(map(int,input().split())))

# 출력
colorCheck(0, 0, n)
print(minusCnt)
print(zeroCnt)
print(plusCnt)