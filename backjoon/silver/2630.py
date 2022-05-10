# 색종이 만들기
import sys
input = sys.stdin.readline
# 솔루션
# 색종이 체크 함수
def colorCk(row, col, n):
    # 변수를 글로벌 처리
    global whiteCnt, blueCnt
    preColor = maps[row][col] # 현재 색상
    
    for i in range(row, row + n):
        for j in range(col, col+ n):
            # 색상이 다를시 구간 슬라이싱
            if maps[i][j] != preColor:
                # 2**n개이기때문에 4사분면까지 체크하면 됨,
                nextN = n // 2
                colorCk(row, col, nextN)
                colorCk(row, col + nextN, nextN)
                colorCk(row+nextN, col, nextN)
                colorCk(row+nextN, col + nextN, nextN)
                return
    # 체크가 끝났을때 각각 카운트
    if preColor == 1:
        blueCnt += 1
    else:
        whiteCnt += 1
    return
# 입력
n = int(input())
whiteCnt, blueCnt = 0, 0
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))
# 출력
colorCk(0, 0, n)
print(whiteCnt)
print(blueCnt)