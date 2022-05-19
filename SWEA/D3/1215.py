# 회문 1
t = 1
for tc in range(1, t+1):
    targetLen = int(input())
    dx = [0, targetLen]
    dy = [targetLen, 0]
    maps = [list(input()) for _ in range(8)]
    for i in range(8):
        for j in range(8):
            # 현재 위치에서 두가지 방향
            for z in range(2):
                nx = i + dx[z]
                ny = j + dy[z]
                if 0<= nx <=7 and 0 <= ny <=7:
                    print(maps[i:i+nx][j:j+ny]) 
            